# Copyright (c) 2026 kraynux [kraynux@proton.me] - Licence MIT (voir fichier LICENSE)
"""Regression directe de trois bugs reels distincts trouves et corriges le
meme jour (2026-09-16/17) sur le style de navigation "onglets" (barre
persistante, D-014 point 6 revu) :

1. Chaque ecran garde SA PROPRE barre d'onglets vivante en permanence
   (`SuiteTabBar`, jamais recomposee) - rien ne la resynchronisait quand
   on REVENAIT dessus par une autre route ("je reclique sur scan, l'
   interface reste sur accueil"). Corrige par `screen_patching.py::
   wrap_screen_resume_with_tab_sync` (resync sur `on_screen_resume`).
2. Le correctif ci-dessus, naif, plantait (`ValueError: No Tab with id
   ...`, avalee en silence) quand la resync tentait de s'appliquer AVANT
   que les propres enfants `Tab` de la barre n'aient fini de monter -
   corrige via `call_after_refresh` + nouvelles tentatives bornees.
3. `Tabs._on_mount` (Textual, natif) active de lui-meme le tout premier
   onglet ("ACCUEIL", en tete de liste) au tout premier montage de
   N'IMPORTE QUELLE barre - meme celle d'un outil qui n'a rien a voir
   avec Accueil - postant un vrai `TabActivated` que `SuiteTabBar.
   on_tabs_tab_activated` traitait comme un clic reel, renvoyant l'app
   vers Accueil juste apres un changement d'outil reussi. Corrige par le
   garde `SuiteTabBar._suite_synced` (ignore toute activation tant que
   `wrap_screen_resume_with_tab_sync` n'a pas confirme le montage).

Ce test reproduit la sequence EXACTE rapportee par l'utilisateur (SCAN ->
SCAN -> ACCUEIL -> SCAN) puis l'etend a un outil jamais visite (FOLD) et
un aller-retour supplementaire, en verifiant a CHAQUE etape que le mode
de l'app, le type d'ecran affiche et l'onglet visuellement actif restent
les trois alignes - c'est precisement leur DESALIGNEMENT qui constituait
le bug a chaque fois."""
from __future__ import annotations

from textual.pilot import Pilot

from omega_suite.app.dependency_container import DependencyContainer
from omega_suite.interfaces.tui.app import OmegaSuiteApp
from omega_suite.interfaces.tui.screens.accueil import AccueilScreen
from omega_suite.interfaces.tui.screens.terminal_warning import TerminalWarningScreen
from omega_suite.interfaces.tui.widgets.suite_tab_bar import SuiteTabBar

_SCREEN_TYPE_NAME_BY_MODE = {
    "accueil": "AccueilScreen",
    "scan": "SuiteScanScreen",
    "fold": "SuiteFoldScreen",
}


async def _reach_accueil(pilot: Pilot[None]) -> None:
    await pilot.press("x")
    await pilot.pause()
    if isinstance(pilot.app.screen, TerminalWarningScreen):
        await pilot.click("#continue")
        await pilot.pause()
    assert isinstance(pilot.app.screen, AccueilScreen)


def _assert_consistent(app: OmegaSuiteApp, expected_mode: str) -> None:
    assert app.current_mode == expected_mode
    assert type(app.screen).__name__ == _SCREEN_TYPE_NAME_BY_MODE[expected_mode]
    bar = app.screen.query_one(SuiteTabBar)
    assert bar.active == expected_mode


async def test_reported_click_sequence_stays_consistent_at_every_step(
    onglets_container: DependencyContainer,
) -> None:
    app = OmegaSuiteApp(onglets_container)
    async with app.run_test() as pilot:
        await _reach_accueil(pilot)
        _assert_consistent(app, "accueil")

        for step, target in [
            ("SCAN (1ere fois, jamais visite)", "scan"),
            ("SCAN (reclique, deja actif)", "scan"),
            ("ACCUEIL", "accueil"),
            ("SCAN (3e clic)", "scan"),
            ("FOLD (jamais visite)", "fold"),
            ("ACCUEIL a nouveau", "accueil"),
            ("FOLD a nouveau (deja en cache)", "fold"),
        ]:
            await pilot.click(f"Tab#{target}")
            await pilot.pause()
            _assert_consistent(app, target)


async def test_clicking_an_accueil_grid_button_matches_clicking_its_tab(
    onglets_container: DependencyContainer,
) -> None:
    """`AccueilScreen.on_button_pressed` passe par la meme
    `request_tool_switch()` que la barre d'onglets - meme coherence
    attendue, quelle que soit la voie utilisee pour changer d'outil."""
    app = OmegaSuiteApp(onglets_container)
    async with app.run_test() as pilot:
        await _reach_accueil(pilot)
        await pilot.click("#scan")
        await pilot.pause()
        _assert_consistent(app, "scan")
