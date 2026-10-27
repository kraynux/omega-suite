# Copyright (c) 2026 kraynux [kraynux@proton.me] - Licence MIT (voir fichier LICENSE)
"""Regression d'un bug reel constate le 2026-10-16 ("omega-fuzz gele
silencieusement, sans message d'erreur", apres correction d'un premier
bug distinct - vendoring casse de `omega_fuzz.domain.tests`, voir
build-release.sh) : `Tabs` peut re-emettre un evenement d'activation
fantome pour le MEME slug qu'une vraie demande deja en vol (meme cause
documentee dans `request_tool_switch` pour `_pending_switch_target`,
mais ici pour `_patch_workers`) - sans deduplication, deux demandes
concurrentes pour le meme outil lancaient chacune leur propre worker
`thread=True`, important/monkey-patchant les MEMES classes d'ecran EN
PARALLELE (`patch_tool_screens` ne prend aucun verrou) : deux threads
qui importent simultanement un arbre de modules qui se chevauche est une
classe connue, bien que rare, de blocage de l'import CPython - silencieux,
sans exception, sans rapport avec le terminal utilise en apparence (plus
probable sur un terminal a faible latence d'evenements, qui rapproche les
deux demandes dans le temps)."""
from __future__ import annotations

import asyncio
from unittest.mock import patch

from omega_suite.app.dependency_container import DependencyContainer
from omega_suite.interfaces.tui.app import OmegaSuiteApp
from omega_suite.interfaces.tui.screens.terminal_warning import TerminalWarningScreen


async def _reach_accueil(pilot) -> None:
    await pilot.press("x")
    await pilot.pause()
    if isinstance(pilot.app.screen, TerminalWarningScreen):
        await pilot.click("#continue")
        await pilot.pause()


async def test_concurrent_requests_for_the_same_never_visited_tool_patch_only_once(
    onglets_container: DependencyContainer,
) -> None:
    app = OmegaSuiteApp(onglets_container)
    async with app.run_test() as pilot:
        await _reach_accueil(pilot)

        call_count = 0
        from omega_suite.interfaces.tui.app import patch_tool_screens as _real_patch_tool_screens

        def _counting_patch(**kwargs: object) -> None:
            nonlocal call_count
            call_count += 1
            _real_patch_tool_screens(**kwargs)  # type: ignore[arg-type]

        with patch("omega_suite.interfaces.tui.app.patch_tool_screens", side_effect=_counting_patch):
            # Deux demandes concurrentes pour LE MEME outil jamais visite,
            # exactement le scenario "evenement fantome + vrai clic" -
            # avant le correctif, chacune lancait son propre worker.
            await asyncio.gather(
                pilot.app.request_tool_switch("fuzz"),
                pilot.app.request_tool_switch("fuzz"),
            )
            await pilot.pause()

        assert call_count == 1, (
            f"patch_tool_screens() appele {call_count} fois pour 2 demandes concurrentes "
            "du meme outil - devrait etre dedupe a 1 seul appel"
        )
        assert pilot.app.current_mode == "fuzz"
        assert "fuzz" not in pilot.app._patch_workers
