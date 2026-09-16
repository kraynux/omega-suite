# Copyright (c) 2026 kraynux [kraynux@proton.me] - Licence MIT (voir fichier LICENSE)
"""Isolation CSS entre les 7 outils fusionnes en onglets d'une seule
`App` Textual (D-015 point 1, ~/DEV/SUITE/DECISIONS_ARCHITECTURE.md).

Un `#id`/`.classe` Textual est global au DOM et `App.CSS_PATH`
(fichiers) n'est JAMAIS scope par Textual (verifie dans le source :
`App._load_screen_css` ne passe `scope=` qu'a `screen.CSS`, jamais a
`screen.css_path`) - charger simultanement les feuilles de style de 2+
outils dans une seule App provoque une fuite de style entre eux des
qu'un selecteur partage (`.omega-form-panel`, `#exports-dir-input`, ...)
diverge, meme legerement, d'un outil a l'autre.

Correctif valide empiriquement (spike, voir D-015) : le mecanisme natif
`SCOPED_CSS` de Textual (actif par defaut) isole correctement le CSS
d'un ecran des lors que (a) le CSS est charge via `.CSS` (chaine), jamais
`.CSS_PATH` (fichiers, jamais scope), et (b) l'ecran porte un
`_css_type_name`/`_css_type_names` DISTINCT par outil - le moteur de
correspondance de type verifie `scope in node._css_type_names`
(`textual/css/model.py`), un frozenset, pas `_css_type_name` (singulier,
ne sert qu'au cache/etiquetage) : patcher uniquement `_css_type_name`
sans `_css_type_names` echoue silencieusement (aucune exception, le
style ne s'applique juste jamais).

Cette fonction PATCHE LES CLASSES D'ORIGINE en place (jamais de
sous-classe) : chaque outil instancie ses propres ecrans via son propre
code interne (`home.py::_screen_for()`, boutons, etc.) que cette suite
ne modifie jamais - une sous-classe creee ici ne serait tout simplement
jamais utilisee par cette navigation interne. Patcher l'objet classe
partage, une seule fois au demarrage de la suite, fait beneficier TOUTE
la navigation interne du correctif sans toucher un seul fichier des 7
projets sources."""
from __future__ import annotations

import importlib
import pkgutil
from collections.abc import Callable
from pathlib import Path
from types import ModuleType
from typing import Any

from omega_lib.terminal.models import RenderProfile
from textual.screen import Screen

_STYLESHEET_FILES = ("base.tcss", "terminal_frame.tcss")

_TAB_BAR_CSS = """
.omega-suite-tab-bar {
    dock: top;
    margin-top: 1;
}
.omega-suite-tab-bar #tabs-list {
    align-horizontal: center;
}
"""
"""Style minimal de la barre d'onglets persistante (widgets/suite_tab_bar.py)
- injectee dans le CSS de CHAQUE outil quand le style de navigation
"onglets" est actif (D-014 point 6 revu), puisque le CSS de chaque outil
est isole (D-015 point 1) et ne connait sinon pas cette classe.

`margin-top: 1` (bug reel constate - "menu onglet marche pas") : deux
widgets "dock: top" ne s'empilent PAS forcement l'un au-dessus de
l'autre - verifie par un test isole, sans rapport avec Tabs, que
`Header()` ignore l'ordre de montage et reste toujours epingle a la
toute premiere ligne, SUPERPOSANT tout autre widget "dock: top" au lieu
de s'empiler avec lui. La barre d'onglets etait donc recouverte par le
Header de chaque outil, qui interceptait tous les clics a sa place -
aucune exception levee, juste des clics qui n'atteignaient jamais la
barre. Un decalage explicite d'une ligne (la hauteur de Header, fixe
dans toute la suite) evite le recouvrement sans dependre d'un ordre de
montage qui ne fonctionne pas ici."""


def _read_tool_css(styles_dir: Path, profile: RenderProfile, *, inject_tab_bar: bool) -> str:
    names = (*_STYLESHEET_FILES, f"{profile.value}.tcss")
    text = "\n".join((styles_dir / name).read_text(encoding="utf-8") for name in names)
    if inject_tab_bar:
        text += _TAB_BAR_CSS
    return text


