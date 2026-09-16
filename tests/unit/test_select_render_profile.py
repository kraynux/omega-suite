# Copyright (c) 2026 kraynux [kraynux@proton.me] - Licence MIT (voir fichier LICENSE)
"""app/select_render_profile.py - override du profil de rendu (auto par
defaut si jamais defini ou remis a `None`)."""
from __future__ import annotations

from pathlib import Path

from omega_lib.terminal.models import RenderProfile

from omega_suite.app.select_render_profile import (
    RENDER_PROFILE_OVERRIDE_KEY,
    select_render_profile,
)
from omega_suite.infrastructure.storage.json_settings_store import JsonSettingsStore


def test_selecting_a_profile_persists_its_value(tmp_path: Path) -> None:
    store = JsonSettingsStore(tmp_path / "settings.json")
    select_render_profile(settings_store=store, render_profile=RenderProfile.MONO)
    assert store.get(RENDER_PROFILE_OVERRIDE_KEY) == "mono"


def test_selecting_none_clears_the_override(tmp_path: Path) -> None:
    """"Automatique" (None) doit ecrire une chaine vide, jamais laisser
    l'ancienne valeur en place ni la cle absente (le reglage doit rester
    explicitement "aucun override")."""
    store = JsonSettingsStore(tmp_path / "settings.json")
    select_render_profile(settings_store=store, render_profile=RenderProfile.COMPLETE)
    select_render_profile(settings_store=store, render_profile=None)
    assert store.get(RENDER_PROFILE_OVERRIDE_KEY) == ""
