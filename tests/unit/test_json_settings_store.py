# Copyright (c) 2026 kraynux [kraynux@proton.me] - Licence MIT (voir fichier LICENSE)
"""infrastructure/storage/json_settings_store.py - implementation JSON du
port SettingsStore, seul etat propre a omega-suite (theme, profil de
rendu, style de navigation)."""
from __future__ import annotations

import json
from pathlib import Path

from omega_suite.infrastructure.storage.json_settings_store import JsonSettingsStore


def test_get_returns_default_when_file_missing(tmp_path: Path) -> None:
    store = JsonSettingsStore(tmp_path / "settings.json")
    assert store.get("theme") is None
    assert store.get("theme", "omega-base") == "omega-base"


def test_set_then_get_round_trips(tmp_path: Path) -> None:
    store = JsonSettingsStore(tmp_path / "settings.json")
    store.set("theme", "omega-dark")
    assert store.get("theme") == "omega-dark"


def test_set_creates_parent_directories(tmp_path: Path) -> None:
    path = tmp_path / "nested" / "dir" / "settings.json"
    store = JsonSettingsStore(path)
    store.set("theme", "omega-dark")
    assert path.exists()


def test_set_persists_across_new_instances(tmp_path: Path) -> None:
    path = tmp_path / "settings.json"
    JsonSettingsStore(path).set("navigation_style", "onglets")
    reloaded = JsonSettingsStore(path)
    assert reloaded.get("navigation_style") == "onglets"


def test_set_preserves_other_keys(tmp_path: Path) -> None:
    """Bug facile a introduire (ecraser tout le fichier au lieu de
    fusionner) : `set()` doit relire l'existant avant de reecrire."""
    path = tmp_path / "settings.json"
    store = JsonSettingsStore(path)
    store.set("theme", "omega-dark")
    store.set("navigation_style", "onglets")
    assert store.get("theme") == "omega-dark"
    assert store.get("navigation_style") == "onglets"


def test_all_returns_a_copy(tmp_path: Path) -> None:
    store = JsonSettingsStore(tmp_path / "settings.json")
    store.set("theme", "omega-dark")
    snapshot = store.all()
    snapshot["theme"] = "mutated"
    assert store.get("theme") == "omega-dark"


def test_written_file_is_valid_json(tmp_path: Path) -> None:
    path = tmp_path / "settings.json"
    JsonSettingsStore(path).set("theme", "omega-dark")
    assert json.loads(path.read_text(encoding="utf-8")) == {"theme": "omega-dark"}
