# Copyright (c) 2026 kraynux [kraynux@proton.me] - Licence MIT (voir fichier LICENSE)
"""Composition ASCII de l'ecran de demarrage. Logo fourni par l'utilisateur,
voir ~/DEV/SUITE/ascii.txt (section "LOGO ASCII splash") - caracteres non
modifies, meme convention que les 7 outils (CHECK notamment).

Alignement (retour utilisateur, 3 rounds - voir aussi
~/DEV/SUITE/DECISIONS_ARCHITECTURE.md) :
- Round 1 : centrage independant de chaque ligne (`str.center(85)`)
  cassait l'alignement ENTRE les 4 lignes du diagramme reseau (labels de
  longueurs differentes -> chaine totale de longueur differente -> centre
  differemment).
- Round 2 : tentative de preserver l'indentation D'ORIGINE du fichier
  source (tabulations etendues a 8 colonnes) - a REVELE que cette
  indentation n'etait fiable QUE pour la partie superieure du dessin
  (boite LINUX SCANNER SUITE, badge V1.5, socle ▄██▄, espaces uniquement
  dans le fichier) ; la partie inferieure (diagramme reseau, socle bas,
  tagline - ecrite avec des tabulations dans le fichier) ne correspondait
  PAS a un centrage geometrique reel une fois les tabulations etendues -
  vraisemblablement un artefact d'affichage de l'editeur du createur du
  fichier (tabstops differents de l'hypothese 8-colonnes), pas un
  positionnement intentionnel.
- Round 3 (celui-ci) : calcul GEOMETRIQUE pur, plus aucune indentation
  copiee du fichier source. Chaque element symetrique est centre sur
  `_WIDTH=85` (largeur de la grande boite OMEGA-SUITE, l'axe de reference
  commun). Les 4 lignes du diagramme reseau sont un cas particulier : leur
  prefixe avant l'unite d'ecran ("<nom>---") fait TOUJOURS exactement 13
  caracteres dans les 4 lignes (l'auteur a deja equilibre le nombre de
  tirets pour ca - verifie caractere par caractere), donc c'est l'UNITE
  D'ECRAN elle-meme ("█<boite>█", 17 caracteres - meme largeur que le
  socle _CAP_TOP juste au-dessus) qui doit etre centree sur `_WIDTH`,
  jamais la ligne entiere (le suffixe "---NOM-OUTIL" a droite varie de
  13 a 15 caracteres selon l'outil, ce qui decale l'unite d'ecran si on
  centre la ligne complete).

Couleurs demandees dans ascii.txt :
- cadres/"containers" : clair ($foreground).
- texte "LINUX SCANNER SUITE" : vif ($accent).
- bandeau OMEGA-SUITE (3 lignes, dans sa boite) : vif / clair / vif.
- noms d'outils (OMEGA-SCAN, OMEGA-CHECK, ...) sur le diagramme reseau :
  "OMEGA" vif, "-" en nuance, le reste clair (retour utilisateur - 3 tons
  distincts, jamais un segment laisse sans balise de couleur : un segment
  non balise heritait sinon de la couleur par defaut du widget, $accent).
- tagline du bas : mots clairs, "|" vifs (meme convention que CHECK).
- degrade de blocs █▓▒░ : █ clair, ▓ un ton en dessous ($secondary),
  ▒/░ un ton encore en dessous (meme couleur pour les deux, faute de
  4e jeton de theme disponible - demande explicitement groupee ainsi
  dans ascii.txt : "1 nuance en dessous" pour les deux caracteres)."""
from __future__ import annotations

from textual.widgets import Static

_WIDTH = 85
"""Largeur de la grande boite OMEGA-SUITE - axe de centrage commun a
tout le dessin."""

_SHADE_COLORS = {
    "█": "$foreground",
    "▓": "$secondary",
    "▒": "$foreground 40%",
    "░": "$foreground 40%",
}


def _centered(line: str) -> str:
    return line.center(_WIDTH)


def _shaded(line: str, default: str = "$foreground") -> str:
    """Colore chaque caractere de degrade selon `_SHADE_COLORS`, le reste
    (espaces, texte "V1.5", cadres ╠╣) dans `default`."""
    return "".join(f"[{_SHADE_COLORS.get(ch, default)}]{ch}[/]" for ch in line)


def _split_frame(line: str, frame_char: str = "│") -> str:
    """Ligne du type '│ texte │' (deja centree) -> cadre clair, texte vif."""
    prefix, _, rest = line.partition(frame_char)
    inner, _, suffix = rest.rpartition(frame_char)
    return f"{prefix}[$foreground]{frame_char}[/][$accent]{inner}[/][$foreground]{frame_char}{suffix}[/]"


def _wordmark_line(line: str, color: str, frame_char: str = "│") -> str:
    prefix, _, rest = line.partition(frame_char)
    inner, _, suffix = rest.rpartition(frame_char)
    return f"{prefix}[$foreground]{frame_char}[/][{color}]{inner}[/][$foreground]{frame_char}{suffix}[/]"


def _tagline(line: str) -> str:
    """'SCANNER | TESTER | ...' -> mots clairs, '|' vifs."""
    parts = line.split("|")
    colored = [f"[$foreground]{part}[/]" for part in parts]
    return "[$accent]|[/]".join(colored)


def _colored_label(name: str) -> str:
    """'OMEGA-SCAN' -> 'OMEGA' vif, '-' en nuance, 'SCAN' clair (retour
    utilisateur : les 3 parties d'un nom d'outil ont chacune leur propre
    ton, pas un bloc uniforme)."""
    prefix, sep, suffix = name.partition("-")
    return f"[$accent]{prefix}[/][$secondary]{sep}[/][$foreground]{suffix}[/]"


