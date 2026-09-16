# Copyright (c) 2026 kraynux [kraynux@proton.me] - Licence MIT (voir fichier LICENSE)
"""Confirmation avant fermeture d'omega-suite - copie du patron identique
dans les 7 outils (D-007/D-008), texte adapte a la suite."""
from __future__ import annotations

from textual.app import ComposeResult
from textual.containers import Center, Container, Horizontal, Middle, Vertical
from textual.screen import Screen
from textual.widgets import Button, Static


class QuitConfirmScreen(Screen[bool]):
    def compose(self) -> ComposeResult:
        with Middle(), Center(), Vertical(classes="omega-confirm-box"):
            yield Static("QUITTER OMEGA-SUITE ?", classes="omega-confirm-title")
            with Horizontal(classes="omega-confirm-buttons"):
                with Container(classes="omega-btn-frame"):
                    yield Button("Oui, quitter", id="confirm", variant="error")
                with Container(classes="omega-btn-frame"):
                    yield Button("Non, continuer", id="cancel", variant="primary")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.dismiss(event.button.id == "confirm")
