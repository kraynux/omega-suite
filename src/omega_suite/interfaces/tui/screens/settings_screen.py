# Copyright (c) 2026 kraynux [kraynux@proton.me] - Licence MIT (voir fichier LICENSE)
"""Ecran Reglages de la suite (D-014) : theme + profil de rendu -
generiques, communs aux 7 outils - et un bouton de purge globale des
exports. Tout le reste (dossiers export/captures par outil, purges
specifiques) reste dans le Reglages de chaque outil, inchange."""
from __future__ import annotations

from typing import TYPE_CHECKING

from omega_lib.terminal.models import RenderProfile
from omega_lib.theme.policies import TUI_THEMES
from textual.app import ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Select, Static

from omega_suite.app.clear_all_exports import clear_all_exports
from omega_suite.app.select_navigation_style import (
    NavigationStyle,
    current_navigation_style,
    select_navigation_style,
)
from omega_suite.app.select_render_profile import select_render_profile
from omega_suite.app.select_theme import UnknownThemeError, select_theme
from omega_suite.interfaces.tui.screens.confirm import ConfirmScreen

if TYPE_CHECKING:
    from omega_suite.app.dependency_container import DependencyContainer

_AUTO = "auto"
_RENDER_PROFILE_OVERRIDE_KEY = "render_profile_override"
_NAVIGATION_CHOICES = (("Accueil (grille de boutons)", "accueil"), ("Onglets (barre persistante)", "onglets"))


class SettingsScreen(Screen[None]):
    def __init__(self, *, container: DependencyContainer) -> None:
        super().__init__()
        self._container = container

    def compose(self) -> ComposeResult:
        store = self._container.settings_store
        yield Header()
        with Vertical(classes="omega-form-panel"):
            yield Static("REGLAGES DE LA SUITE", classes="omega-title")

            yield Static("Theme", classes="omega-subtitle")
            yield Select(
                [(name, name) for name in TUI_THEMES],
                value=self.app.theme,
                allow_blank=False,
                id="theme-select",
            )

            yield Static("Profil de rendu (redemarrage requis)", classes="omega-subtitle")
            current_override = store.get(_RENDER_PROFILE_OVERRIDE_KEY, "")
            yield Select(
                [("Automatique", _AUTO)] + [(p.value, p.value) for p in RenderProfile],
                value=current_override or _AUTO,
                allow_blank=False,
                id="render-profile-select",
            )

            yield Static("Style de navigation (redemarrage requis)", classes="omega-subtitle")
            yield Select(
                _NAVIGATION_CHOICES,
                value=current_navigation_style(settings_store=store),
                allow_blank=False,
                id="navigation-style-select",
            )

            yield Static("Purge", classes="omega-subtitle")
            with Horizontal(classes="omega-actions"), Container(classes="omega-btn-frame"):
                yield Button("Vider tous les exports", id="clear-all-exports", variant="error")

            with Horizontal(classes="omega-actions"), Container(classes="omega-btn-frame"):
                yield Button("Retour", id="back")
        yield Footer()

    def on_select_changed(self, event: Select.Changed) -> None:
        if event.select.id == "theme-select":
            if str(event.value) == self.app.theme:
                return
            self._apply_theme(str(event.value))
        elif event.select.id == "render-profile-select":
            current_override = (
                self._container.settings_store.get(_RENDER_PROFILE_OVERRIDE_KEY, "") or _AUTO
            )
            if str(event.value) == current_override:
                return
            self._apply_render_profile(str(event.value))
        elif event.select.id == "navigation-style-select":
            current_style = current_navigation_style(settings_store=self._container.settings_store)
            if str(event.value) == current_style:
                return
            new_style: NavigationStyle = "onglets" if str(event.value) == "onglets" else "accueil"
            select_navigation_style(settings_store=self._container.settings_store, style=new_style)
            self._offer_restart("Style de navigation")

    def _offer_restart(self, setting_label: str) -> None:
        """Le reglage est deja ecrit (appelant) - ne demande qu'a relancer
        TOUT DE SUITE plutot que de laisser l'utilisateur sur un simple
        "applique au prochain demarrage" sans action concrete (bug
        d'ergonomie reel constate) : `App.pending_restart` (interfaces.
        tui/app.py) + `os.execv()` dans `omega_suite/__main__.py`, jamais
        ici - `self.app.exit()` doit d'abord rendre la main pour que
        Textual s'arrete proprement et le terminal soit restaure avant
        que le processus ne soit remplace."""
        self.app.push_screen(
            ConfirmScreen(
                title="REDEMARRER OMEGA-SUITE ?",
                message=(
                    f"{setting_label} modifie - ne s'applique qu'au demarrage. "
                    "Fermer puis relancer omega-suite tout de suite ?"
                ),
            ),
            self._restart_if_confirmed,
        )

    def _restart_if_confirmed(self, confirmed: bool | None) -> None:
        if not confirmed:
            self.app.notify("Applique au prochain demarrage.")
            return
        self.app.pending_restart = True  # type: ignore[attr-defined]
        self.app.exit()

    def _apply_theme(self, theme_name: str) -> None:
        try:
            select_theme(settings_store=self._container.settings_store, theme_name=theme_name)
        except UnknownThemeError as exc:
            self.app.notify(str(exc), severity="error")
            return
        self.app.theme = theme_name

    def _apply_render_profile(self, value: str) -> None:
        profile = None if value == _AUTO else RenderProfile(value)
        select_render_profile(settings_store=self._container.settings_store, render_profile=profile)
        self._offer_restart("Profil de rendu")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "back":
            self.dismiss()
        elif event.button.id == "clear-all-exports":
            self.app.push_screen(
                ConfirmScreen(
                    title="VIDER TOUS LES EXPORTS ?",
                    message=(
                        "Le dossier d'export des 7 outils sera definitivement vide "
                        "(rien d'autre n'est touche)."
                    ),
                ),
                self._clear_all_exports_if_confirmed,
            )

    def _clear_all_exports_if_confirmed(self, confirmed: bool | None) -> None:
        if not confirmed:
            return
        # get_all_tool_containers() (pas .tool_containers) : cette action
        # doit vider les exports des 7 outils meme ceux jamais ouverts
        # cette session (construction paresseuse, dependency_container.py)
        # - seule action de la suite ou payer ce cout une fois est justifie.
        cleared = clear_all_exports(self._container.get_all_tool_containers())
        self.app.notify(f"Exports vides pour {len(cleared)} outil(s).")