def wrap_compose_with_tab_bar(original_compose: Callable[..., Any]) -> Callable[..., Any]:
    """Enveloppe `compose()` d'un ecran pour faire apparaitre la barre
    d'onglets persistante EN PREMIER - jamais une modification du fichier
    source de l'ecran, juste de la methode en memoire (meme principe que
    le reste de ce module). La barre est deposee au-dessus du Header
    propre a l'ecran via un decalage CSS explicite (`margin-top: 1`,
    `_TAB_BAR_CSS` plus haut) et non un ordre de montage : verifie que
    deux widgets "dock: top" ne s'empilent PAS forcement l'un sur l'autre
    - `Header()` reste toujours epingle a la toute premiere ligne quel
    que soit l'ordre de montage, superposant sinon tout ce qui partage
    "dock: top" avec lui.

    Signature volontairement large (`Callable[..., Any]`) : `compose()`
    varie legerement de type ("Iterable[Widget]" vs "ComposeResult"
    selon l'ecran d'origine) - cette fonction reste generique."""

    def compose(self: Screen) -> Any:
        from omega_suite.interfaces.tui.widgets.suite_tab_bar import KNOWN_SLUGS, SuiteTabBar

        # Bug reel constate ("no tabs with ids default") : "s"/"a"
        # (Reglages/Aide de la suite, tous deux patches ici aussi) restent
        # actifs meme PENDANT le splash - avant le tout premier
        # `switch_mode()`, `App.current_mode` vaut encore `"_default"`
        # (`App.DEFAULT_MODE`, Textual), qui n'est pas un de nos slugs.
        current_mode = getattr(self.app, "current_mode", None)
        if current_mode not in KNOWN_SLUGS:
            current_mode = "accueil"
        yield SuiteTabBar(active_slug=current_mode)
        yield from original_compose(self)

    # Marqueur d'idempotence (bug reel constate en ecrivant les tests -
    # voir docstring de `patch_tool_screens`/la boucle de App.__init__) :
    # sans lui, une DEUXIEME `OmegaSuiteApp` construite dans le MEME
    # process (deux tests successifs, par ex.) envelopperait `compose()`
    # UNE SECONDE FOIS, puisque le patch modifie la classe PARTAGEE
    # (persistante pour toute la duree du process), pas une instance -
    # deux `SuiteTabBar` finiraient alors composees sur le meme ecran.
    compose._omega_suite_tab_bar_wrapped = True  # type: ignore[attr-defined]
    return compose


