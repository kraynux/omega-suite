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

_SHORTCUTS: tuple[tuple[str, str], ...] = (
    ("Haut / Bas", "Naviguer entre les elements d'un ecran"),
    ("Tab / Maj+Tab", "Naviguer entre les champs d'un formulaire"),
    ("Echap", "Retour a l'ecran precedent (confirmation de sortie sur l'accueil)"),
    ("t", "Theme suivant (applique immediatement, sans confirmation)"),
    ("r", "Rafraichir la detection du terminal"),
    ("a", "Aide (celle de la suite depuis Accueil, celle de l'outil depuis un onglet)"),
    ("s", "Reglages de la suite"),
    ("q", "Quitter la suite (avec confirmation)"),
)

_TOOL_SCOPES: tuple[tuple[str, str], ...] = (
    ("Omega-SCAN", "Observe la posture de securite visible d'un service HTTP/HTTPS : aucun test actif."),
    ("Omega-FUZZ", "Decouvre une cible dans un perimetre controle puis teste activement ses points d'entree - jamais sans confirmation."),
    ("Omega-FOLD", "Analyse un repertoire local ou crawle un site distant sous des garde-fous toujours actifs (profondeur, pages, meme domaine)."),
    ("Omega-STRESS", "Testeur de charge de serveur."),
    ("Omega-CHECK", "Identifie les services d'une cible unique (scan fixe) : jamais de test actif ni d'authentification tentee."),
    ("Omega-DEEP", "Decouvre et cartographie l'architecture autour d'une cible racine : rien n'est scanne sans validation explicite."),
    ("Omega-TRACK", "Observe des cibles explicitement enregistrees et autorisees : aucune decouverte ni derive automatique."),
)


class HelpScreen(Screen[None]):
    def compose(self) -> ComposeResult:
        yield Header()
        with VerticalScroll(classes="omega-panel"):
            yield Static("AIDE DE LA SUITE", classes="omega-title")

            yield Static("Raccourcis clavier", classes="omega-subtitle")
            for key, description in _SHORTCUTS:
                yield Static(f"{key:<14} {description}")
            yield Static("")

            yield Static("Navigation", classes="omega-subtitle")
            yield Static(
                "Chaque outil est un onglet : le choisir (barre du haut ou bouton "
                "d'Accueil) affiche instantanement ses propres ecrans - la pile "
                "d'ecrans de chaque outil reste intacte en arriere-plan tant qu'on "
                "ne quitte pas la suite, rien n'est perdu en changeant d'onglet."
            )
            yield Static("")

            yield Static("Stockage des exports", classes="omega-subtitle")
            yield Static(
                "Chaque outil ecrit ses propres exports dans var/<outil>/exports/ "
                "et ses captures d'ecran dans var/<outil>/screenshots/, relatif au "
                "dossier ou omega-suite a ete lance (ou sous "
                "$OMEGA_SUITE_VAR_DIR/<outil>/ si cette variable d'environnement "
                "est definie). Chaque outil peut redefinir son propre dossier de "
                "destination depuis ses propres Reglages. 'Vider tous les "
                "exports' (Reglages de la suite) vide ce dossier pour les 7 "
                "outils d'un coup, meme ceux jamais ouverts cette session."
            )
            yield Static("")

            yield Static("Perimetre des 7 outils", classes="omega-subtitle")
            for name, scope in _TOOL_SCOPES:
                yield Static(f"[b]{name}[/b]\n{scope}\n")
            yield Static(
                "Le tout premier chargement d'un outil (onglet ou bouton "
                "d'Accueil) prend un court instant, le temps de le charger en "
                "memoire - une notification l'indique. Les visites suivantes de "
                "ce meme outil, le reste de la session, sont instantanees."
            )
            yield Static("")

            with Horizontal(classes="omega-actions"), Container(classes="omega-btn-frame"):
                yield Button("Retour", id="back")
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "back":
            self.dismiss()
