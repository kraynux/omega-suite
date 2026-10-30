# Copyright (c) 2026 kraynux [kraynux@proton.me] - Licence MIT (voir fichier LICENSE)
"""Purge globale des dossiers d'export des 7 outils (D-014 point 10).

La purge d'export n'est PAS uniforme entre les 7 outils (verifie au
code) : CHECK/DEEP/FOLD/FUZZ/SCAN/TRACK ont `default_exports_dir`,
STRESS a `export_dir` ; certains ont un `clear_exports()` dedie, d'autres
non (SCAN, STRESS). Deleguer a "la logique de chaque outil" est donc
impossible sans en modifier. omega-suite implemente donc sa propre petite
fonction de purge et l'applique directement aux dossiers d'export connus.

Correctif 2026-10-27 (commun a la suite omega-*) :
- dossier vide = celui CONFIGURE dans les reglages de l'outil
  (`exports_dir_override` de son propre fichier de reglages), sinon son
  dossier par defaut - auparavant toujours le dossier par defaut ;
- seul le CONTENU est supprime, le dossier reste ; un lien symbolique est
  supprime sans suivre sa cible ;
- dossiers systeme, personnels, dossier de la suite et ses parents
  refuses (le chemin d'un outil est un champ libre) ;
- un element qui resiste (droits) est signale, jamais retente avec
  `sudo` (une demande de mot de passe figerait l'interface)."""
from __future__ import annotations

import shutil
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from omega_suite.shared.i18n import _

_EXPORTS_DIR_OVERRIDE_KEY = "exports_dir_override"
_SYSTEM_DIRS = frozenset(Path(p) for p in (
    "/", "/bin", "/boot", "/dev", "/etc", "/home", "/lib", "/lib32", "/lib64", "/media", "/mnt",
    "/opt", "/proc", "/root", "/run", "/sbin", "/srv", "/sys", "/tmp", "/usr", "/var",
    "/var/lib", "/var/log", "/usr/local",
))


@dataclass
class ClearAllResult:
    cleared: list[str] = field(default_factory=list)
    """Outils dont le dossier a ete vide (entierement ou en partie)."""
    problems: list[str] = field(default_factory=list)
    """Une ligne par dossier refuse ou element impossible a supprimer."""


def _exports_dir_of(container: Any) -> Path | None:
    default = getattr(container, "default_exports_dir", None) or getattr(container, "export_dir", None)
    if default is None:
        return None
    store = getattr(container, "settings_store", None)
    override = ""
    if store is not None:
        try:
            override = (store.get(_EXPORTS_DIR_OVERRIDE_KEY, "") or "").strip()
        except (OSError, ValueError):
            override = ""
    return Path(override).expanduser() if override else Path(default)


def _refusal(directory: Path, suite_root: Path) -> str | None:
    target = directory.resolve()
    root = suite_root.resolve()
    if target in _SYSTEM_DIRS or target.parent == Path("/home"):
        return _("dossier système ou personnel")
    if target == root or target in root.parents:
        return _("contient l'installation d'omega-suite")
    if target.exists() and not target.is_dir():
        return _("ce n'est pas un dossier")
    return None


def clear_all_exports(tool_containers: dict[str, Any], suite_root: Path) -> ClearAllResult:
    """Vide le dossier d'export de chaque outil connu. Peut etre long (construction des
    conteneurs, gros dossiers) : a appeler hors du thread de l'interface."""
    result = ClearAllResult()
    for slug, container in tool_containers.items():
        directory = _exports_dir_of(container)
        if directory is None:
            continue
        reason = _refusal(directory, suite_root)
        if reason is not None:
            result.problems.append(_("{slug} : dossier refusé ({reason}) : {resolve}").format(slug=slug, reason=reason, resolve=directory.resolve()))
            continue
        directory.mkdir(parents=True, exist_ok=True)
        for entry in sorted(directory.iterdir()):
            try:
                if entry.is_dir() and not entry.is_symlink():
                    shutil.rmtree(entry)
                else:
                    entry.unlink()
            except OSError as exc:
                result.problems.append(f"{slug} : {entry.name} ({exc.strerror or exc})")
        result.cleared.append(slug)
    return result
