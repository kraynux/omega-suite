# Copyright (c) 2026 kraynux [kraynux@proton.me] - Licence MIT (voir fichier LICENSE)
"""Ecran Aide de la suite (D-014 point 10) : raccourcis globaux +
navigation par onglets + tableau recapitulatif du perimetre des 7 outils
(condense de leur propre `_SCOPE_NOTICE`). Affiche uniquement depuis
Accueil - depuis un onglet outil, `a` ouvre le HelpScreen de cet outil,
inchange (dispatch fait par OmegaSuiteApp.action_help(), pas ici)."""
from __future__ import annotations

from textual.app import ComposeResult
from textual.containers import Container, Horizontal, VerticalScroll
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Static

from omega_suite.shared.i18n import _

_SHORTCUTS: tuple[tuple[str, str], ...] = (
    (_("Haut / Bas"), _("Naviguer entre les éléments d'un écran")),
    (_("Tab / Maj+Tab"), _("Naviguer entre les champs d'un formulaire")),
    (_("Échap"), _("Retour à l'écran précédent (confirmation de sortie sur l'accueil)")),
    ("t", _("Thème suivant (appliqué immédiatement, sans confirmation)")),
    ("r", _("Rafraîchir la détection du terminal")),
    ("a", _("Aide (celle de la suite depuis Accueil, celle de l'outil depuis un onglet)")),
    ("s", _("Réglages de la suite")),
    ("q", _("Quitter la suite (avec confirmation)")),
)

_TOOL_SCOPES: tuple[tuple[str, str], ...] = (
    ("Omega-SCAN", _("Observe la posture de sécurité visible d'un service HTTP/HTTPS : aucun "
                     "test actif.")),
    ("Omega-FUZZ", _("Découvre une cible dans un périmètre contrôlé puis teste activement ses "
                     "points d'entrée - jamais sans confirmation.")),
    ("Omega-FOLD", _("Analyse un répertoire local ou crawle un site distant sous des "
                     "garde-fous toujours actifs (profondeur, pages, même domaine).")),
    ("Omega-STRESS", _("Testeur de charge de serveur.")),
    ("Omega-CHECK", _("Identifie les services d'une cible unique (scan fixe) : jamais de test "
                      "actif ni d'authentification tentée.")),
    ("Omega-DEEP", _("Découvre et cartographie l'architecture autour d'une cible racine : rien "
                     "n'est scanné sans validation explicite.")),
    ("Omega-TRACK", _("Observe des cibles explicitement enregistrées et autorisées : aucune "
                      "découverte ni dérive automatique.")),
)


class HelpScreen(Screen[None]):
    def compose(self) -> ComposeResult:
        yield Header()
        with VerticalScroll(classes="omega-panel"):
            yield Static(_("AIDE DE LA SUITE"), classes="omega-title")

            yield Static(_("Raccourcis clavier"), classes="omega-subtitle")
            for key, description in _SHORTCUTS:
                yield Static(_("{key:<14} {description}").format(key=key, description=description))
            yield Static("")

            yield Static(_("Navigation"), classes="omega-subtitle")
            yield Static(
                _("Chaque outil est un onglet : le choisir (barre du haut ou bouton d'Accueil) "
                  "affiche instantanément ses propres écrans - la pile d'écrans de chaque "
                  "outil reste intacte en arrière-plan tant qu'on ne quitte pas la suite, rien "
                  "n'est perdu en changeant d'onglet.")
            )
            yield Static("")

            yield Static(_("Stockage des exports"), classes="omega-subtitle")
            yield Static(
                _("Chaque outil écrit ses propres exports dans var/<outil>/exports/ et ses "
                  "captures d'écran dans var/<outil>/screenshots/, relatif au dossier où "
                  "omega-suite a été lancé (ou sous $OMEGA_SUITE_VAR_DIR/<outil>/ si cette "
                  "variable d'environnement est définie). Chaque outil peut redéfinir son "
                  "propre dossier de destination depuis ses propres Réglages. 'Vider tous les "
                  "exports' (Réglages de la suite) vide ce dossier pour les 7 outils d'un "
                  "coup, même ceux jamais ouverts cette session.")
            )
            yield Static("")

            yield Static(_("Périmètre des 7 outils"), classes="omega-subtitle")
            for name, scope in _TOOL_SCOPES:
                yield Static(f"[b]{name}[/b]\n{scope}\n")
            yield Static(
                _("Le tout premier chargement d'un outil (onglet ou bouton d'Accueil) prend un "
                  "court instant, le temps de le charger en mémoire - une notification "
                  "l'indique. Les visites suivantes de ce même outil, le reste de la session, "
                  "sont instantanées.")
            )
            yield Static("")

            with Horizontal(classes="omega-actions"), Container(classes="omega-btn-frame"):
                yield Button(_("Retour"), id="back")
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "back":
            self.dismiss()
