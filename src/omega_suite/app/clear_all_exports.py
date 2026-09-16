# Copyright (c) 2026 kraynux [kraynux@proton.me] - Licence MIT (voir fichier LICENSE)
"""Purge globale des dossiers d'export des 7 outils (D-014 point 10).

La purge d'export n'est PAS uniforme entre les 7 outils (verifie au
code) : CHECK/DEEP/FOLD/FUZZ/SCAN/TRACK ont `default_exports_dir`,
STRESS a `export_dir` ; certains ont un `clear_exports()` dedie, d'autres
non (SCAN, STRESS). Deleguer a "la logique de chaque outil" est donc
impossible sans en modifier - hors de question pour des outils finis.
omega-suite implemente donc sa propre petite fonction de purge (identique
au patron deja eprouve chez CHECK/DEEP/FOLD/FUZZ : `shutil.rmtree` +
recreation) et l'applique directement aux dossiers d'export connus - pas
de la logique metier, un geste de nettoyage filesystem trivial (voir
`omega_check.application.commands.clear_exports`, qui documente deja ce
geste ainsi)."""
from __future__ import annotations

import shutil
from pathlib import Path
from typing import Any


def _exports_dir_of(container: Any) -> Path | None:
    return getattr(container, "default_exports_dir", None) or getattr(
        container, "export_dir", None
    )


def clear_all_exports(tool_containers: dict[str, Any]) -> list[str]:
    """Vide le dossier d'export de chaque outil connu. Retourne la liste
    des slugs effectivement vides (pour le message de confirmation)."""
    cleared: list[str] = []
    for slug, container in tool_containers.items():
        directory = _exports_dir_of(container)
        if directory is None:
            continue
        shutil.rmtree(directory, ignore_errors=True)
        directory.mkdir(parents=True, exist_ok=True)
        cleared.append(slug)
    return cleared
