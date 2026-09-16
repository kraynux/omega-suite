# Copyright (c) 2026 kraynux [kraynux@proton.me] - Licence MIT (voir fichier LICENSE)
from __future__ import annotations

from pathlib import Path

import pytest

from omega_suite.app.bootstrap import bootstrap
from omega_suite.app.dependency_container import DependencyContainer
from omega_suite.app.select_navigation_style import select_navigation_style


@pytest.fixture
def container(tmp_path: Path) -> DependencyContainer:
    return bootstrap(var_dir=tmp_path)


@pytest.fixture
def onglets_container(tmp_path: Path) -> DependencyContainer:
    """Meme conteneur, mais avec le style de navigation "onglets" deja
    ecrit dans settings.json AVANT le bootstrap - `OmegaSuiteApp` ne lit
    ce reglage qu'a la construction (`self._onglets`, non rechargeable a
    chaud, D-014)."""
    first_pass = bootstrap(var_dir=tmp_path)
    select_navigation_style(settings_store=first_pass.settings_store, style="onglets")
    return bootstrap(var_dir=tmp_path)
