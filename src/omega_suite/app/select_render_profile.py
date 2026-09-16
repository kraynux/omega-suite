# Copyright (c) 2026 kraynux [kraynux@proton.me] - Licence MIT (voir fichier LICENSE)
"""Choisir et persister le profil de rendu de la suite - applique au
prochain demarrage (meme comportement que les 7 outils : le css_path
d'une App Textual est fixe a la construction, pas de rechargement a
chaud, D-014 "Ecran Reglages de la suite")."""
from __future__ import annotations

from omega_lib.terminal.models import RenderProfile

from omega_suite.ports.settings_store import SettingsStore

RENDER_PROFILE_OVERRIDE_KEY = "render_profile_override"


def select_render_profile(
    *, settings_store: SettingsStore, render_profile: RenderProfile | None
) -> None:
    settings_store.set(RENDER_PROFILE_OVERRIDE_KEY, render_profile.value if render_profile else "")
