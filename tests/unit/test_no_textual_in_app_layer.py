# Copyright (c) 2026 kraynux [kraynux@proton.me] - Licence MIT (voir fichier LICENSE)
"""Verifie que `app/` reste independant de Textual AU RUNTIME - complementaire
d'import-linter (verifie tous les chemins possibles statiquement, meme
contrat dans pyproject.toml), pas un remplacement : un vrai bug reel a ete
trouve et corrige (2026-09-16) via ce contrat - `app/tool_adapters.py`
importait `from textual.screen import Screen` au niveau du module pour un
`cast()` dans `_fuzz_adapter()`, en violation de "textual seulement dans
interfaces.tui" (pyproject.toml::[[tool.importlinter.contracts]]) - corrige
en abandonnant le `cast()` (retour `Any`, deja compatible avec
`Callable[[Any], Screen]` cote appelant). Ce test garde ce module (et le
reste du package `app/`) honnete au niveau runtime, pas seulement statique.

Patron identique a `omega_track/tests/unit/test_imports.py` : diff
avant/apres l'import, jamais une presence absolue dans `sys.modules`
(un AUTRE test de la meme suite peut deja avoir charge `textual` avant
que celui-ci ne s'execute - `sys.modules` est un etat global au process)."""
from __future__ import annotations

import importlib
import sys

_FORBIDDEN = ("textual",)


def _newly_forbidden_modules(module_name: str, forbidden_prefixes: tuple[str, ...]) -> list[str]:
    for name in list(sys.modules):
        if name == module_name or name.startswith(module_name + "."):
            del sys.modules[name]
    before = set(sys.modules)
    importlib.import_module(module_name)
    after = set(sys.modules)
    newly_loaded = after - before
    return [
        name
        for name in newly_loaded
        if any(name == prefix or name.startswith(prefix + ".") for prefix in forbidden_prefixes)
    ]


def test_app_package_imports_without_textual() -> None:
    assert _newly_forbidden_modules("omega_suite.app", _FORBIDDEN) == []


def test_tool_adapters_module_imports_without_textual() -> None:
    """Regression directe du bug 2026-09-16 (voir docstring du module) -
    `tool_adapters.py` specifiquement, pas seulement le package `app/`
    dans son ensemble."""
    assert _newly_forbidden_modules("omega_suite.app.tool_adapters", _FORBIDDEN) == []


def test_dependency_container_module_imports_without_textual() -> None:
    assert _newly_forbidden_modules("omega_suite.app.dependency_container", _FORBIDDEN) == []


def test_cli_package_imports_without_textual() -> None:
    assert _newly_forbidden_modules("omega_suite.interfaces.cli", _FORBIDDEN) == []
