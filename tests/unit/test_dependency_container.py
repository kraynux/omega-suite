# Copyright (c) 2026 kraynux [kraynux@proton.me] - Licence MIT (voir fichier LICENSE)
"""app/dependency_container.py - construction paresseuse a DEUX niveaux
(bug reel constate et corrige - "5 secondes au demarrage", voir docstring
du module source) : ni l'adaptateur d'un outil (son import Python) ni son
conteneur (base SQLite, sondes reseau) ne doivent jamais etre payes avant
le premier acces reel a CET outil precis."""
from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest

from omega_suite.app.dependency_container import DependencyContainer
from omega_suite.app.tool_adapters import ToolAdapter
from omega_suite.infrastructure.storage.json_settings_store import JsonSettingsStore


class _FakeAdapterFactory:
    """Compte ses propres appels - le test doit pouvoir affirmer "jamais
    appelee" aussi facilement que "appelee exactement une fois"."""

    def __init__(self, slug: str) -> None:
        self.slug = slug
        self.call_count = 0
        self.built_containers: list[Path] = []

    def __call__(self) -> ToolAdapter:
        self.call_count += 1
        return ToolAdapter(
            slug=self.slug,
            screens_package=f"fake_{self.slug}.interfaces.tui.screens",
            build_container=self._build_container,
            build_home_screen=lambda container: container,
        )

    def _build_container(self, var_dir: Path) -> Any:
        self.built_containers.append(var_dir)
        return object()


@pytest.fixture
def container(tmp_path: Path) -> tuple[DependencyContainer, _FakeAdapterFactory, _FakeAdapterFactory]:
    scan_factory = _FakeAdapterFactory("scan")
    fold_factory = _FakeAdapterFactory("fold")
    dep_container = DependencyContainer(
        adapter_factories={"scan": scan_factory, "fold": fold_factory},
        settings_store=JsonSettingsStore(tmp_path / "settings.json"),
        var_dir=tmp_path,
    )
    return dep_container, scan_factory, fold_factory


def test_adapter_factories_are_never_called_at_construction(
    container: tuple[DependencyContainer, _FakeAdapterFactory, _FakeAdapterFactory],
) -> None:
    _dep_container, scan_factory, fold_factory = container
    assert scan_factory.call_count == 0
    assert fold_factory.call_count == 0


def test_get_adapter_calls_the_factory_exactly_once(
    container: tuple[DependencyContainer, _FakeAdapterFactory, _FakeAdapterFactory],
) -> None:
    dep_container, scan_factory, fold_factory = container
    dep_container.get_adapter("scan")
    dep_container.get_adapter("scan")
    assert scan_factory.call_count == 1
    assert fold_factory.call_count == 0


def test_get_adapter_caches_the_same_instance(
    container: tuple[DependencyContainer, _FakeAdapterFactory, _FakeAdapterFactory],
) -> None:
    dep_container, _scan_factory, _fold_factory = container
    assert dep_container.get_adapter("scan") is dep_container.get_adapter("scan")


def test_get_tool_container_does_not_touch_untouched_tools(
    container: tuple[DependencyContainer, _FakeAdapterFactory, _FakeAdapterFactory],
) -> None:
    dep_container, scan_factory, fold_factory = container
    dep_container.get_tool_container("scan")
    assert scan_factory.call_count == 1
    assert len(scan_factory.built_containers) == 1
    assert fold_factory.call_count == 0


def test_get_tool_container_caches_and_uses_a_dedicated_subdir(
    container: tuple[DependencyContainer, _FakeAdapterFactory, _FakeAdapterFactory],
) -> None:
    dep_container, scan_factory, _fold_factory = container
    first = dep_container.get_tool_container("scan")
    second = dep_container.get_tool_container("scan")
    assert first is second
    assert len(scan_factory.built_containers) == 1
    assert scan_factory.built_containers[0].name == "scan"


def test_tool_containers_property_never_forces_construction(
    container: tuple[DependencyContainer, _FakeAdapterFactory, _FakeAdapterFactory],
) -> None:
    dep_container, scan_factory, fold_factory = container
    assert dep_container.tool_containers == {}
    dep_container.get_tool_container("scan")
    assert set(dep_container.tool_containers) == {"scan"}
    assert scan_factory.call_count == 1
    assert fold_factory.call_count == 0


def test_get_all_tool_containers_forces_every_tool(
    container: tuple[DependencyContainer, _FakeAdapterFactory, _FakeAdapterFactory],
) -> None:
    """Reserve aux actions qui doivent agir sur TOUS les outils meme non
    visites (ex. "Vider tous les exports") - le seul endroit ou payer ce
    cout d'un coup est justifie."""
    dep_container, scan_factory, fold_factory = container
    all_containers = dep_container.get_all_tool_containers()
    assert set(all_containers) == {"scan", "fold"}
    assert scan_factory.call_count == 1
    assert fold_factory.call_count == 1
