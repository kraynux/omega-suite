# Copyright (c) 2026 kraynux [kraynux@proton.me] - Licence MIT (voir fichier LICENSE)
"""Choisir et persister le style de navigation de la suite : "accueil"
(grille de boutons, defaut - D-014) ou "onglets" (barre persistante
visible sur tous les ecrans, y compris a l'interieur d'un outil - demande
explicite de l'utilisateur, D-014 point 6 revu). Applique au prochain
demarrage - meme raison que le profil de rendu (select_render_profile.py) :
la barre est injectee une seule fois, au demarrage, dans les classes
d'ecran patchees (screen_patching.py), pas rechargeable a chaud."""
from __future__ import annotations

from typing import Literal

from omega_suite.ports.settings_store import SettingsStore

NAVIGATION_STYLE_KEY = "navigation_style"

NavigationStyle = Literal["accueil", "onglets"]
DEFAULT_NAVIGATION_STYLE: NavigationStyle = "accueil"


def select_navigation_style(*, settings_store: SettingsStore, style: NavigationStyle) -> None:
    settings_store.set(NAVIGATION_STYLE_KEY, style)


def current_navigation_style(*, settings_store: SettingsStore) -> NavigationStyle:
    value = settings_store.get(NAVIGATION_STYLE_KEY, DEFAULT_NAVIGATION_STYLE)
    return "onglets" if value == "onglets" else "accueil"
