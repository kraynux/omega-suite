# Copyright (c) 2026 kraynux [kraynux@proton.me] - Licence MIT (voir fichier LICENSE)
"""Point d'entree Textual de la suite (D-014/D-015) : une seule App
Textual heberge les 7 outils comme modes/onglets. Chaque outil garde son
`HomeScreen`/ses ecrans/son CSS intacts (isolation CSS via
screen_patching.patch_tool_screens, D-015 point 1) - aucun fichier des 7
projets sources n'est modifie, seules leurs classes de widgets sont
patchees en memoire, une fois, au demarrage."""
from __future__ import annotations

import logging
from functools import partial
from pathlib import Path, PurePath
from typing import TYPE_CHECKING, ClassVar, cast

from textual.app import App, SystemCommand
from textual.binding import Binding, BindingType

from omega_suite.app.dependency_container import DependencyContainer
from omega_suite.app.select_navigation_style import current_navigation_style
from omega_suite.app.select_theme import UnknownThemeError, select_theme
from omega_suite.interfaces.tui.language_setting import notify_language_at_startup
from omega_suite.interfaces.tui.rendering.textual_theme_builder import build_all_textual_themes
from omega_suite.interfaces.tui.screen_patching import (
    patch_tool_screens,
    wrap_compose_with_tab_bar,
    wrap_screen_resume_with_tab_sync,
)
from omega_suite.interfaces.tui.screens.accueil import AccueilScreen
from omega_suite.interfaces.tui.screens.help_screen import HelpScreen
from omega_suite.interfaces.tui.screens.quit_confirm import QuitConfirmScreen
from omega_suite.interfaces.tui.screens.settings_screen import SettingsScreen
from omega_suite.interfaces.tui.screens.splash import SplashScreen
from omega_suite.interfaces.tui.screens.terminal_warning import TerminalWarningScreen
from omega_suite.interfaces.tui.startup import resolve_startup_state
from omega_suite.shared.i18n import _

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable

    from textual.screen import Screen
    from textual.worker import Worker

from omega_lib.terminal.models import RenderProfile
from omega_lib.theme.policies import TUI_THEMES

TITLE = _("Ω OMEGA-SUITE")
_STYLES_DIR = Path(__file__).parent / "styles"


