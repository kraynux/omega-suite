# Copyright (c) 2026 kraynux [kraynux@proton.me] - Licence MIT (voir fichier LICENSE)
"""Choisir et persister le theme actif de la suite - un seul theme
partage par les 7 onglets + Accueil (D-014 : un seul `App.theme`,
un seul process Textual)."""
from __future__ import annotations

from omega_lib.theme.policies import TUI_THEMES

from omega_suite.ports.settings_store import SettingsStore

THEME_KEY = "theme"


class UnknownThemeError(ValueError):
    pass


def select_theme(*, settings_store: SettingsStore, theme_name: str) -> None:
    if theme_name not in TUI_THEMES:
        raise UnknownThemeError(theme_name)
    settings_store.set(THEME_KEY, theme_name)
