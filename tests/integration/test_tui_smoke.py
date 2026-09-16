# Copyright (c) 2026 kraynux [kraynux@proton.me] - Licence MIT (voir fichier LICENSE)
"""Smoke test : demarrage complet (splash -> avertissement terminal
eventuel -> accueil), cycle de theme, sortie avec confirmation. Meme
patron que omega_track/tests/integration/test_tui_smoke.py - assertions
structurelles (Pilot), jamais de capture d'ecran (deja documente ailleurs
dans la suite comme peu fiable pour ce genre d'interface : un artefact de
rendu SVG peut deplacer visuellement des caracteres de dessin de boite
sans que le Text sous-jacent ne change)."""
from __future__ import annotations

from textual.pilot import Pilot

from omega_suite.app.dependency_container import DependencyContainer
from omega_suite.interfaces.tui.app import OmegaSuiteApp
from omega_suite.interfaces.tui.screens.accueil import AccueilScreen
from omega_suite.interfaces.tui.screens.terminal_warning import TerminalWarningScreen


async def _reach_accueil(pilot: Pilot[None]) -> None:
    """Ferme le splash (n'importe quelle touche), puis franchit
    l'avertissement terminal s'il apparait (profil MONO ou terminal trop
    petit - depend de l'environnement reel d'execution des tests)."""
    await pilot.press("x")
    await pilot.pause()
    if isinstance(pilot.app.screen, TerminalWarningScreen):
        await pilot.click("#continue")
        await pilot.pause()
    assert isinstance(pilot.app.screen, AccueilScreen)


async def test_app_reaches_accueil_after_splash(container: DependencyContainer) -> None:
    app = OmegaSuiteApp(container)
    async with app.run_test() as pilot:
        await _reach_accueil(pilot)


async def test_quit_requires_confirmation(container: DependencyContainer) -> None:
    app = OmegaSuiteApp(container)
    async with app.run_test() as pilot:
        await _reach_accueil(pilot)
        await pilot.press("q")
        await pilot.pause()
        assert app.is_running
        await pilot.click("#confirm")
    assert not app.is_running


async def test_theme_cycle_key_changes_theme_for_the_whole_suite(container: DependencyContainer) -> None:
    app = OmegaSuiteApp(container)
    async with app.run_test() as pilot:
        await _reach_accueil(pilot)
        initial_theme = app.theme
        await pilot.press("t")
        await pilot.pause()
        assert app.theme != initial_theme


async def test_help_is_reachable_from_accueil(container: DependencyContainer) -> None:
    app = OmegaSuiteApp(container)
    async with app.run_test() as pilot:
        await _reach_accueil(pilot)
        await pilot.press("a")
        await pilot.pause()
        assert not isinstance(pilot.app.screen, AccueilScreen)


async def test_settings_are_reachable_from_accueil(container: DependencyContainer) -> None:
    app = OmegaSuiteApp(container)
    async with app.run_test() as pilot:
        await _reach_accueil(pilot)
        await pilot.press("s")
        await pilot.pause()
        assert not isinstance(pilot.app.screen, AccueilScreen)
