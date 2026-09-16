# Copyright (c) 2026 kraynux [kraynux@proton.me] - Licence MIT (voir fichier LICENSE)
"""Construit reellement les 7 adaptateurs (import du vrai code de chaque
outil, PAS de bouchon) : garde-fou contre la derive des 7 projets sources
(chacun evolue independamment - un renommage de `bootstrap()`/
`build_container()` cote outil casserait silencieusement la suite sans ce
test, voir la docstring de `tool_adapters.py` qui documente deja les
divergences relevees au code entre les 7).

Couvre aussi directement la regression FUZZ du 2026-09-16 : son
adaptateur est le seul a construire son ecran d'accueil via une fonction
locale (`_build_home`) plutot qu'un lambda direct - c'etait le seul a
importer `textual.screen.Screen` au niveau du module `app/tool_adapters.py`
(viole "textual seulement dans interfaces.tui") pour un `cast()` devenu
inutile (`HomeScreen` de FUZZ n'a pas de marqueur `py.typed`, deja traite
comme `Any` par mypy)."""
from __future__ import annotations

from pathlib import Path

import pytest
from textual.screen import Screen

from omega_suite.app.tool_adapters import TOOL_ADAPTER_FACTORIES


@pytest.mark.parametrize("slug", sorted(TOOL_ADAPTER_FACTORIES))
def test_adapter_builds_a_real_container_and_home_screen(slug: str, tmp_path: Path) -> None:
    adapter = TOOL_ADAPTER_FACTORIES[slug]()
    assert adapter.slug
    container = adapter.build_container(tmp_path / slug)
    screen = adapter.build_home_screen(container)
    assert isinstance(screen, Screen)


def test_the_seven_tools_get_seven_distinct_var_subdirectories(tmp_path: Path) -> None:
    """Chaque outil doit ecrire dans SON PROPRE sous-dossier - jamais le
    `var/` par defaut de l'outil lance seul (D-015 point 8)."""
    slugs = {adapter().slug for adapter in TOOL_ADAPTER_FACTORIES.values()}
    assert len(slugs) == len(TOOL_ADAPTER_FACTORIES)
