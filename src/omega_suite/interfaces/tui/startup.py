# Copyright (c) 2026 kraynux [kraynux@proton.me] - Licence MIT (voir fichier LICENSE)
"""Resout theme et profil de rendu de la suite au demarrage - meme
patron que le `startup_controller.py` identique dans les 7 outils
(D-007/D-008), sans la couche port/query supplementaire (omega-suite n'a
pas les 9 couches des outils, D-000 : juste app/ + interfaces/)."""
from __future__ import annotations

from dataclasses import dataclass

from omega_lib.infrastructure.terminal.detector import SystemTerminalDetector
from omega_lib.terminal.models import RenderProfile, TerminalProfile
from omega_lib.terminal.service import resolve_render_profile
from omega_lib.theme.models import AppliedTheme
from omega_lib.theme.policies import DEFAULT_TUI_THEME
from omega_lib.theme.service import resolve_applied_theme

from omega_suite.app.select_render_profile import RENDER_PROFILE_OVERRIDE_KEY
from omega_suite.app.select_theme import THEME_KEY
from omega_suite.ports.settings_store import SettingsStore


@dataclass(frozen=True, slots=True)
class StartupState:
    terminal: TerminalProfile
    theme: AppliedTheme


def resolve_startup_state(*, settings_store: SettingsStore) -> StartupState:
    signals = SystemTerminalDetector().detect()
    terminal = resolve_render_profile(signals)
    render_profile = _effective_render_profile(terminal, settings_store)

    requested_theme = settings_store.get(THEME_KEY, DEFAULT_TUI_THEME) or DEFAULT_TUI_THEME
    theme = resolve_applied_theme(requested_theme, render_profile)
    if theme.fell_back_from is not None:
        settings_store.set(THEME_KEY, theme.theme_name)

    return StartupState(terminal=terminal, theme=theme)


def _effective_render_profile(
    terminal: TerminalProfile, settings_store: SettingsStore
) -> RenderProfile:
    override = settings_store.get(RENDER_PROFILE_OVERRIDE_KEY, "")
    if override:
        return RenderProfile(override)
    return terminal.render_profile
