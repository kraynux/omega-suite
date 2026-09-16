# Copyright (c) 2026 kraynux [kraynux@proton.me] - Licence MIT (voir fichier LICENSE)
"""Conteneur de composition de la suite : assemble les 7 conteneurs
d'outils (chacun construit et valide independamment par son propre
projet) plutot que de reimplementer une quelconque logique metier -
omega-suite reste une facade additionnelle (OMEGA-SUITE_ARBORESCENCE.md).

Construction PARESSEUSE a DEUX niveaux (bug reel constate - "5 secondes
au demarrage") :
1. `ToolAdapter` lui-meme (`tool_adapters.py::_scan_adapter()` etc.) -
   son SEUL fait d'etre appele importe `interfaces.tui.screens.home` de
   l'outil, qui importe LUI-MEME tous ses ecrans freres (patron constate
   dans les 7 `home.py`) et donc leurs dependances lourdes (httpx,
   cryptography, aiohttp, beautifulsoup4, lxml, dnspython, maxminddb,
   pyyaml, psutil) - appeler les 7 factories EAGERLY, avant meme que
   l'utilisateur ait choisi un outil, est le premier cout mesure.
2. `adapter.build_container()` - ouvre une connexion SQLite et instancie
   des sondes reseau pour CET outil - second cout mesure, plus petit
   mais reel.
Les deux ne sont desormais payes qu'au premier `switch_mode` reel vers
CET outil precis (`get_adapter()`/`get_tool_container()`), jamais avant,
jamais pour un outil que l'utilisateur ne visite pas cette session."""
from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING, Any

from omega_suite.infrastructure.config import paths
from omega_suite.ports.settings_store import SettingsStore

if TYPE_CHECKING:
    from omega_suite.app.tool_adapters import ToolAdapter


@dataclass(frozen=True)
class DependencyContainer:
    adapter_factories: dict[str, Callable[[], ToolAdapter]]
    settings_store: SettingsStore
    var_dir: Path
    _adapter_cache: dict[str, ToolAdapter] = field(default_factory=dict, repr=False)
    _tool_container_cache: dict[str, Any] = field(default_factory=dict, repr=False)

    def get_adapter(self, slug: str) -> ToolAdapter:
        """Construit (une seule fois, mise en cache) le `ToolAdapter` de
        l'outil `slug` - c'est CET appel qui declenche l'import de
        l'outil, jamais fait avant que ce ne soit necessaire."""
        if slug not in self._adapter_cache:
            self._adapter_cache[slug] = self.adapter_factories[slug]()
        return self._adapter_cache[slug]

    def get_tool_container(self, slug: str) -> Any:
        """Construit (une seule fois, mise en cache) le conteneur de
        l'outil `slug`, ou renvoie celui deja construit."""
        if slug not in self._tool_container_cache:
            adapter = self.get_adapter(slug)
            self._tool_container_cache[slug] = adapter.build_container(
                paths.tool_var_dir(self.var_dir, slug)
            )
        return self._tool_container_cache[slug]

    def get_all_tool_containers(self) -> dict[str, Any]:
        """Force la construction des 7 adaptateurs+conteneurs (jamais
        fait implicitement) - reserve aux actions qui doivent agir sur
        TOUS les outils meme non visites cette session (ex. "Vider tous
        les exports", Reglages de la suite)."""
        for slug in self.adapter_factories:
            self.get_tool_container(slug)
        return dict(self._tool_container_cache)

    @property
    def tool_containers(self) -> dict[str, Any]:
        """Vue en lecture seule des SEULS conteneurs deja construits
        (ne force jamais une construction) - utilisee pour tout ce qui
        ne doit agir que sur l'outil actif (capture d'ecran)."""
        return dict(self._tool_container_cache)
