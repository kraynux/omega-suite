# Copyright (c) 2026 kraynux [kraynux@proton.me] - Licence MIT (voir fichier LICENSE)
"""Racine de composition de la suite : le reglage propre a la suite
(theme/profil de rendu, D-014) et le var_dir dedie (D-015 point 8).
N'appelle AUCUNE des 7 factories d'adaptateur ici (bug reel constate -
"5 secondes au demarrage") : appeler `_scan_adapter()` etc. importe deja
`interfaces.tui.screens.home` de l'outil, qui importe lui-meme tous ses
ecrans freres et leurs dependances lourdes - les 7 factories ne sont
appelees que paresseusement, voir `DependencyContainer.get_adapter()`."""
from __future__ import annotations

from pathlib import Path

from omega_suite.app.dependency_container import DependencyContainer
from omega_suite.app.tool_adapters import TOOL_ADAPTER_FACTORIES
from omega_suite.infrastructure.config import paths
from omega_suite.infrastructure.storage.json_settings_store import JsonSettingsStore


def bootstrap(*, var_dir: Path | None = None) -> DependencyContainer:
    base = var_dir if var_dir is not None else paths.resolve_var_dir()
    base.mkdir(parents=True, exist_ok=True)

    settings_store = JsonSettingsStore(paths.default_settings_path(base))

    return DependencyContainer(
        adapter_factories=dict(TOOL_ADAPTER_FACTORIES),
        settings_store=settings_store,
        var_dir=base,
    )
