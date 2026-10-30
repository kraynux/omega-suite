# Copyright (c) 2026 kraynux [kraynux@proton.me] - Licence MIT (voir fichier LICENSE)
"""app/clear_all_exports.py - purge globale des exports des 7 outils
(D-014 point 10). La purge n'est PAS uniforme entre les 7 outils : certains
exposent `default_exports_dir`, STRESS expose `export_dir` - ce module doit
gerer les deux sans en privilegier un au detriment de l'autre."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from omega_suite.app.clear_all_exports import clear_all_exports


@dataclass
class _DefaultExportsDirContainer:
    default_exports_dir: Path


@dataclass
class _ExportDirContainer:
    export_dir: Path


class _NeitherContainer:
    pass


def test_clears_containers_exposing_default_exports_dir(tmp_path: Path) -> None:
    exports = tmp_path / "scan" / "exports"
    exports.mkdir(parents=True)
    (exports / "report.json").write_text("{}", encoding="utf-8")

    cleared = clear_all_exports({"scan": _DefaultExportsDirContainer(exports)}, tmp_path / "suite").cleared

    assert cleared == ["scan"]
    assert exports.exists()
    assert list(exports.iterdir()) == []


def test_clears_containers_exposing_export_dir(tmp_path: Path) -> None:
    """STRESS n'utilise pas la meme cle que les 6 autres (verifie au
    code, app.py::_deliver_screenshot_for_active_tool documente deja
    cette meme divergence) - doit etre vide au meme titre."""
    exports = tmp_path / "stress" / "exports"
    exports.mkdir(parents=True)
    (exports / "report.html").write_text("<html></html>", encoding="utf-8")

    cleared = clear_all_exports({"stress": _ExportDirContainer(exports)}, tmp_path / "suite").cleared

    assert cleared == ["stress"]
    assert list(exports.iterdir()) == []


def test_skips_containers_with_neither_attribute(tmp_path: Path) -> None:
    cleared = clear_all_exports({"unknown": _NeitherContainer()}, tmp_path / "suite").cleared
    assert cleared == []


def test_recreates_the_directory_even_if_it_did_not_exist(tmp_path: Path) -> None:
    exports = tmp_path / "fold" / "exports"
    cleared = clear_all_exports({"fold": _DefaultExportsDirContainer(exports)}, tmp_path / "suite").cleared
    assert cleared == ["fold"]
    assert exports.is_dir()


def test_clears_multiple_tools_independently(tmp_path: Path) -> None:
    scan_exports = tmp_path / "scan" / "exports"
    stress_exports = tmp_path / "stress" / "exports"
    scan_exports.mkdir(parents=True)
    stress_exports.mkdir(parents=True)
    (scan_exports / "a.json").write_text("{}", encoding="utf-8")
    (stress_exports / "b.html").write_text("<html></html>", encoding="utf-8")

    cleared = clear_all_exports(
        {
            "scan": _DefaultExportsDirContainer(scan_exports),
            "stress": _ExportDirContainer(stress_exports),
        },
        tmp_path / "suite",
    ).cleared

    assert set(cleared) == {"scan", "stress"}
    assert list(scan_exports.iterdir()) == []
    assert list(stress_exports.iterdir()) == []


class _Settings:
    def __init__(self, values: dict[str, str]) -> None:
        self._values = values

    def get(self, key: str, default: str = "") -> str:
        return self._values.get(key, default)


@dataclass
class _ConfiguredContainer:
    default_exports_dir: Path
    settings_store: _Settings


def test_clears_folder_configured_in_tool_settings_not_default(tmp_path: Path) -> None:
    """Correctif 2026-10-27 : le dossier choisi dans les reglages de l'outil est vide, plus
    toujours son dossier par defaut."""
    default = tmp_path / "check" / "exports"
    default.mkdir(parents=True)
    (default / "garder.html").write_text("x")
    custom = tmp_path / "ailleurs"
    custom.mkdir()
    (custom / "vieux.html").write_text("x")
    container = _ConfiguredContainer(default, _Settings({"exports_dir_override": str(custom)}))

    result = clear_all_exports({"check": container}, tmp_path / "suite")

    assert result.cleared == ["check"] and result.problems == []
    assert list(custom.iterdir()) == []
    assert (default / "garder.html").exists()


def test_system_folder_refused_and_reported(tmp_path: Path) -> None:
    container = _ConfiguredContainer(tmp_path / "x", _Settings({"exports_dir_override": "/etc"}))
    result = clear_all_exports({"check": container}, tmp_path / "suite")
    assert result.cleared == []
    assert "dossier refusé" in result.problems[0]


def test_suite_root_refused(tmp_path: Path) -> None:
    suite_root = tmp_path / "suite"
    suite_root.mkdir()
    result = clear_all_exports({"scan": _DefaultExportsDirContainer(suite_root)}, suite_root)
    assert result.cleared == [] and "omega-suite" in result.problems[0]


def test_symlink_removed_without_touching_target(tmp_path: Path) -> None:
    exports = tmp_path / "scan" / "exports"
    exports.mkdir(parents=True)
    outside = tmp_path / "garder.txt"
    outside.write_text("z")
    (exports / "lien").symlink_to(outside)
    clear_all_exports({"scan": _DefaultExportsDirContainer(exports)}, tmp_path / "suite")
    assert list(exports.iterdir()) == [] and outside.exists()