class OmegaSuiteApp(App[None]):
    """Demarrage, puis enchaine splash -> (avertissement terminal) ->
    Accueil -> 7 onglets outils (D-014)."""

    TITLE = TITLE
    BINDINGS: ClassVar[list[BindingType]] = [
        Binding("q", "quit", _("Quitter"), show=True),
        Binding("ctrl+q", "quit", _("Quitter"), show=False),
        Binding("t", "cycle_theme", _("Thème suivant"), show=True),
        Binding("r", "refresh_terminal", _("Rafraîchir"), show=True),
        Binding("a", "help", _("Aide"), show=True),
        Binding("s", "reglages", _("Réglages"), show=True),
    ]

    def __init__(self, container: DependencyContainer) -> None:
        self._container = container
        self._startup_state = resolve_startup_state(settings_store=container.settings_store)
        self._profile = self._startup_state.theme.render_profile
        # Style de navigation "onglets" (barre persistante, D-014 point 6
        # revu) decide UNE FOIS au demarrage - la barre est injectee dans
        # compose(), pas rechargeable a chaud (meme raison que le profil
        # de rendu : redemarrage requis pour changer de style).
        self._onglets = current_navigation_style(settings_store=container.settings_store) == "onglets"
        self._patched_tools: set[str] = set()
        self._patch_workers: dict[str, Worker[None]] = {}
        self._pending_switch_target: str | None = None
        # Seul canal qui survit a la fermeture de l'App (meme patron que
        # PendingInstanceSwitch d'omega-serv) : le profil de rendu et le
        # style de navigation ne se rechargent pas a chaud (`self._onglets`
        # decide UNE FOIS, plus haut) - Reglages propose de relancer TOUT
        # DE SUITE plutot que de laisser "applique au prochain demarrage"
        # sans action concrete (bug d'ergonomie reel constate). L'appel
        # `os.execv()` lui-meme n'a jamais lieu ici, jamais depuis
        # interfaces.tui/ - seulement dans `omega_suite/__main__.py`,
        # APRES que `App.run()` soit revenu (Textual entierement arrete,
        # terminal restaure).
        self.pending_restart = False
        self.pending_language: str | None = None
        """Langue choisie dans les Reglages : imposee aux 7 outils au redemarrage (Q2)."""

        # Patcher les 7 outils ICI (bug reel constate - "5 secondes au
        # demarrage") forcerait a IMPORTER tous les ecrans des 7 outils
        # (et leurs dependances : httpx, cryptography, aiohttp, bs4,
        # lxml, dnspython, maxminddb, pyyaml, psutil...) avant meme le
        # premier rendu - voir `_patch_tool_once()`, appele paresseusement
        # dans `_make_home_screen_factory()`, au premier `switch_mode`
        # reel vers CET outil precis, jamais avant.
        if self._onglets:
            for suite_screen_cls in (AccueilScreen, SettingsScreen, HelpScreen):
                # Marqueur d'idempotence (bug reel constate en ecrivant
                # les tests d'integration - voir screen_patching.py::
                # patch_tool_screens) : ces classes sont PARTAGEES,
                # persistantes pour toute la duree du process - une
                # SECONDE `OmegaSuiteApp` construite dans le meme process
                # (deux tests successifs, par ex.) enveloppait sinon
                # `compose()` une seconde fois, composant deux
                # `SuiteTabBar` sur le meme ecran.
                already_wrapped = getattr(
                    suite_screen_cls.__dict__.get("compose"), "_omega_suite_tab_bar_wrapped", False
                )
                if "compose" in suite_screen_cls.__dict__ and not already_wrapped:
                    # setattr() plutot qu'une affectation directe - meme
                    # raison que screen_patching.py (types de compose()
                    # trop varies d'un ecran a l'autre pour mypy).
                    setattr(  # noqa: B010
                        suite_screen_cls, "compose", wrap_compose_with_tab_bar(suite_screen_cls.compose)
                    )
                    # Meme correctif de resynchronisation que
                    # screen_patching.py::patch_tool_screens (bug reel
                    # constate - "je reclique sur scan, l'interface reste
                    # sur accueil") : Accueil est un ecran de MODE installe
                    # une seule fois (`install_screen`), sa barre reste
                    # montee en permanence et doit se resynchroniser a
                    # chaque reprise, pas seulement a sa toute premiere
                    # construction.
                    original_resume = suite_screen_cls.__dict__.get("on_screen_resume")
                    setattr(  # noqa: B010
                        suite_screen_cls,
                        "on_screen_resume",
                        wrap_screen_resume_with_tab_sync(original_resume),
                    )

        css_path = cast(
            "list[str | PurePath]",
            [str(_STYLES_DIR / "base.tcss"), str(_STYLES_DIR / "terminal_frame.tcss")],
        )
        super().__init__(css_path=css_path)
        for theme in build_all_textual_themes():
            self.register_theme(theme)
        self.theme = self._startup_state.theme.theme_name

    def on_mount(self) -> None:
        # self.MODES (ClassVar) est copie dans self._modes DES
        # `super().__init__()` (avant que le constructeur de cette classe
        # n'ait fini) - une affectation posterieure de self.MODES n'a
        # aucun effet, `add_mode()` (API publique dediee) est la maniere
        # correcte de declarer des modes calcules dynamiquement.
        self.install_screen(AccueilScreen(), name="accueil")
        self.add_mode("accueil", "accueil")
        # `add_mode(mode, callable)` (PAS un ecran deja construit, bug
        # reel constate - "5 secondes au demarrage") : cette boucle
        # n'itere que sur les SLUGS (`adapter_factories`, un dict de
        # callables jamais appeles ici) - construire ne serait-ce qu'UN
        # `ToolAdapter` importe deja tous les ecrans de cet outil et
        # leurs dependances lourdes. Textual n'appelle ce callable qu'au
        # tout premier `switch_mode()` reel vers cet outil - un seul
        # outil importe/patche/construit a la fois, seulement quand
        # l'utilisateur y va (voir `_make_home_screen_factory`).
        for slug in self._container.adapter_factories:
            self.add_mode(slug, self._make_home_screen_factory(slug))
        notify_language_at_startup(self)
        self.push_screen(SplashScreen(), self._after_splash)

    async def request_tool_switch(self, slug: str) -> None:
        """Point d'entree UNIQUE pour changer d'outil (bouton Accueil OU
        onglet - bug reel constate : "ca fige le terminal", "l'interface
        reste sur accueil"). `_patch_tool_once()` (imports Python de tout
        l'outil, ~300-1500ms mesures) est SYNCHRONE et bloquait tout
        l'event loop pendant l'appel direct a `switch_mode()` depuis un
        clic reel - un clic souris reel arrive en 2 evenements terminal
        (bouton presse/relache) ; le gel de 1.5s au milieu desynchronise
        cette paire, d'ou l'incoherence "onglet actif" (gere par `Tabs`
        lui-meme, jamais bloque) vs "ecran affiche" (gere par
        `switch_mode`, bloque). Corrige en deportant `_patch_tool_once`
        dans un VRAI thread (`run_worker(thread=True)` - un `import`
        Python ne peut pas etre rendu asynchrone autrement) : l'event
        loop reste reactif pendant l'import, `switch_mode()` n'est appele
        qu'une fois l'outil pret, plus jamais depuis un handler qui
        bloque.

        `_pending_switch_target` (bug reel constate malgre ce qui
        precede - "le focus arrive bien sur fold, l'interface reste sur
        accueil") : `Tabs` peut re-emettre son evenement d'activation
        INITIAL (celui du tout premier montage de la barre) a un moment
        inattendu (constate y compris dans un test automatise, sans
        aucun clic reel) - une demande "accueil" fantome peut donc
        arriver juste avant une VRAIE demande "fold", creant une
        situation a deux demandes en vol simultanement si les deux
        awaits se chevauchent. Seule la DERNIERE demande enregistree
        est autorisee a appeler `switch_mode()` a la fin de son attente
        - une demande plus ancienne qui se termine apres coup ne fait
        plus rien (elle sait qu'elle est perimee).

        `_patch_workers` (bug reel constate, 2026-10-16 - "omega-fuzz
        gele silencieusement, sans message d'erreur") : la meme demande
        fantome ci-dessus peut aussi arriver pour LE MEME slug (pas
        seulement un slug different) pendant qu'un premier worker est
        deja en train d'importer/patcher cet outil - sans ce dict, une
        SECONDE demande pour "fuzz" lancerait un SECOND worker qui
        importe/monkey-patche les MEMES classes d'ecran EN PARALLELE du
        premier (aucun verrou dans `patch_tool_screens`) : deux threads
        import important simultanement un arbre de modules qui se
        chevauche est une classe connue, bien que rare, de blocage de
        l'import CPython - silencieux, sans exception, donc sans le
        moindre message a l'ecran. Une demande qui trouve deja un worker
        en vol pour ce slug REUTILISE ce worker au lieu d'en demarrer un
        second ; l'entree est retiree dans tous les cas (succes ou
        echec) pour qu'une tentative ULTERIEURE (apres un vrai echec)
        reparte sur un worker neuf plutot que de rester bloquee sur un
        resultat perime."""
        if slug == self.current_mode:
            return
        self._pending_switch_target = slug
        if slug != "accueil" and slug not in self._patched_tools:
            self.notify(_("Chargement de {upper}...").format(upper=slug.upper()), timeout=10)
            worker = self._patch_workers.get(slug)
            if worker is None:
                worker = self.run_worker(partial(self._patch_tool_once, slug), thread=True, exclusive=False)
                self._patch_workers[slug] = worker
            try:
                await worker.wait()
            finally:
                self._patch_workers.pop(slug, None)
        if self._pending_switch_target != slug:
            return
        self.switch_mode(slug)

    def _make_home_screen_factory(self, slug: str) -> Callable[[], Screen]:
        def factory() -> Screen:
            self._patch_tool_once(slug)
            adapter = self._container.get_adapter(slug)
            tool_container = self._container.get_tool_container(slug)
            return adapter.build_home_screen(tool_container)

        return factory

    def _patch_tool_once(self, slug: str) -> None:
        """Isolation CSS + redirection Quitter (D-015/D-014) - appele une
        seule fois par outil, juste avant sa toute premiere construction
        reelle (jamais a l'avance pour les 7 : voir `_make_home_screen_factory`).

        `_patched_tools.add(slug)` APRES `patch_tool_screens()` reussi,
        jamais avant (bug reel constate, 2026-10-16 : "le module
        omega-fuzz gele le logiciel", vendoring casse - voir
        build-release.sh) : marquer l'outil comme patche avant meme de
        savoir si l'import a reussi laissait un import EN ECHEC (ex.
        `ModuleNotFoundError`) figer silencieusement cet etat pour le
        reste de la session - toute nouvelle tentative sautait alors le
        worker d'import (`request_tool_switch` : `slug not in
        self._patched_tools` devenait faux) et retombait directement sur
        `switch_mode()`, qui re-appelle `_patch_tool_once` via
        `_make_home_screen_factory` - lui-meme court-circuite par la
        garde du dessus, sans jamais re-tenter le patch ni signaler quoi
        que ce soit de coherent. Si `patch_tool_screens()` leve, l'outil
        reste desormais absent de `_patched_tools` - une tentative
        ulterieure refait un essai complet, au lieu de rester bloque dans
        un etat "pretendument patche" qui ne l'a jamais ete."""
        if slug in self._patched_tools:
            return
        adapter = self._container.get_adapter(slug)
        patch_tool_screens(
            tool_slug=adapter.slug,
            screens_package_name=adapter.screens_package,
            profile=self._profile,
            inject_tab_bar=self._onglets,
        )
        self._patched_tools.add(slug)

    def _after_splash(self, _result: None) -> None:
        terminal = self._startup_state.terminal
        too_small = terminal.signals.columns < 80 or terminal.signals.rows < 24
        if terminal.render_profile == RenderProfile.MONO or too_small:
            message = (
                _("Terminal détecté : {family} ({columns}x{rows}). Rendu appliqué : {value}.").format(family=terminal.signals.family, columns=terminal.signals.columns, rows=terminal.signals.rows, value=terminal.render_profile.value)
            )
            self.push_screen(TerminalWarningScreen(message=message), self._show_accueil)
        else:
            self._show_accueil(None)

    def _show_accueil(self, _result: None) -> None:
        self.switch_mode("accueil")

    def watch_theme(self, _theme_name: str) -> None:
        terminal = self._startup_state.terminal
        self.sub_title = _("{theme} | {columns}x{rows}").format(theme=self.theme, columns=terminal.signals.columns, rows=terminal.signals.rows)

    async def action_quit(self) -> None:
        self.push_screen(QuitConfirmScreen(), self._quit_if_confirmed)

    def _quit_if_confirmed(self, confirmed: bool | None) -> None:
        if confirmed:
            self.exit()

    def action_cycle_theme(self) -> None:
        names = list(TUI_THEMES.keys())
        current_index = names.index(self.theme) if self.theme in names else 0
        next_name = names[(current_index + 1) % len(names)]
        try:
            select_theme(settings_store=self._container.settings_store, theme_name=next_name)
        except UnknownThemeError as exc:
            self.notify(str(exc), severity="error")
            return
        except OSError as exc:
            self.notify(_("Thème appliqué mais non enregistré : {exc}").format(exc=exc), severity="warning")
        self.theme = next_name

    def action_refresh_terminal(self) -> None:
        from omega_lib.infrastructure.terminal.detector import SystemTerminalDetector
        from omega_lib.terminal.service import resolve_render_profile

        from omega_suite.interfaces.tui.startup import StartupState

        terminal = resolve_render_profile(SystemTerminalDetector().detect())
        self._startup_state = StartupState(terminal=terminal, theme=self._startup_state.theme)
        self.sub_title = _("{theme} | {columns}x{rows}").format(theme=self.theme, columns=terminal.signals.columns, rows=terminal.signals.rows)
        self.notify(
            _("{family} ({columns}x{rows})").format(family=terminal.signals.family, columns=terminal.signals.columns, rows=terminal.signals.rows),
            title=_("Terminal rafraîchi"),
        )

    def action_help(self) -> None:
        """Dispatch contextuel (D-014 point 10) : Aide de la suite depuis
        Accueil, Aide DE L'OUTIL ACTIF (classe inchangee) depuis un onglet."""
        if self.current_mode == "accueil":
            self.push_screen(HelpScreen())
            return
        if self.current_mode not in self._container.adapter_factories:
            self.push_screen(HelpScreen())
            return
        adapter = self._container.get_adapter(self.current_mode)
        import importlib

        help_module = importlib.import_module(f"{adapter.screens_package}.help_screen")
        self.push_screen(help_module.HelpScreen())

    def action_reglages(self) -> None:
        self.push_screen(SettingsScreen(container=self._container))

    def get_system_commands(self, screen: Screen) -> Iterable[SystemCommand]:
        """Socle generique uniquement (D-015 point 4) : les extras propres
        a un outil (raccourcis de navigation TRACK, etc.) ne sont pas
        reproduits ici, deliberement - restent atteignables depuis le menu
        de l'onglet concerne."""
        yield SystemCommand(_("Thème"), _("Changer le thème actif"), self.action_change_theme)
        yield SystemCommand(_("Réglages"), _("Ouvrir les réglages de la suite"), self.action_reglages)
        yield SystemCommand(_("Aide"), _("Ouvrir l'aide"), self.action_help)
        yield SystemCommand(
            _("Quitter"), _("Quitter omega-suite (avec confirmation)"), self.action_quit
        )
        yield SystemCommand(
            _("Capture d'écran"),
            _("Enregistrer une capture SVG de l'écran courant"),
            self._deliver_screenshot_for_active_tool,
        )

    def _deliver_screenshot_for_active_tool(self) -> None:
        """Dossier de captures de l'OUTIL ACTIF (D-015 point 4) - la
        cle exacte du reglage "dossier override" differe d'un outil a
        l'autre (verifie : STRESS n'utilise pas la meme cle que les 6
        autres), on se contente donc du dossier par defaut de l'outil,
        toujours present sous le meme nom d'attribut."""
        container = self._container.tool_containers.get(self.current_mode)
        default_dir = getattr(container, "default_exports_dir", None) or getattr(
            container, "export_dir", None
        )
        directory = default_dir or (self._container.var_dir / "screenshots")
        directory.mkdir(parents=True, exist_ok=True)
        self.deliver_screenshot(path=str(directory))

    def _handle_exception(self, error: Exception) -> None:
        logging.getLogger("omega_suite").error(
            "Exception non prevue (onglet: %s)", self.current_mode, exc_info=error
        )
        self.notify(
            str(error) or type(error).__name__,
            title=_("Erreur inattendue"),
            severity="error",
            timeout=10,
        )