def wrap_screen_resume_with_tab_sync(
    original_on_screen_resume: Callable[[Any], None] | None,
) -> Callable[[Any], None]:
    """Enveloppe (ou cree) `on_screen_resume()` pour REsynchroniser la
    barre d'onglets de CET ecran sur `App.current_mode` a chaque reprise
    - bug reel constate ("je reclique sur scan, l'interface reste sur
    accueil") : `compose()` ne fixe l'onglet actif QU'A LA TOUTE PREMIERE
    construction de l'ecran (une fois pour toute sa duree de vie, un
    ecran de mode reste MONTE en permanence, jamais recompose). Cliquer
    un onglet MET A JOUR la barre SUR LAQUELLE ON A CLIQUE (comportement
    natif de `Tabs`, correct) mais ne touche jamais a la barre de l'ecran
    qu'on QUITTE - en y revenant plus tard, cette barre affiche encore le
    dernier onglet clique dessus il y a longtemps, pas l'onglet reel.
    Pire : `Tabs` ne re-emet meme pas l'evenement d'activation si on
    reclique sur un onglet DEJA marque actif (meme perime) - la barre
    reste bloquee, invisible tant qu'on ne clique pas un AUTRE onglet.
    `Screen.post_message(events.ScreenResume())` (Textual) est envoye a
    CHAQUE `switch_mode()`, y compris le tout premier (resynchronisation
    alors sans effet, deja correcte) - point d'ancrage fiable.

    `call_after_refresh` (bug reel constate par un spike cible - une
    `ValueError: No Tab with id ...` levee ICI MEME et avalee en silence
    par `App._handle_exception`, laissant la barre sans aucun onglet
    actif ni focus) : pour un ecran de mode visite pour la PREMIERE fois,
    `ScreenResume` est envoye des la pose de l'ecran sur la pile, AVANT
    que les enfants `Tab` de sa propre `SuiteTabBar` (montes par le
    `compose()` de `Tabs` lui-meme, asynchrone) aient fini de monter -
    `bar.active = current_mode` retombe alors dans `Tabs.validate_active`
    qui interroge `#tabs-list > #{id}` et ne trouve encore personne.
    Reporter la resynchronisation au prochain rafraichissement laisse le
    temps a ce montage de se terminer - avec une nouvelle tentative (max
    5, `_MAX_SYNC_ATTEMPTS`) si meme ce premier rafraichissement ne
    suffit pas, plutot que d'abandonner en silence : un ecran visite une
    seule fois dans toute la session (le cas le plus courant) ne
    beneficierait sinon jamais d'un `on_screen_resume` ulterieur pour
    rattraper le coup.

    Marque aussi `SuiteTabBar._suite_synced = True` une fois le montage
    confirme (widgets/suite_tab_bar.py) - leve le garde qui, jusque la,
    fait ignorer par cette barre precise toute activation d'onglet
    (bug reel constate - "l'ecran finit par revenir tout seul sur
    accueil") : faute de `active=` fourni au constructeur de `Tabs`
    (meme raison que ci-dessus - eviter le crash de montage), `Tabs.
    _on_mount` active de lui-meme, nativement, son tout premier onglet
    ("ACCUEIL", en tete de `_TAB_ITEMS`) des le premier montage de
    CHAQUE barre, meme celle d'un outil qui n'a rien a voir avec Accueil
    - ce n'est pas un clic, mais cela poste quand meme un vrai
    `TabActivated` que `SuiteTabBar.on_tabs_tab_activated` traiterait
    sinon comme une vraie demande de retour a Accueil, juste apres que
    l'utilisateur ait choisi un autre outil."""

    def on_screen_resume(self: Screen) -> None:
        if original_on_screen_resume is not None:
            original_on_screen_resume(self)

        _MAX_SYNC_ATTEMPTS = 5

        def sync_tab_bar(attempt: int = 1) -> None:
            from omega_suite.interfaces.tui.widgets.suite_tab_bar import SuiteTabBar

            current_mode = getattr(self.app, "current_mode", None)
            if not current_mode:
                return
            try:
                bar = self.query_one(SuiteTabBar)
            except Exception:  # noqa: BLE001 - NoMatches si jamais l'ecran n'a pas de barre
                return
            if not bar.query(f"#tabs-list > #{current_mode}"):
                # Tab pas encore monte (voir docstring) - reessayer au
                # prochain rafraichissement plutot que planter ou
                # abandonner definitivement.
                if attempt < _MAX_SYNC_ATTEMPTS:
                    self.call_after_refresh(lambda: sync_tab_bar(attempt + 1))
                return
            if bar.active != current_mode:
                bar.active = current_mode
            bar._suite_synced = True

        self.call_after_refresh(sync_tab_bar)

    on_screen_resume._omega_suite_tab_bar_wrapped = True  # type: ignore[attr-defined]
    return on_screen_resume


def _iter_screen_classes(screens_package: ModuleType) -> list[type[Screen]]:
    """Classes `Screen` definies DANS ce package (pas les classes de base
    importees d'ailleurs, ex. `textual.screen.Screen` lui-meme, ni une
    classe reexportee d'un autre module sans y etre definie)."""
    found: list[type[Screen]] = []
    package_path = screens_package.__path__
    prefix = screens_package.__name__ + "."
    module_names = [screens_package.__name__]
    module_names += [info.name for info in pkgutil.iter_modules(package_path, prefix)]
    for module_name in module_names:
        module = importlib.import_module(module_name)
        for obj in vars(module).values():
            if (
                isinstance(obj, type)
                and issubclass(obj, Screen)
                and obj.__module__ == module.__name__
            ):
                found.append(obj)
    return found


def _redirect_quit_to_accueil(self: Screen, confirmed: bool | None) -> None:
    """Remplace `_quit_if_confirmed` du `HomeScreen` de chaque outil
    (D-014 point 9) : ferme aujourd'hui toute l'appli standalone via
    `self.app.exit()` - en suite, doit revenir a l'onglet Accueil plutot
    que fermer omega-suite entier. Nom de methode verifie identique
    caractere pour caractere dans les 7 `home.py`."""
    if confirmed:
        self.app.switch_mode("accueil")


