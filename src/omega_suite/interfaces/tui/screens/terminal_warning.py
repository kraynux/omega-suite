# Copyright (c) 2026 kraynux [kraynux@proton.me] - Licence MIT (voir fichier LICENSE)
"""Avertissement terminal trop petit/degrade - copie du patron identique
dans les 7 outils (D-007/D-008), une seule fois au niveau suite (D-014
point 6 : plus de 7 verifications redondantes)."""
from __future__ import annotations

from textual.app import ComposeResult
from textual.containers import Center, Container, Horizontal, Middle
from textual.screen import Screen
from textual.widgets import Button, Static


class TerminalWarningScreen(Screen[None]):
    def __init__(self, *, message: str) -> None:
        super().__init__()
        self._message = message

    def compose(self) -> ComposeResult:
        with Middle(), Center():
            yield Static("TERMINAL LIMITE", classes="omega-title")
            yield Static(self._message, classes="omega-subtitle")
            with Horizontal(classes="omega-actions"), Container(classes="omega-btn-frame"):
                yield Button("Continuer quand meme", id="continue", variant="primary")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "continue":
            self.dismiss()
