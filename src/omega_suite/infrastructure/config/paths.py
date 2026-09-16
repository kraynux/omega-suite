# Copyright (c) 2026 kraynux [kraynux@proton.me] - Licence MIT (voir fichier LICENSE)
"""Resolution du dossier runtime de la suite - meme patron que les 7
outils (D-015 point 8) : `./var` relatif au repertoire de lancement par
defaut, override via `$OMEGA_SUITE_VAR_DIR`. Chaque outil recoit ensuite
un sous-dossier DEDIE (`var/<slug>/`) passe explicitement a son propre
`build_container()` - jamais laisse a son propre defaut, pour ne pas
retomber silencieusement sur un `./var` relatif au lancement d'omega-suite
(D-015 point 8, bug silencieux identifie avant implementation)."""
from __future__ import annotations

import os
from pathlib import Path

DEFAULT_VAR_DIRNAME = "var"
ENV_VAR_DIR = "OMEGA_SUITE_VAR_DIR"


def resolve_var_dir() -> Path:
    override = os.environ.get(ENV_VAR_DIR)
    if override:
        return Path(override)
    return Path.cwd() / DEFAULT_VAR_DIRNAME


def tool_var_dir(suite_var_dir: Path, slug: str) -> Path:
    return suite_var_dir / slug.lower()


def default_settings_path(suite_var_dir: Path) -> Path:
    return suite_var_dir / "settings.json"
