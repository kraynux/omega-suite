# Copyright (c) 2026 kraynux [kraynux@proton.me] - Licence MIT (voir fichier LICENSE)
"""Ecran de demarrage unique de la suite (D-014 point 2 : un seul splash,
plus les 7 splash individuels des outils, jamais invoques en mode suite).
Copie du patron identique dans les 7 outils (D-007/D-008)."""
from __future__ import annotations

from textual import events
from textual.app import ComposeResult
from textual.containers import Center, Middle
from textual.screen import Screen
from textual.widgets import Static

from omega_suite.interfaces.tui.widgets.splash_hero import SplashHero


class SplashScreen(Screen[None]):
    def compose(self) -> ComposeResult:
        with Middle(classes="omega-splash-middle"):
            with Center():
                yield SplashHero()
            with Center():
                yield Static("Appuyez sur une touche pour continuer...", classes="omega-splash-prompt")

    def on_key(self, event: events.Key) -> None:
        event.stop()
        self.dismiss()

    def on_click(self, event: events.Click) -> None:
        event.stop()
        self.dismiss()
