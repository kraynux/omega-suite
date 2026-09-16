# Copyright (c) 2026 kraynux [kraynux@proton.me] - Licence MIT (voir fichier LICENSE)
"""app/select_theme.py - un seul theme partage par les 7 onglets + Accueil
(D-014) ; rejette tout nom de theme inconnu plutot que de le persister
silencieusement."""
from __future__ import annotations

from pathlib import Path

import pytest
from omega_lib.theme.policies import TUI_THEMES

from omega_suite.app.select_theme import THEME_KEY, UnknownThemeError, select_theme
from omega_suite.infrastructure.storage.json_settings_store import JsonSettingsStore


def test_selecting_a_known_theme_persists_it(tmp_path: Path) -> None:
    store = JsonSettingsStore(tmp_path / "settings.json")
    theme_name = next(iter(TUI_THEMES))
    select_theme(settings_store=store, theme_name=theme_name)
    assert store.get(THEME_KEY) == theme_name


def test_selecting_an_unknown_theme_raises_and_does_not_persist(tmp_path: Path) -> None:
    store = JsonSettingsStore(tmp_path / "settings.json")
    with pytest.raises(UnknownThemeError):
        select_theme(settings_store=store, theme_name="un-theme-qui-n-existe-pas")
    assert store.get(THEME_KEY) is None
