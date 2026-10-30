# Copyright (c) 2026 kraynux [kraynux@proton.me] - Licence MIT (voir fichier LICENSE)
"""Ecran Accueil de la suite (D-014 points 6/7) : point d'entree unique
apres le splash, racine de la barre d'onglets. Grille 2x5, 10 boutons
(7 outils + Reglages + Aide + Quitter), ordre fixe convenu."""
from __future__ import annotations

from typing import ClassVar

from textual.app import ComposeResult
from textual.binding import Binding, BindingType
from textual.containers import Center, Container, Grid, Vertical
from textual.screen import Screen
from textual.widgets import Button, Footer, Header

from omega_suite.interfaces.tui.widgets.home_wordmark import HomeWordmark
from omega_suite.shared.i18n import _

_GRID_ITEMS: tuple[tuple[str, str], ...] = (
    ("scan", "Omega-SCAN"),
    ("fuzz", "Omega-FUZZ"),
    ("fold", "Omega-FOLD"),
    ("stress", "Omega-STRESS"),
    ("check", "Omega-CHECK"),
    ("settings", _("RÉGLAGES")),
    ("deep", "Omega-DEEP"),
    ("help", _("AIDE")),
    ("track", "Omega-TRACK"),
    ("quit", _("QUITTER")),
)

_TOOL_IDS = frozenset({item_id for item_id, _ignored in _GRID_ITEMS} - {"settings", "help", "quit"})


class AccueilScreen(Screen[None]):
    """Racine de navigation de la suite - n'herite pas de OmegaScreen
    (meme convention que le HomeScreen de chaque outil) : `echap` ici
    demande confirmation de sortie, rien "en dessous" de cet ecran."""

    BINDINGS: ClassVar[list[BindingType]] = [
        Binding("escape", "back", _("Retour"), show=True),
        Binding("up", "focus_previous_item", _("Monter"), show=False),
        Binding("down", "focus_next_item", _("Descendre"), show=False),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        with Vertical(classes="omega-home-root"):
            with Center():
                yield HomeWordmark()
            with Center():
                with Grid(classes="omega-accueil-grid") as grid:
                    for item_id, label in _GRID_ITEMS:
                        with Container(classes="omega-btn-frame"):
                            yield Button(label, id=item_id)
                grid.border_title = _("ACCUEIL")
        yield Footer()

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        item_id = event.button.id
        if item_id is None:
            return
        if item_id == "quit":
            await self.app.action_quit()
            return
        if item_id == "settings":
            self.app.action_reglages()  # type: ignore[attr-defined]
            return
        if item_id == "help":
            self.app.action_help()  # type: ignore[attr-defined]
            return
        if item_id in _TOOL_IDS:
            # await (pas un switch_mode() direct, meme bug reel que la
            # barre d'onglets - "ca fige le terminal") : voir
            # OmegaSuiteApp.request_tool_switch(), qui deporte l'import
            # potentiellement lent d'un outil jamais visite dans un
            # thread avant de changer de mode.
            await self.app.request_tool_switch(item_id)  # type: ignore[attr-defined]

    async def action_back(self) -> None:
        await self.app.action_quit()

    def action_focus_previous_item(self) -> None:
        self.focus_previous()

    def action_focus_next_item(self) -> None:
        self.focus_next()
