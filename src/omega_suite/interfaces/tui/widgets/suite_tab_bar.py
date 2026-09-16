# Copyright (c) 2026 kraynux [kraynux@proton.me] - Licence MIT (voir fichier LICENSE)
"""Barre d'onglets persistante (style de navigation "onglets", D-014
point 6 revu) : injectee au-dessus de CHAQUE ecran (les 7 outils et la
suite elle-meme, patche par screen_patching.py) quand ce style est actif,
pour permettre de changer d'outil sans repasser par Accueil, meme depuis
un ecran profondement empile (Historique, Reglages d'un outil, ...).

Libelles COURTS sur la barre elle-meme (D-014 point 6) - le nom complet
n'apparait que sur les boutons de la grille Accueil, jamais ici, pour ne
jamais avoir besoin du plein ecran."""
from __future__ import annotations

from textual.widgets import Tab, Tabs

# Ordre = ordre de lecture de la grille Accueil (gauche->droite,
# haut->bas) pour les seuls outils, Accueil ajoute en premier.
_TAB_ITEMS: tuple[tuple[str, str], ...] = (
    ("accueil", "ACCUEIL"),
    ("scan", "SCAN"),
    ("fuzz", "FUZZ"),
    ("fold", "FOLD"),
    ("stress", "STRESS"),
    ("check", "CHECK"),
    ("deep", "DEEP"),
    ("track", "TRACK"),
)

KNOWN_SLUGS = frozenset(slug for slug, _ in _TAB_ITEMS)
"""Exporte pour screen_patching.py::wrap_compose_with_tab_bar - seule
source de verite sur les onglets reellement construits ci-dessous."""


class SuiteTabBar(Tabs):
    """Une instance par ecran (patche par screen_patching.py) - reagit a
    sa propre selection en basculant le mode de la suite, jamais un
    widget partage entre plusieurs ecrans (chaque ecran patche compose
    la sienne, comme il composerait son propre Header)."""

    def __init__(self, *, active_slug: str) -> None:
        tabs = [Tab(label, id=slug) for slug, label in _TAB_ITEMS]
        # Defense en profondeur (bug reel constate - "s"/"a" restent
        # actifs meme pendant le splash, avant le tout premier
        # `switch_mode()` : `App.current_mode` vaut alors encore
        # "_default", Textual, pas un de nos slugs) : si jamais un
        # appelant passe un slug inconnu, retomber sur "accueil" plutot
        # que de laisser `Tabs` lever `ValueError: No Tab with id ...`.
        # La verification "en amont" vit aussi dans screen_patching.py,
        # celle-ci reste un filet supplementaire.
        if active_slug not in KNOWN_SLUGS:
            active_slug = "accueil"
        # PAS de `active=active_slug` ici (bug reel constate par un spike
        # cible - une `ValueError: No Tab with id ...` levee DANS
        # `Tabs._on_mount` lui-meme et avalee en silence, laissant la
        # barre sans onglet actif ni focus) : ce parametre fait executer
        # `self.active = self._first_active` (`Tabs._on_mount`, Textual)
        # SANS le `try/except NoMatches` que le chemin de repli (aucun
        # `active` fourni, choisit le premier onglet) possede - et le
        # Mount de CETTE `Tabs` peut survenir AVANT que ses propres
        # enfants `Tab` (montes par son propre `compose()`) ne le soient,
        # notamment pour l'ecran d'un outil visite pour la premiere fois
        # via `switch_mode()`. Laisser Textual choisir son repli sur
        # place (sans risque, deja protege) puis `screen_patching.py::
        # wrap_screen_resume_with_tab_sync` impose le VRAI onglet actif
        # juste apres, via `call_after_refresh` (donc une fois les Tab
        # enfants surement montes).
        super().__init__(*tabs, classes="omega-suite-tab-bar")
        self._suite_synced = False
        """Faux jusqu'a ce que `screen_patching.py::wrap_screen_resume_with_tab_sync`
        ait impose au moins une fois le VRAI onglet actif (bug reel
        constate par un spike cible - "je clique sur scan, l'ecran finit
        par revenir tout seul sur accueil") : `Tabs._on_mount`, faute de
        `active=` fourni au constructeur (voir plus haut), active QUAND
        MEME automatiquement son tout premier onglet ("ACCUEIL", en tete
        de `_TAB_ITEMS`) des son tout premier montage - un comportement
        NATIF de Tabs, pas un clic - et ce choix POSTE un vrai
        `TabActivated`. Sans ce garde, `on_tabs_tab_activated` ci-dessous
        le traiterait comme un clic reel sur ACCUEIL et redemanderait un
        `switch_mode("accueil")` juste APRES que l'utilisateur ait
        reellement choisi un autre outil - exactement le symptome
        observe. Tant que ce drapeau est faux, les activations sont
        ignorees (l'affichage interne de `Tabs` - soulignement, classe
        "-active" - continue de fonctionner normalement, seule la
        navigation de la suite est mise en pause)."""

    async def on_tabs_tab_activated(self, event: Tabs.TabActivated) -> None:
        """`await` (pas un `self.app.switch_mode(target)` direct, bug reel
        constate - "ca fige le terminal", incoherence onglet actif/ecran
        affiche) : `OmegaSuiteApp.request_tool_switch()` deporte l'import
        potentiellement lent (outil jamais visite cette session) dans un
        thread reel avant de changer de mode - jamais un appel bloquant
        depuis ce handler de clic."""
        event.stop()
        if not self._suite_synced:
            return
        target = event.tab.id
        if target:
            await self.app.request_tool_switch(target)  # type: ignore[attr-defined]
