# Copyright (c) 2026 kraynux [kraynux@proton.me] - Licence MIT (voir fichier LICENSE)
"""app/select_navigation_style.py - style "accueil" (grille, defaut) ou
"onglets" (barre persistante, D-014 point 6 revu). Applique au prochain
demarrage - Reglages propose desormais de redemarrer tout de suite
(SettingsScreen._offer_restart), mais la persistance elle-meme reste
testee ici independamment de l'UI."""
from __future__ import annotations

from pathlib import Path

from omega_suite.app.select_navigation_style import (
    DEFAULT_NAVIGATION_STYLE,
    current_navigation_style,
    select_navigation_style,
)
from omega_suite.infrastructure.storage.json_settings_store import JsonSettingsStore


def test_defaults_to_accueil_when_never_set(tmp_path: Path) -> None:
    store = JsonSettingsStore(tmp_path / "settings.json")
    assert DEFAULT_NAVIGATION_STYLE == "accueil"
    assert current_navigation_style(settings_store=store) == "accueil"


def test_select_onglets_then_read_back(tmp_path: Path) -> None:
    store = JsonSettingsStore(tmp_path / "settings.json")
    select_navigation_style(settings_store=store, style="onglets")
    assert current_navigation_style(settings_store=store) == "onglets"


def test_unknown_stored_value_falls_back_to_accueil(tmp_path: Path) -> None:
    """Defense en profondeur (meme garde-fou que SuiteTabBar cote UI) :
    une valeur perimee/corrompue dans settings.json ne doit jamais faire
    planter la suite au demarrage, juste retomber sur le defaut."""
    store = JsonSettingsStore(tmp_path / "settings.json")
    store.set("navigation_style", "un-style-qui-n-existe-plus")
    assert current_navigation_style(settings_store=store) == "accueil"
