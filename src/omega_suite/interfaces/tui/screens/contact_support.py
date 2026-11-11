# Copyright (c) 2026 kraynux - kraynux@proton.me - Licence MIT (voir fichier LICENSE)
"""Aide de la suite -> Contact et support : ecrans partages d'omega-lib (D-016, 2026-11-09), repris
d'omega-serv / omega-log. Declaration « omega-suite », une seule fois, la seule de la suite : l'aide
d'un onglet ouvre aussi celle-ci (l'ecran de l'outil, sa base et ses traductions, mais la declaration de
la suite)."""
from __future__ import annotations

from typing import Any, ClassVar

from omega_lib.interfaces.tui.contact_support import ContactSupportKit
from omega_lib.ports.declaration import ContactSupportServices
from textual.binding import Binding, BindingType
from textual.screen import Screen

from omega_suite.shared.i18n import STATE, _


class _SuiteScreen(Screen[None]):
    """Memes touches que l'Accueil : Echap -> retour, fleches -> element suivant / precedent."""

    BINDINGS: ClassVar[list[BindingType]] = [
        Binding("escape", "back", _("Retour"), show=True),
        Binding("up", "focus_previous_item", _("Monter"), show=False),
        Binding("down", "focus_next_item", _("Descendre"), show=False),
    ]

    def action_back(self) -> None:
        self.dismiss()

    def action_focus_previous_item(self) -> None:
        self.focus_previous()

    def action_focus_next_item(self) -> None:
        self.focus_next()


def contact_support_screen(services: ContactSupportServices) -> Screen[Any]:
    kit = ContactSupportKit(services=services, translate=_,
                            language_code=lambda: STATE.language.code, base_screen=_SuiteScreen)
    return kit.screen()
