# Copyright (c) 2026 kraynux [kraynux@proton.me] - Licence MIT (voir fichier LICENSE)
"""Registre des 7 outils integres a la suite : chacun expose un point
d'entree `bootstrap()`/`build_container()` legerement different (verifie
au code, pas suppose) - SCAN et STRESS renvoient un wrapper `Application`
(`.container`), STRESS n'accepte pas `console_logging`, FUZZ n'a pas de
`app/bootstrap.py` du tout (son point d'entree est
`app/composition_root.py::build_container`) et son `HomeScreen` exige en
plus un `scan_runtime_factory`. Ce module absorbe ces differences reelles
en un seul endroit - le reste de la suite (app.py, bootstrap.py) ne
manipule que `ToolAdapter`, jamais les particularites de chaque outil."""
from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    # Sous garde (jamais un import reel a l'execution, `from __future__
    # import annotations` stringifie deja toutes les annotations
    # ci-dessous) : le contrat import-linter "textual seulement dans
    # interfaces.tui" interdit tout import - meme de type - de `textual`
    # depuis `app/`.
    from textual.screen import Screen


@dataclass(frozen=True)
class ToolAdapter:
    slug: str
    """Identifiant court utilise pour le nom de mode Textual, le prefixe
    de scope CSS (screen_patching.py) et le sous-dossier `var/<slug>/`."""
    screens_package: str
    """Chemin d'import du package `interfaces.tui.screens` de l'outil."""
    build_container: Callable[[Path], Any]
    """Construit le conteneur de l'outil pour le `var_dir` donne (deja
    dedie a cet outil, jamais partage) - toujours `console_logging=False`
    (memes raisons que chaque TUI standalone : Textual possede l'ecran)."""
    build_home_screen: Callable[[Any], Screen]
    """Construit l'ecran d'accueil de l'outil a partir de son conteneur."""


def _scan_adapter() -> ToolAdapter:
    from omega_scan.app.bootstrap import bootstrap
    from omega_scan.interfaces.tui.screens.home import HomeScreen

    return ToolAdapter(
        slug="Scan",
        screens_package="omega_scan.interfaces.tui.screens",
        build_container=lambda var_dir: bootstrap(var_dir=var_dir, console_logging=False).container,
        build_home_screen=lambda container: HomeScreen(container=container),
    )


def _check_adapter() -> ToolAdapter:
    from omega_check.app.bootstrap import bootstrap
    from omega_check.interfaces.tui.screens.home import HomeScreen

    return ToolAdapter(
        slug="Check",
        screens_package="omega_check.interfaces.tui.screens",
        build_container=lambda var_dir: bootstrap(var_dir=var_dir, console_logging=False),
        build_home_screen=lambda container: HomeScreen(container=container),
    )


def _deep_adapter() -> ToolAdapter:
    from omega_deep.app.bootstrap import bootstrap
    from omega_deep.interfaces.tui.screens.home import HomeScreen

    return ToolAdapter(
        slug="Deep",
        screens_package="omega_deep.interfaces.tui.screens",
        build_container=lambda var_dir: bootstrap(var_dir=var_dir, console_logging=False),
        build_home_screen=lambda container: HomeScreen(container=container),
    )


def _fold_adapter() -> ToolAdapter:
    from omega_fold.app.bootstrap import bootstrap
    from omega_fold.interfaces.tui.screens.home import HomeScreen

    return ToolAdapter(
        slug="Fold",
        screens_package="omega_fold.interfaces.tui.screens",
        build_container=lambda var_dir: bootstrap(var_dir=var_dir, console_logging=False),
        build_home_screen=lambda container: HomeScreen(container=container),
    )


def _stress_adapter() -> ToolAdapter:
    from omega_stress.app.bootstrap import bootstrap
    from omega_stress.interfaces.tui.screens.home import HomeScreen

    # STRESS::bootstrap() n'accepte pas console_logging (verifie a la
    # lecture, seul outil du perimetre dans ce cas) et renvoie un
    # wrapper Application (.container), comme SCAN.
    return ToolAdapter(
        slug="Stress",
        screens_package="omega_stress.interfaces.tui.screens",
        build_container=lambda var_dir: bootstrap(var_dir=var_dir).container,
        build_home_screen=lambda container: HomeScreen(container=container),
    )


def _track_adapter() -> ToolAdapter:
    from omega_track.app.bootstrap import bootstrap
    from omega_track.interfaces.tui.screens.home import HomeScreen

    return ToolAdapter(
        slug="Track",
        screens_package="omega_track.interfaces.tui.screens",
        build_container=lambda var_dir: bootstrap(var_dir=var_dir, console_logging=False),
        build_home_screen=lambda container: HomeScreen(container=container),
    )


def _fuzz_adapter() -> ToolAdapter:
    from omega_fuzz.app.composition_root import build_container, build_tui_scan_runtime
    from omega_fuzz.interfaces.tui.screens.home import HomeScreen

    # Retourne `Any`, jamais `Screen` (contrat import-linter "textual
    # seulement dans interfaces.tui" - aucun symbole de `textual`, pas
    # meme pour un `cast()`, n'est importable ici) : `HomeScreen` de FUZZ
    # n'expose pas de marqueur `py.typed`, mypy le traite deja comme
    # `Any` (`ignore_missing_imports`, pyproject.toml) - assigner cette
    # fonction a `ToolAdapter.build_home_screen: Callable[[Any], Screen]`
    # reste type-safe, `Any` etant compatible avec tout type de retour.
    def _build_home(container: Any) -> Any:
        return HomeScreen(
            container=container,
            scan_runtime_factory=lambda auth_path: build_tui_scan_runtime(auth_path, container=container),
        )

    return ToolAdapter(
        slug="Fuzz",
        screens_package="omega_fuzz.interfaces.tui.screens",
        build_container=lambda var_dir: build_container(var_dir=var_dir, console_logging=False),
        build_home_screen=_build_home,
    )


# Ordre = ordre de la grille Accueil (D-014 point 7), pas alphabetique.
TOOL_ADAPTER_FACTORIES: dict[str, Callable[[], ToolAdapter]] = {
    "scan": _scan_adapter,
    "fuzz": _fuzz_adapter,
    "fold": _fold_adapter,
    "stress": _stress_adapter,
    "check": _check_adapter,
    "deep": _deep_adapter,
    "track": _track_adapter,
}
