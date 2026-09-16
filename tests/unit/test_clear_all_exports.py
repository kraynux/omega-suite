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

    cleared = clear_all_exports({"scan": _DefaultExportsDirContainer(exports)})

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

    cleared = clear_all_exports({"stress": _ExportDirContainer(exports)})

    assert cleared == ["stress"]
    assert list(exports.iterdir()) == []


def test_skips_containers_with_neither_attribute(tmp_path: Path) -> None:
    cleared = clear_all_exports({"unknown": _NeitherContainer()})
    assert cleared == []


def test_recreates_the_directory_even_if_it_did_not_exist(tmp_path: Path) -> None:
    exports = tmp_path / "fold" / "exports"
    cleared = clear_all_exports({"fold": _DefaultExportsDirContainer(exports)})
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
        }
    )

    assert set(cleared) == {"scan", "stress"}
    assert list(scan_exports.iterdir()) == []
    assert list(stress_exports.iterdir()) == []
