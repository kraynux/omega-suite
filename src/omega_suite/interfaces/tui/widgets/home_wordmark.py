# Copyright (c) 2026 kraynux [kraynux@proton.me] - Licence MIT (voir fichier LICENSE)
"""Bandeau texte OMEGA-SUITE affiche en haut de screens/accueil.py (logo
fourni par l'utilisateur, voir ~/DEV/SUITE/ascii.txt section "LOGO MENU
GENERAL" - caracteres non modifies, meme regle que les 7 outils).
Couleur par jetons de theme Rich/Textual ($accent/$foreground)
directement dans le markup - reactif au changement de theme (meme
mecanisme que widgets/splash_hero.py)."""
from __future__ import annotations

from textual.widgets import Static

_WIDTH = 81
"""Largeur des lignes 1 et 3 (l'element le plus large - la ligne 2 est
plus courte de 3 caracteres dans le fichier source, centree sur le meme
axe plutot que sur sa propre longueur)."""

_WORDMARK_LINES = (
    "┌╦═══╦┐ ┌╦═╦═╦┐ ┌╦═══╦┐ ┌╦═══╦┐ ┌╦═══╦┐   ┌╦═══╦┐ ┌╦   ╦┐ ┌═╤╦╤═┐ ┌═╤╦╤═┐ ┌╦═══╦┐",
    "│║   ║│ │║ ║ ║│ ├╬══    │║  ═╦┐ ├╬═══╬┤ ═ └╩═══╦┐ │║   ║│   │║│     │║│   ├╬══",
    "└╩═══╩┘ └╩   ╩┘ └╩═══╩┘ └╩═══╩┘ └╩   ╩┘   └╩═══╩┘ └╩═══╩┘ └═╧╩╧═┘   ╧╩╧   └╩═══╩┘",
)
"""OMEGA-SUITE en un seul bandeau de lettres, fourni par l'utilisateur
(~/DEV/SUITE/ascii.txt), caracteres non modifies."""

_MARKUP = "\n".join((
    f"[$accent]{_WORDMARK_LINES[0].center(_WIDTH)}[/]",
    # .ljust AVANT .center : la ligne 2, plus courte, doit garder le meme
    # bord gauche que les lignes 1/3 (retour utilisateur - centrer une
    # chaine plus courte sur son propre axe la decale visuellement par
    # rapport aux deux autres lignes).
    f"[$foreground]{_WORDMARK_LINES[1].ljust(_WIDTH).center(_WIDTH)}[/]",
    f"[$accent]{_WORDMARK_LINES[2].center(_WIDTH)}[/]",
))


class HomeWordmark(Static):
    """Bandeau decoratif centre en haut de screens/accueil.py."""

    def __init__(self) -> None:
        super().__init__(_MARKUP, classes="omega-home-wordmark")
