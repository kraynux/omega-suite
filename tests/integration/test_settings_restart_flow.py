# Copyright (c) 2026 kraynux [kraynux@proton.me] - Licence MIT (voir fichier LICENSE)
"""Ecran Reglages : changer le style de navigation ou le profil de rendu
("redemarrage requis") propose desormais de redemarrer omega-suite TOUT
DE SUITE (bug d'ergonomie reel constate - "applique au prochain
demarrage" sans action concrete) plutot que de se contenter d'ecrire le
reglage. Meme patron que la "bascule execv" d'omega-serv
(PendingInstanceSwitch) : l'`os.execv()` lui-meme n'a jamais lieu dans
interfaces/tui/, seulement dans `omega_suite/__main__.py` APRES que
`App.run()` soit revenu - ce test s'arrete donc a `app.pending_restart`
et `app.is_running`, jamais a un vrai remplacement de processus."""
from __future__ import annotations

from textual.pilot import Pilot
from textual.widgets import Select

from omega_suite.app.dependency_container import DependencyContainer
from omega_suite.app.select_navigation_style import current_navigation_style
from omega_suite.interfaces.tui.app import OmegaSuiteApp
from omega_suite.interfaces.tui.screens.settings_screen import SettingsScreen
from omega_suite.interfaces.tui.screens.terminal_warning import TerminalWarningScreen


async def _reach_accueil(pilot: Pilot[None]) -> None:
    await pilot.press("x")
    await pilot.pause()
    if isinstance(pilot.app.screen, TerminalWarningScreen):
        await pilot.click("#continue")
        await pilot.pause()


async def test_confirming_the_restart_sets_pending_restart_and_exits(
    container: DependencyContainer,
) -> None:
    app = OmegaSuiteApp(container)
    async with app.run_test() as pilot:
        await _reach_accueil(pilot)
        app.push_screen(SettingsScreen(container=container))
        await pilot.pause()

        select = app.screen.query_one("#navigation-style-select", Select)
        select.value = "onglets"
        await pilot.pause()

        await pilot.click("#confirm")
        await pilot.pause()

    assert app.pending_restart is True
    assert not app.is_running
    # Le reglage lui-meme est deja ecrit avant meme la confirmation de
    # redemarrage (SettingsScreen.on_select_changed) - une confirmation
    # refusee laisserait donc quand meme le nouveau style persiste,
    # seulement pas encore actif pour CETTE session.
    assert current_navigation_style(settings_store=container.settings_store) == "onglets"


async def test_declining_the_restart_keeps_the_app_running(container: DependencyContainer) -> None:
    app = OmegaSuiteApp(container)
    async with app.run_test() as pilot:
        await _reach_accueil(pilot)
        app.push_screen(SettingsScreen(container=container))
        await pilot.pause()

        select = app.screen.query_one("#navigation-style-select", Select)
        select.value = "onglets"
        await pilot.pause()

        await pilot.click("#cancel")
        await pilot.pause()

        assert app.pending_restart is False
        assert app.is_running