def _diagram_row(left_name: str, right_name: str, middle: str) -> str:
    """Construit une ligne du diagramme reseau en ancrant l'UNITE D'ECRAN
    ("█<middle>█", `_BEZEL_WIDTH` caracteres) sur le meme axe que
    `_CAP_TOP`/`_CAP_BOTTOM` juste au-dessus/en-dessous - jamais en
    centrant la ligne entiere (voir docstring du module). Cote gauche :
    nombre de tirets ajuste pour que "<nom>---" fasse toujours
    `_PREFIX_WIDTH` caracteres (verifie dans le fichier source - l'auteur
    compense deja les noms plus longs avec moins de tirets), condition
    necessaire a l'ancrage de l'unite d'ecran. Cote droit : purement
    decoratif (n'ancre rien), toujours 3 tirets dans le fichier source
    quelle que soit la longueur du nom, jamais recalcule."""
    left_dashes = "─" * (_PREFIX_WIDTH - len(left_name))
    right_dashes = "───"
    bezel = f"█{middle}█"
    leading = " " * ((_WIDTH - _BEZEL_WIDTH) // 2 - _PREFIX_WIDTH)
    line = f"{leading}{left_name}{left_dashes}{bezel}{right_dashes}{right_name}"
    left_idx = len(leading)
    after_left = left_idx + len(left_name)
    bezel_end = after_left + len(left_dashes) + len(bezel)
    right_idx = bezel_end + len(right_dashes)
    after_right = right_idx + len(right_name)
    return (
        _shaded(line[:left_idx])
        + _colored_label(left_name)
        + _shaded(line[after_left:right_idx])
        + _colored_label(right_name)
        + _shaded(line[after_right:])
    )


_PREFIX_WIDTH = 13
"""'<NOM>' + tirets, TOUJOURS 13 caracteres dans les 4 lignes du fichier
source (l'auteur a deja compense les noms d'outils plus longs avec moins
de tirets) - verifie caractere par caractere."""
_BEZEL_WIDTH = 17
"""'█<boite>█' - meme largeur que `_CAP_TOP`/`_CAP_BOTTOM`, doit se
centrer sur le meme axe qu'eux."""

_LINUX_BOX = (
    "┌─────────────────────┐",
    "│ LINUX SCANNER SUITE │",
    "└─────────────────────┘",
)

_BADGE = "░▒▓█V1.5█▓▒░"

_OMEGA_BOX = (
    "┌───────────────────────────────────────────────────────────────────────────────────┐",
    "│ ┌╦═══╦┐ ┌╦═╦═╦┐ ┌╦═══╦┐ ┌╦═══╦┐ ┌╦═══╦┐   ┌╦═══╦┐ ┌╦   ╦┐ ┌═╤╦╤═┐ ┌═╤╦╤═┐ ┌╦═══╦┐ │",
    "│ │║   ║│ │║ ║ ║│ ├╬══    │║  ═╦┐ ├╬═══╬┤ ═ └╩═══╦┐ │║   ║│   │║│     │║│   ├╬══    │",
    "│ └╩═══╩┘ └╩   ╩┘ └╩═══╩┘ └╩═══╩┘ └╩   ╩┘   └╩═══╩┘ └╩═══╩┘ └═╧╩╧═┘   ╧╩╧   └╩═══╩┘ │",
    "└───────────────────────────────────────────────────────────────────────────────────┘",
)

_CAP_TOP = "▄▄▄▄▄▄▄▄██▄▄▄▄▄▄▄"
_CAP_BOTTOM = "█████████████████"
_CAP_SMALL = "███▓███"
_CAP_STRIPE = "╠░░░░░░░░░░░░░╣"

_TAGLINE = "SCANNER | TESTER | FINDER | NETWORK"

_LINES: tuple[str, ...] = (
    f"[$foreground]{_centered(_LINUX_BOX[0])}[/]",
    _split_frame(_centered(_LINUX_BOX[1])),
    f"[$foreground]{_centered(_LINUX_BOX[2])}[/]",
    _shaded(_centered(_BADGE)),
    f"[$foreground]{_centered(_OMEGA_BOX[0])}[/]",
    _wordmark_line(_centered(_OMEGA_BOX[1]), "$accent"),
    _wordmark_line(_centered(_OMEGA_BOX[2]), "$foreground"),
    _wordmark_line(_centered(_OMEGA_BOX[3]), "$accent"),
    f"[$foreground]{_centered(_OMEGA_BOX[4])}[/]",
    _shaded(_centered(_CAP_TOP)),
    _diagram_row("OMEGA-SCAN", "OMEGA-TRACK", "┌─────────────┐"),
    _diagram_row("OMEGA-CHECK", "OMEGA-FUZZ", "│~/find ░░░░░░│"),
    _diagram_row("OMEGA-DEEP", "OMEGA-STRESS", "│ip:127.0.0.1░│"),
    _diagram_row("OMEGA-FOLD", "OMEGA-SUITE", "└─────────────┘"),
    _shaded(_centered(_CAP_BOTTOM)),
    _shaded(_centered(_CAP_SMALL)),
    _shaded(_centered(_CAP_STRIPE)),
    "",
    _tagline(_centered(_TAGLINE)),
)

_MARKUP = "\n".join(_LINES)


class SplashHero(Static):
    """Bloc decoratif de l'ecran de demarrage (screens/splash.py)."""

    def __init__(self) -> None:
        super().__init__(_MARKUP, classes="omega-splash-hero")
