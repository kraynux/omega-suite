<!-- Copyright (c) 2026 kraynux - kraynux@proton.me - Licence MIT (voir fichier LICENSE) -->
<div align="center">
  <img src="https://raw.githubusercontent.com/kraynux/kraynux/refs/heads/main/docs/assets/omega-suite.png" alt="Omega-Suite" width="384">
</div>


#  OMEGA-SUITE

**Ensemble des scanners "OMEGA" réunifiés dans une seule interface et une bibliotheque partagée**

> Élaboré par **kraynux** pour **Omega-server** 
[kraynux.snake-mackarel](https://kraynux.snake-mackarel.ts.net)

Page officielle : [OMEGA-SUITE](https://kraynux.snake-mackarel.ts.net/omega-suite/) &nbsp;   
Screenshots → [omega-scan](https://kraynux.snake-mackarel.ts.net/omega-scan/screenshots/) · [omega-check](https://kraynux.snake-mackarel.ts.net/omega-check/screenshots/) · [omega-deep](https://kraynux.snake-mackarel.ts.net/omega-deep/screenshots/) · [omega-fold](https://kraynux.snake-mackarel.ts.net/omega-fold/screenshots/) · [omega-track](https://kraynux.snake-mackarel.ts.net/omega-track/screenshots/) · [omega-fuzz](https://kraynux.snake-mackarel.ts.net/omega-fuzz/screenshots/) · [omega-stress](https://kraynux.snake-mackarel.ts.net/omega-stress/screenshots/) 

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux-informational.svg)](https://www.linux.org/)
[![Interface](https://img.shields.io/badge/Interface-Textual%20TUI-cyan.svg)](https://github.com/Textualize/textual)

**Langues:**
<img src="https://flagcdn.com/w20/fr.png" alt="France" style="height:14px;"> [Français](README.md) · <img src="https://flagcdn.com/w20/gb.png" alt="English" style="height:14px;"> [English](docs/translation/en/README.md) · <img src="https://flagcdn.com/w20/es.png" alt="Español" style="height:14px;"> [Español](docs/translation/es/README.md) · <img src="https://flagcdn.com/w20/br.png" alt="Português (Brasil)" style="height:14px;"> [Português (Brasil)](docs/translation/pt-BR/README.md) · <img src="https://flagcdn.com/w20/it.png" alt="Italiano" style="height:14px;"> [Italiano](docs/translation/it/README.md) · <img src="https://flagcdn.com/w20/de.png" alt="Deutsch" style="height:14px;"> [Deutsch](docs/translation/de/README.md) · <img src="https://flagcdn.com/w20/nl.png" alt="Nederlands" style="height:14px;"> [Nederlands](docs/translation/nl/README.md) · <img src="https://flagcdn.com/w20/pl.png" alt="Polski" style="height:14px;"> [Polski](docs/translation/pl/README.md) · <img src="https://flagcdn.com/w20/ru.png" alt="Русский" style="height:14px;"> [Русский](docs/translation/ru/README.md) · <img src="https://flagcdn.com/w20/cn.png" alt="中文" style="height:14px;"> [中文](docs/translation/zh-CN/README.md) · <img src="https://flagcdn.com/w20/vn.png" alt="Tiếng Việt" style="height:14px;"> [Tiếng Việt](docs/translation/vi/README.md) · <img src="https://flagcdn.com/w20/th.png" alt="ไทย" style="height:14px;"> [ไทย](docs/translation/th/README.md) · <img src="https://flagcdn.com/w20/id.png" alt="Bahasa Indonesia" style="height:14px;"> [Bahasa Indonesia](docs/translation/id/README.md) · <img src="https://flagcdn.com/w20/jp.png" alt="日本語" style="height:14px;"> [日本語](docs/translation/ja/README.md) · <img src="https://flagcdn.com/w20/kr.png" alt="한국어" style="height:14px;"> [한국어](docs/translation/ko/README.md) · <img src="https://flagcdn.com/w20/in.png" alt="हिन्दी" style="height:14px;"> [हिन्दी](docs/translation/hi/README.md) · <img src="https://flagcdn.com/w20/ae.png" alt="العربية" style="height:14px;"> [العربية](docs/translation/ar/README.md)

---
**Omega-Suite** est une Interface unifiee de la suite des outils scanners **omega-** :  
[omega-scan](https://github.com/kraynux/omega-scan), [omega-check](https://github.com/kraynux/omega-check), [omega-deep](https://github.com/kraynux/omega-deep), [omega-fold](https://github.com/kraynux/omega-fold), [omega-stress](https://github.com/kraynux/omega-stress), [omega-track](https://github.com/kraynux/omega-track) et [omega-fuzz](https://github.com/kraynux/omega-fuzz)  
reunis dans une seule application TUI (grille d'Accueil ou barre d'onglets persistante, selon le choix de l'utilisateur) avec une bibliotheque partagee [(`omega-lib`)](https://github.com/kraynux/omega-lib).


Chaque outil reste executable de facon autonome (`omega-check scan ...`
fonctionne toujours) - omega-suite est une facade additionnelle, pas un
remplacement.

Voir `~/DEV/SUITE/OMEGA-SUITE_SPECIFICATIONS.md` et
`~/DEV/SUITE/DECISIONS_ARCHITECTURE.md` (D-014/D-015) pour le detail des
choix d'architecture et d'ergonomie.

## Présentation

Omega-Suite agit comme un **poste de pilotage** des scanners Omega pour la sécurité réseau

### Objectifs

- Réunir les 7 outils **scanners omega** dans une interface cohérente, sans jamais les modifier ni les remplacer.
- Un seul thème, un seul profil de rendu, un seul style de navigation pour les 7 outils - configurés une fois, plutôt que 7 fois.
- Passer d'un outil à l'autre sans perdre son contexte : chaque pile d'écrans reste intacte en arrière-plan.
- Rester léger malgré les 7 outils réunis : rien n'est chargé en mémoire avant sa première ouverture réelle.

## Fonctionnalités

- **Une seule application TUI** (Textual) pour Omega-SCAN, -CHECK, -DEEP, -FOLD, -STRESS, -TRACK et -FUZZ.
- **Deux styles de navigation** au choix (Réglages, redémarrage proposé immédiatement) : grille de boutons depuis Accueil, ou barre d'onglets persistante visible même en profondeur (Historique, Réglages d'un outil...), sans jamais repasser par Accueil.
- **Chargement paresseux** : chaque outil (code Python et dépendances) n'est importé qu'à sa toute première ouverture dans la session - le temps de démarrage et la mémoire restent proportionnels aux outils réellement utilisés.
- **Thème et profil de rendu partagés** : le thème change à chaud pour les 7 outils à la fois ; profil de rendu et style de navigation, plus structurels, proposent de redémarrer omega-suite tout de suite.
- **Aide contextuelle** : raccourcis globaux et panorama du périmètre des 7 outils depuis Accueil, aide propre à l'outil actif depuis un onglet.
- **Purge globale des exports** des 7 outils en un clic (Réglages de la suite), même pour ceux jamais ouverts dans la session.
- **Isolation stricte entre les 7 outils** malgré le partage d'une seule application : aucune fuite de style ni d'état d'un outil à l'autre.
- **Chaque outil reste utilisable en autonomie complète** (TUI et CLI propres, `omega-check scan ...` fonctionne toujours) - omega-suite n'en est qu'une façade additionnelle, jamais un remplacement.

## Installation

L'archive officielle est fournie au format `.tar.gz`. Vérifiez son intégrité avant installation :

```bash
sha256sum omega-suite.tar.gz
```

```bash
./install.sh
./omega-suite.sh
```


## Utilisation
### Lancement

```bash
cd ~/omega-suite
./omega-suite.sh
```

###  ou simplement, si l'alias a été créé dans le terminal taper  :
```bash
suite
```
## Langues de l'interface

L'interface est disponible en 17 langues. Le choix se fait dans les Réglages de la suite (« Langue / Language ») et s'applique aux 7 outils après un redémarrage de l'interface ; la variable `OMEGA_SUITE_LANG` permet de forcer une langue le temps d'une session. Un réglage séparé, « Langue des exports », fixe la langue des rapports exportés par les 7 outils. Sur une console texte Linux (TTY), les langues à écriture non latine s'affichent en anglais pour la session. La ligne de commande reste en français.

## Compatibilité terminaux

L'interface interactive (Textual) détecte automatiquement les capacités du terminal (émulateur, taille) et adapte sa feuille de style structurelle en conséquence (`complete`/`standard`/`reduced`/`mono`), sans flag manuel. Le mode CLI reste toujours en texte simple, indépendant du terminal. Politique partagée par toute la suite `omega-` (`omega-lib`, `terminal/policies.py`) — identique à celle d'`omega-check`/`omega-fire`.

### Profil selon l'émulateur détecté

| Émulateur | Profil initial |
|---|---|
| Ghostty, Alacritty, WezTerm, Kitty | `complete` |
| Konsole, GNOME Terminal, Terminator, Xfce4 Terminal | `standard` |
| xterm, urxvt, SSH moderne | `reduced` |
| TTY Linux, SSH ancien | `mono` |
| Émulateur non reconnu | `reduced` (repli par défaut) |

### Profil selon la taille du terminal

| Taille minimale (colonnes × lignes) | Plafond de profil |
|---|---|
| 120 × 32 | `complete` |
| 100 × 28 | `standard` |
| 80 × 24 | `reduced` |
| en dessous | `mono` |

Le profil final retenu est **le plus restrictif des deux** (émulateur et taille) — un Ghostty en plein écran redimensionné à 70 colonnes redescend en `mono`, même si son émulateur autoriserait `complete`. Rafraîchissable en direct par la touche `r`, ou surchargeable manuellement depuis les Réglages de la suite (touche `s`).

## Architecture

### Principes de conception

- **Façade de composition, jamais une 8e couche métier** : omega-suite n'a pas de `domain/` propre - il assemble les 7 conteneurs déjà validés indépendamment par chaque projet, sans en réimplémenter la logique.
- **Aucun fichier des 7 outils n'est modifié.** Leurs classes d'écrans/widgets partagés sont patchées en mémoire, une seule fois, à la première ouverture réelle de cet outil dans la session : isolation CSS (un outil ne peut jamais hériter du style d'un autre), redirection du « Quitter » interne de l'outil vers l'onglet Accueil de la suite, et injection de la barre d'onglets si ce style de navigation est actif.
- **`textual` interdit hors de `interfaces/tui/`** (vérifié par `import-linter` à chaque modification) : `app/` reste indépendant de l'affichage, et pourrait en théorie servir une autre interface.
- **Construction paresseuse à deux niveaux** : l'adaptateur d'un outil (import de son code), puis son conteneur (base SQLite, sondes réseau) - aucun des deux n'est payé avant la première visite réelle de cet outil précis.

### Structure des données

```text
src/omega_suite/
├── app/              Assemblage : DependencyContainer paresseux, bootstrap, adaptateurs des 7 outils
│                     (tool_adapters.py), réglages partagés (thème, profil de rendu, style de navigation)
├── infrastructure/   Chemins runtime (var/), stockage des réglages (JSON)
├── interfaces/
│   ├── tui/          Seul endroit qui importe Textual : App, écrans propres à la suite (Accueil, Réglages,
│   │                 Aide, Splash), patch en mémoire des écrans des 7 outils (screen_patching.py)
│   └── cli/          Réservé, vide à ce jour - chaque outil garde son propre mode CLI, invoqué directement
└── ports/            Contrats attendus par app/ (SettingsStore)
```

## Prérequis

### Système

- Python 3.10+
- Linux (Textual fonctionne sur d'autres systèmes, non testés ni supportés par ce projet)
- Un terminal, quel qu'il soit - ses capacités réelles sont détectées automatiquement et le rendu s'y adapte (voir « Compatibilité terminaux » ci-dessus), jusqu'à une simple TTY

### Dépendances Python

Déclarées dans `pyproject.toml`, un seul environnement virtuel les réunit toutes (voir `install.sh`) :

- `omega-lib` : bibliothèque partagée (thèmes, détection de terminal, niveaux de confiance)
- `omega-scan`, `omega-check`, `omega-deep`, `omega-fold`, `omega-stress`, `omega-track`, `omega-fuzz` : les 7 outils intégrés, chacun avec ses propres dépendances transitives
- `textual` : interface TUI
- Dépendances de développement (`pip install -e ".[dev]"`) : `pytest`, `pytest-asyncio`, `pytest-cov`, `ruff`, `mypy`, `import-linter`

### Exports

Chaque outil écrit ses propres exports sous `var/<outil>/exports/` et ses captures d'écran sous `var/<outil>/screenshots/` - `var/` relatif au dossier où omega-suite a été lancé, ou `$OMEGA_SUITE_VAR_DIR` pour le surcharger. Ce n'est jamais le `var/` par défaut de l'outil lancé seul : les deux usages (autonome ou intégré à la suite) ne se mélangent jamais. Chaque outil peut redéfinir son propre dossier de destination depuis ses propres Réglages. Le bouton « Vider tous les exports » (Réglages de la suite) vide ce dossier pour les 7 outils d'un coup, même ceux jamais ouverts dans la session - voir l'Aide de la suite (touche `a` depuis Accueil) pour le détail.

---

## Sécurité

- omega-suite lui-même ne fait aucune requête réseau et ne scanne rien : il orchestre l'affichage des 7 outils, chacun garde intégralement ses propres garde-fous (voir leur périmètre respectif dans l'Aide de la suite, ou leur propre README).
- Aucun secret ni identifiant n'est manipulé par omega-suite lui-même. Ce que chaque outil stocke (cibles épinglées, historique, réglages propres) reste sous son propre sous-dossier `var/<outil>/`, inchangé par la suite.
- Le seul état propre à omega-suite (thème, profil de rendu, style de navigation) vit dans `var/settings.json`, sans donnée sensible.
- `import-linter` interdit tout import de `textual` en dehors de `interfaces/tui/` à chaque modification (voir Architecture) - une garantie structurelle, pas une simple convention.

## Tests et qualité

```bash
source .venv/bin/activate
pip install -e ".[dev]"
lint-imports        # verifie la Dependency Rule (textual hors de interfaces/tui interdit)
pytest -q
ruff check src tests
mypy -p omega_suite
```

## Désinstallation

omega-suite ne touche rien en dehors de son propre dossier et de l'alias de lancement :

1. Retirer la ligne `alias suite="..."` ajoutée par `install.sh` dans `~/.bashrc` et `~/.zshrc`.
2. Supprimer le dossier `omega-suite/` (environnement virtuel `.venv/`, données `var/` et réglages inclus).

Les 7 outils installés séparément (ou en développement dans leurs propres dossiers) ne sont pas affectés : chacun reste installable/désinstallable indépendamment, en suivant son propre README.

## Licence

Omega-Suite est distribué sous licence **MIT**. Consultez le fichier [`LICENSE`](LICENSE) pour le texte complet.

---

> **Omega-Suite — Observer, piloter, auditer, pour mieux sécuriser.**
>
> Une interface TUI unifiée pour les scanners Omega-