def patch_tool_screens(
    *,
    tool_slug: str,
    screens_package_name: str,
    profile: RenderProfile,
    inject_tab_bar: bool = False,
) -> None:
    """Patche en place, une seule fois PAR CLASSE (voir `already_wrapped`
    plus bas - bug reel constate en ecrivant les tests d'integration :
    `App._patched_tools` n'empeche un double-patch QUE pour la duree de
    vie d'UNE App ; une SECONDE `OmegaSuiteApp` construite dans le meme
    process, appelant cette fonction une seconde fois sur les MEMES
    classes partagees, enveloppait `compose()`/`on_screen_resume()` deux
    fois - deux `SuiteTabBar` composees sur le meme ecran, la resync
    levant alors `TooManyMatches`, avalee en silence, bloquant `_suite_synced`
    a `False` pour toujours), toutes les classes `Screen` du package
    `screens_package_name` (ex. `"omega_check.interfaces.tui.screens"`)
    d'un outil : isolation CSS (voir docstring du module) + redirection
    du "Quitter" interne de l'ecran d'accueil vers l'onglet Accueil de la
    suite + (si `inject_tab_bar`, style de navigation "onglets") barre
    persistante ajoutee au-dessus de chaque ecran."""
    screens_package = importlib.import_module(screens_package_name)
    assert screens_package.__file__ is not None
    styles_dir = Path(screens_package.__file__).parent.parent / "styles"
    css_text = _read_tool_css(styles_dir, profile, inject_tab_bar=inject_tab_bar)

    # UN SEUL scope/identite PAR OUTIL (pas par classe d'ecran) - bug de
    # performance reel constate ("pas tres fluide, ca met du temps") :
    # `App._load_screen_css` met en cache la source CSS d'un ecran sous
    # `read_from = (inspect.getfile(screen.__class__), f"{screen.__class__.__name__}.CSS")`
    # - deux composants qui different NATURELLEMENT par fichier/classe
    #   concrete, meme quand le contenu CSS assigne est IDENTIQUE (c'est
    #   toujours le cas ici : tous les ecrans d'un outil recoivent le
    #   meme `css_text`). Chaque ecran distinct declenchait donc une
    #   entree SEPAREE dans `Stylesheet.source`, et `Stylesheet.reparse()`
    #   reconstruit tout depuis une Stylesheet NEUVE a chaque nouvelle
    #   entree (`Stylesheet.reparse()`, cache de parsing jamais reutilise
    #   d'un reparse a l'autre par construction) - mesure : ~1-2 secondes
    #   par PREMIERE visite d'un ecran, avec le cout total qui grossit a
    #   mesure que l'utilisateur visite plus d'ecrans distincts.
    # Correctif : forcer TOUS les ecrans d'un meme outil a partager le
    # MEME `read_from`, en leur donnant le meme `__name__` ET le meme
    # `__module__` (fictif - `inspect.getfile` leve alors `TypeError`,
    # deja rattrapee dans `_load_screen_css`, qui retombe sur un
    # `screen_path` vide, identique pour tous) - une seule entree de
    # source par outil au lieu d'une par ecran, quel que soit le nombre
    # d'ecrans visites. Sans danger : `CSS_PATH` est deja vide (voir plus
    # bas), donc aucun autre code de Textual n'appelle `inspect.getfile`
    # sur ces classes (verifie dans le source de Textual).
    shared_type_name = f"Suite{tool_slug}Screen"
    shared_module_name = f"_omega_suite_patched_{tool_slug.lower()}"

    for screen_cls in _iter_screen_classes(screens_package):
        screen_cls.CSS = css_text
        screen_cls.CSS_PATH = []
        screen_cls._css_type_name = shared_type_name
        screen_cls._css_type_names = frozenset({shared_type_name}) | screen_cls._css_type_names
        screen_cls.__name__ = shared_type_name
        screen_cls.__module__ = shared_module_name
        if "_quit_if_confirmed" in screen_cls.__dict__:
            # setattr() plutot qu'une affectation directe : `screen_cls`
            # est type `type[Screen]` pour mypy, qui ne connait pas cet
            # attribut (present seulement sur le HomeScreen de chaque
            # outil) - setattr() evite un type: ignore fragile.
            setattr(screen_cls, "_quit_if_confirmed", _redirect_quit_to_accueil)  # noqa: B010
        already_wrapped = getattr(
            screen_cls.__dict__.get("compose"), "_omega_suite_tab_bar_wrapped", False
        )
        if inject_tab_bar and "compose" in screen_cls.__dict__ and not already_wrapped:
            setattr(screen_cls, "compose", wrap_compose_with_tab_bar(screen_cls.compose))  # noqa: B010
            original_resume = screen_cls.__dict__.get("on_screen_resume")
            setattr(  # noqa: B010
                screen_cls, "on_screen_resume", wrap_screen_resume_with_tab_sync(original_resume)
            )
