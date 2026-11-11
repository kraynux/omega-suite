# Copyright (c) 2026 kraynux [kraynux@proton.me] - Licence MIT (voir fichier LICENSE)
"""Contact et support dans la suite (omega-lib, D-016, 2026-11-09) : l'aide de la suite (Accueil)
declare « omega-suite » ; l'aide d'un onglet ouvre la MEME (une seule
declaration dans la suite, decision 2026-11-09). Aucun envoi : on n'appuie jamais sur « Envoyer »."""
from __future__ import annotations

from pathlib import Path

from textual.widgets import Button

from omega_suite.app.dependency_container import DependencyContainer
from omega_suite.interfaces.tui.app import OmegaSuiteApp
from omega_suite.interfaces.tui.screens.accueil import AccueilScreen
from omega_suite.interfaces.tui.screens.terminal_warning import TerminalWarningScreen


async def _reach_accueil(pilot) -> None:
    await pilot.press("x")
    await pilot.pause()
    if isinstance(pilot.app.screen, TerminalWarningScreen):
        await pilot.click("#continue")
        await pilot.pause()
    assert isinstance(pilot.app.screen, AccueilScreen)


def test_suite_container_declares_omega_suite(container: DependencyContainer, tmp_path: Path) -> None:
    services = container.contact_support
    assert services is not None and services.software == "omega-suite"
    assert services.store.path == tmp_path / "declaration.json"  # type: ignore[attr-defined]


async def test_suite_help_and_tool_help_share_the_suite_declaration(
    onglets_container: DependencyContainer, tmp_path: Path,
) -> None:
    app = OmegaSuiteApp(onglets_container)
    async with app.run_test(size=(140, 50)) as pilot:
        await _reach_accueil(pilot)
        app.action_help()
        await pilot.pause()
        app.screen.query_one("#contact-support", Button).press()
        await pilot.pause()
        assert type(app.screen).__name__ == "ContactSupportScreen"
        assert app.screen._kit.services.software == "omega-suite"
        await pilot.press("escape")
        await pilot.pause()
        await pilot.press("escape")
        await pilot.pause()

        await pilot.click("Tab#scan")
        await pilot.pause()
        assert app.current_mode == "scan"
        app.action_help()
        await pilot.pause()
        app.screen.query_one("#contact-support", Button).press()
        await pilot.pause()
        services = app.screen._kit.services
        # Une seule declaration dans la suite (decision 2026-11-09), meme depuis un onglet.
        assert services.software == "omega-suite"
        assert services.store.path == tmp_path / "declaration.json"
