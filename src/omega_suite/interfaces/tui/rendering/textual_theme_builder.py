# Copyright (c) 2026 kraynux [kraynux@proton.me] - Licence MIT (voir fichier LICENSE)
"""Construction des objets textual.theme.Theme a partir de omega_lib.theme.policies.
Copie verbatim du patron deja identique dans les 7 outils (D-007/D-008) -
purement derive de omega_lib, aucune logique propre a un outil."""
from __future__ import annotations

from omega_lib.theme.policies import TUI_THEMES, ThemeDefinition
from textual.theme import Theme as TextualTheme


def build_textual_theme(definition: ThemeDefinition) -> TextualTheme:
    palette = definition.palette
    return TextualTheme(
        name=definition.name,
        primary=palette.accent,
        secondary=palette.secondary,
        warning=palette.warning,
        error=palette.error,
        success=palette.success,
        foreground=palette.foreground,
        background=palette.background,
        surface=palette.surface,
        panel=palette.panel,
        dark=definition.dark,
        variables={},
    )


def build_all_textual_themes() -> tuple[TextualTheme, ...]:
    return tuple(build_textual_theme(definition) for definition in TUI_THEMES.values())
