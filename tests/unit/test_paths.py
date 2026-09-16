# Copyright (c) 2026 kraynux [kraynux@proton.me] - Licence MIT (voir fichier LICENSE)
"""infrastructure/config/paths.py - seule source de verite sur les chemins
runtime de la suite (D-015 point 8) : `./var` relatif au lancement par
defaut, override via `$OMEGA_SUITE_VAR_DIR`, un sous-dossier DEDIE par
outil (jamais le `var/` par defaut de l'outil lance seul)."""
from __future__ import annotations

from pathlib import Path

import pytest

from omega_suite.infrastructure.config import paths


def test_resolve_var_dir_defaults_to_cwd_relative_var(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    monkeypatch.delenv(paths.ENV_VAR_DIR, raising=False)
    monkeypatch.chdir(tmp_path)
    assert paths.resolve_var_dir() == tmp_path / "var"


def test_resolve_var_dir_honors_env_override(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    override = tmp_path / "elsewhere"
    monkeypatch.setenv(paths.ENV_VAR_DIR, str(override))
    assert paths.resolve_var_dir() == override


def test_tool_var_dir_is_a_dedicated_lowercase_subfolder(tmp_path: Path) -> None:
    assert paths.tool_var_dir(tmp_path, "Scan") == tmp_path / "scan"
    assert paths.tool_var_dir(tmp_path, "track") == tmp_path / "track"


def test_tool_var_dir_differs_per_tool(tmp_path: Path) -> None:
    """Bug transverse redoute (D-015) : deux outils ne doivent jamais
    finir sur le meme sous-dossier, sous peine de melanger leurs bases/
    exports."""
    slugs = ["scan", "check", "deep", "fold", "stress", "track", "fuzz"]
    resolved = {paths.tool_var_dir(tmp_path, slug) for slug in slugs}
    assert len(resolved) == len(slugs)


def test_default_settings_path_lives_directly_under_var_dir(tmp_path: Path) -> None:
    assert paths.default_settings_path(tmp_path) == tmp_path / "settings.json"
