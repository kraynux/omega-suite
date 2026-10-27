<!-- Copyright (c) 2026 kraynux - kraynux@proton.me - Licence MIT (voir fichier LICENSE) -->
<div align="center">
  <img src="https://raw.githubusercontent.com/kraynux/kraynux/refs/heads/main/docs/assets/omega-suite.png" alt="Omega-Suite" width="384">
</div>


#  OMEGA-SUITE

**Alle "OMEGA"-Scanner vereint in einer einzigen Oberfläche und einer gemeinsamen Bibliothek**

> Entwickelt von **kraynux** für **Omega-server** 
[kraynux.snake-mackarel](https://kraynux.snake-mackarel.ts.net)

Offizielle Seite: [OMEGA-SUITE](https://kraynux.snake-mackarel.ts.net/omega-suite/) &nbsp;   
Screenshots → [omega-scan](https://kraynux.snake-mackarel.ts.net/omega-scan/screenshots/) · [omega-check](https://kraynux.snake-mackarel.ts.net/omega-check/screenshots/) · [omega-deep](https://kraynux.snake-mackarel.ts.net/omega-deep/screenshots/) · [omega-fold](https://kraynux.snake-mackarel.ts.net/omega-fold/screenshots/) · [omega-track](https://kraynux.snake-mackarel.ts.net/omega-track/screenshots/) · [omega-fuzz](https://kraynux.snake-mackarel.ts.net/omega-fuzz/screenshots/) · [omega-stress](https://kraynux.snake-mackarel.ts.net/omega-stress/screenshots/) 

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../../LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux-informational.svg)](https://www.linux.org/)
[![Interface](https://img.shields.io/badge/Interface-Textual%20TUI-cyan.svg)](https://github.com/Textualize/textual)

**Sprachen:**
<img src="https://flagcdn.com/w20/fr.png" alt="France" style="height:14px;"> [Français](../../../README.md) · <img src="https://flagcdn.com/w20/gb.png" alt="English" style="height:14px;"> [English](../en/README.md) · <img src="https://flagcdn.com/w20/es.png" alt="Español" style="height:14px;"> [Español](../es/README.md) · <img src="https://flagcdn.com/w20/br.png" alt="Português (Brasil)" style="height:14px;"> [Português (Brasil)](../pt-BR/README.md) · <img src="https://flagcdn.com/w20/it.png" alt="Italiano" style="height:14px;"> [Italiano](../it/README.md) · <img src="https://flagcdn.com/w20/de.png" alt="Deutsch" style="height:14px;"> [Deutsch](README.md) · <img src="https://flagcdn.com/w20/nl.png" alt="Nederlands" style="height:14px;"> [Nederlands](../nl/README.md) · <img src="https://flagcdn.com/w20/pl.png" alt="Polski" style="height:14px;"> [Polski](../pl/README.md) · <img src="https://flagcdn.com/w20/ru.png" alt="Русский" style="height:14px;"> [Русский](../ru/README.md) · <img src="https://flagcdn.com/w20/cn.png" alt="中文" style="height:14px;"> [中文](../zh-CN/README.md) · <img src="https://flagcdn.com/w20/vn.png" alt="Tiếng Việt" style="height:14px;"> [Tiếng Việt](../vi/README.md) · <img src="https://flagcdn.com/w20/th.png" alt="ไทย" style="height:14px;"> [ไทย](../th/README.md) · <img src="https://flagcdn.com/w20/id.png" alt="Bahasa Indonesia" style="height:14px;"> [Bahasa Indonesia](../id/README.md) · <img src="https://flagcdn.com/w20/jp.png" alt="日本語" style="height:14px;"> [日本語](../ja/README.md) · <img src="https://flagcdn.com/w20/kr.png" alt="한국어" style="height:14px;"> [한국어](../ko/README.md) · <img src="https://flagcdn.com/w20/in.png" alt="हिन्दी" style="height:14px;"> [हिन्दी](../hi/README.md) · <img src="https://flagcdn.com/w20/ae.png" alt="العربية" style="height:14px;"> [العربية](../ar/README.md)

---
**Omega-Suite** ist eine einheitliche Oberfläche für die Scanner-Werkzeuge der **omega-**-Suite:  
[omega-scan](https://github.com/kraynux/omega-scan), [omega-check](https://github.com/kraynux/omega-check), [omega-deep](https://github.com/kraynux/omega-deep), [omega-fold](https://github.com/kraynux/omega-fold), [omega-stress](https://github.com/kraynux/omega-stress), [omega-track](https://github.com/kraynux/omega-track) und [omega-fuzz](https://github.com/kraynux/omega-fuzz)  
vereint in einer einzigen TUI-Anwendung (Raster auf dem Startbildschirm oder dauerhafte Tab-Leiste, je nach Wahl des Benutzers) mit einer gemeinsamen Bibliothek [(`omega-lib`)](https://github.com/kraynux/omega-lib).


Jedes Werkzeug bleibt eigenständig ausführbar (`omega-check scan ...`
funktioniert weiterhin) - omega-suite ist eine zusätzliche Fassade, kein
Ersatz.

Siehe `~/DEV/SUITE/OMEGA-SUITE_SPECIFICATIONS.md` und
`~/DEV/SUITE/DECISIONS_ARCHITECTURE.md` (D-014/D-015) für die Details der
Architektur- und Ergonomieentscheidungen.

## Vorstellung

Omega-Suite dient als **Leitstand** der Omega-Scanner für die Netzwerksicherheit

### Ziele

- Die 7 **omega-Scanner** in einer stimmigen Oberfläche vereinen, ohne sie je zu ändern oder zu ersetzen.
- Ein einziges Theme, ein einziges Darstellungsprofil, ein einziger Navigationsstil für die 7 Werkzeuge - einmal konfiguriert statt 7-mal.
- Von einem Werkzeug zum anderen wechseln, ohne den Kontext zu verlieren: Jeder Bildschirmstapel bleibt im Hintergrund erhalten.
- Trotz der 7 vereinten Werkzeuge schlank bleiben: Nichts wird vor dem ersten tatsächlichen Öffnen in den Speicher geladen.

## Funktionen

- **Eine einzige TUI-Anwendung** (Textual) für Omega-SCAN, -CHECK, -DEEP, -FOLD, -STRESS, -TRACK und -FUZZ.
- **Zwei Navigationsstile** zur Wahl (Einstellungen, Neustart wird sofort angeboten): Schaltflächenraster vom Startbildschirm aus oder dauerhafte Tab-Leiste, die auch in tieferen Ebenen sichtbar bleibt (Verlauf, Einstellungen eines Werkzeugs...), ohne je über den Startbildschirm zurückzumüssen.
- **Verzögertes Laden**: Jedes Werkzeug (Python-Code und Abhängigkeiten) wird erst beim allerersten Öffnen in der Sitzung importiert - Startzeit und Speicherbedarf bleiben proportional zu den tatsächlich genutzten Werkzeugen.
- **Gemeinsames Theme und Darstellungsprofil**: Das Theme wechselt im laufenden Betrieb für alle 7 Werkzeuge zugleich; Darstellungsprofil und Navigationsstil, eher struktureller Natur, bieten einen sofortigen Neustart von omega-suite an.
- **Kontextbezogene Hilfe**: globale Tastenkürzel und Überblick über den Umfang der 7 Werkzeuge vom Startbildschirm aus, eigene Hilfe des aktiven Werkzeugs aus einem Tab.
- **Globales Leeren der Exporte** aller 7 Werkzeuge mit einem Klick (Einstellungen der Suite), auch von solchen, die in der Sitzung nie geöffnet wurden.
- **Strikte Isolation zwischen den 7 Werkzeugen** trotz gemeinsamer Anwendung: kein Durchsickern von Stil oder Zustand von einem Werkzeug zum anderen.
- **Jedes Werkzeug bleibt vollständig eigenständig nutzbar** (eigene TUI und CLI, `omega-check scan ...` funktioniert weiterhin) - omega-suite ist nur eine zusätzliche Fassade, nie ein Ersatz.

## Installation

Das offizielle Archiv wird im Format `.tar.gz` bereitgestellt. Prüfen Sie seine Integrität vor der Installation:

```bash
sha256sum omega-suite.tar.gz
```

```bash
./install.sh
./omega-suite.sh
```


## Verwendung
### Start

```bash
cd ~/omega-suite
./omega-suite.sh
```

###  oder einfach, wenn der Alias erstellt wurde, im Terminal eingeben:
```bash
suite
```
## Terminal-Kompatibilität

Die interaktive Oberfläche (Textual) erkennt automatisch die Fähigkeiten des Terminals (Emulator, Größe) und passt ihr strukturelles Stylesheet entsprechend an (`complete`/`standard`/`reduced`/`mono`), ohne manuelles Flag. Der CLI-Modus bleibt immer reiner Text, unabhängig vom Terminal. Von der gesamten `omega-`-Suite geteilte Richtlinie (`omega-lib`, `terminal/policies.py`) — identisch mit der von `omega-check`/`omega-fire`.

### Profil nach erkanntem Emulator

| Emulator | Anfangsprofil |
|---|---|
| Ghostty, Alacritty, WezTerm, Kitty | `complete` |
| Konsole, GNOME Terminal, Terminator, Xfce4 Terminal | `standard` |
| xterm, urxvt, modernes SSH | `reduced` |
| Linux-TTY, altes SSH | `mono` |
| Nicht erkannter Emulator | `reduced` (Standard-Rückfall) |

### Profil nach Terminalgröße

| Mindestgröße (Spalten × Zeilen) | Profilobergrenze |
|---|---|
| 120 × 32 | `complete` |
| 100 × 28 | `standard` |
| 80 × 24 | `reduced` |
| darunter | `mono` |

Das endgültig gewählte Profil ist **das restriktivere der beiden** (Emulator und Größe) — ein Ghostty im Vollbild, das auf 70 Spalten verkleinert wird, fällt auf `mono` zurück, auch wenn sein Emulator `complete` erlauben würde. Live aktualisierbar mit der Taste `r` oder manuell überschreibbar in den Einstellungen der Suite (Taste `s`).

## Architektur

### Gestaltungsprinzipien

- **Kompositionsfassade, nie eine 8. Fachschicht**: omega-suite hat kein eigenes `domain/` - es setzt die 7 Container zusammen, die jedes Projekt bereits unabhängig validiert hat, ohne deren Logik neu zu implementieren.
- **Keine Datei der 7 Werkzeuge wird geändert.** Ihre geteilten Bildschirm-/Widget-Klassen werden im Speicher gepatcht, ein einziges Mal, beim ersten tatsächlichen Öffnen dieses Werkzeugs in der Sitzung: CSS-Isolation (ein Werkzeug kann nie den Stil eines anderen erben), Umleitung des internen « Beenden » des Werkzeugs auf den Start-Tab der Suite und Einfügen der Tab-Leiste, wenn dieser Navigationsstil aktiv ist.
- **`textual` außerhalb von `interfaces/tui/` verboten** (bei jeder Änderung von `import-linter` geprüft): `app/` bleibt von der Anzeige unabhängig und könnte theoretisch eine andere Oberfläche bedienen.
- **Zweistufiger verzögerter Aufbau**: der Adapter eines Werkzeugs (Import seines Codes), dann sein Container (SQLite-Datenbank, Netzwerksonden) - keines von beiden wird vor dem ersten tatsächlichen Besuch genau dieses Werkzeugs bezahlt.

### Datenstruktur

```text
src/omega_suite/
├── app/              Zusammenbau: verzögerter DependencyContainer, Bootstrap, Adapter der 7 Werkzeuge
│                     (tool_adapters.py), gemeinsame Einstellungen (Theme, Darstellungsprofil, Navigationsstil)
├── infrastructure/   Laufzeitpfade (var/), Speicherung der Einstellungen (JSON)
├── interfaces/
│   ├── tui/          Einziger Ort, der Textual importiert: App, eigene Bildschirme der Suite (Start, Einstellungen,
│   │                 Hilfe, Splash), Patch der Bildschirme der 7 Werkzeuge im Speicher (screen_patching.py)
│   └── cli/          Reserviert, bisher leer - jedes Werkzeug behält seinen eigenen CLI-Modus, direkt aufgerufen
└── ports/            Von app/ erwartete Verträge (SettingsStore)
```

## Voraussetzungen

### System

- Python 3.10+
- Linux (Textual läuft auf anderen Systemen, die von diesem Projekt weder getestet noch unterstützt werden)
- Ein beliebiges Terminal - seine tatsächlichen Fähigkeiten werden automatisch erkannt und die Darstellung passt sich an (siehe « Terminal-Kompatibilität » oben), bis hin zu einem einfachen TTY

### Python-Abhängigkeiten

In `pyproject.toml` deklariert, eine einzige virtuelle Umgebung vereint sie alle (siehe `install.sh`):

- `omega-lib`: gemeinsame Bibliothek (Themes, Terminalerkennung, Vertrauensstufen)
- `omega-scan`, `omega-check`, `omega-deep`, `omega-fold`, `omega-stress`, `omega-track`, `omega-fuzz`: die 7 integrierten Werkzeuge, jedes mit seinen eigenen transitiven Abhängigkeiten
- `textual`: TUI-Oberfläche
- Entwicklungsabhängigkeiten (`pip install -e ".[dev]"`): `pytest`, `pytest-asyncio`, `pytest-cov`, `ruff`, `mypy`, `import-linter`

### Exporte

Jedes Werkzeug schreibt seine eigenen Exporte nach `var/<werkzeug>/exports/` und seine Screenshots nach `var/<werkzeug>/screenshots/` - `var/` relativ zum Ordner, aus dem omega-suite gestartet wurde, oder `$OMEGA_SUITE_VAR_DIR`, um es zu überschreiben. Es ist nie das Standard-`var/` des allein gestarteten Werkzeugs: Die beiden Nutzungen (eigenständig oder in die Suite integriert) vermischen sich nie. Jedes Werkzeug kann seinen eigenen Zielordner in seinen eigenen Einstellungen neu festlegen. Die Schaltfläche « Alle Exporte leeren » (Einstellungen der Suite) leert diesen Ordner für alle 7 Werkzeuge auf einmal, auch für die in der Sitzung nie geöffneten - Details in der Hilfe der Suite (Taste `a` vom Startbildschirm aus).

---

## Sicherheit

- omega-suite selbst stellt keinerlei Netzwerkanfragen und scannt nichts: Es orchestriert die Anzeige der 7 Werkzeuge, von denen jedes seine eigenen Schutzmechanismen vollständig behält (siehe deren jeweiligen Umfang in der Hilfe der Suite oder in ihrem eigenen README).
- Weder Geheimnisse noch Zugangsdaten werden von omega-suite selbst verarbeitet. Was jedes Werkzeug speichert (angeheftete Ziele, Verlauf, eigene Einstellungen), bleibt in seinem eigenen Unterordner `var/<werkzeug>/`, von der Suite unverändert.
- Der einzige eigene Zustand von omega-suite (Theme, Darstellungsprofil, Navigationsstil) liegt in `var/settings.json`, ohne sensible Daten.
- `import-linter` verbietet bei jeder Änderung jeden Import von `textual` außerhalb von `interfaces/tui/` (siehe Architektur) - eine strukturelle Garantie, keine bloße Konvention.

## Tests und Qualität

```bash
source .venv/bin/activate
pip install -e ".[dev]"
lint-imports        # prueft die Dependency Rule (textual ausserhalb von interfaces/tui verboten)
pytest -q
ruff check src tests
mypy -p omega_suite
```

## Deinstallation

omega-suite berührt nichts außerhalb seines eigenen Ordners und des Start-Alias:

1. Die von `install.sh` in `~/.bashrc` und `~/.zshrc` hinzugefügte Zeile `alias suite="..."` entfernen.
2. Den Ordner `omega-suite/` löschen (virtuelle Umgebung `.venv/`, Daten `var/` und Einstellungen eingeschlossen).

Die 7 separat installierten Werkzeuge (oder die in eigenen Ordnern in Entwicklung befindlichen) sind nicht betroffen: Jedes bleibt unabhängig installier-/deinstallierbar, gemäß seinem eigenen README.

## Lizenz

Omega-Suite wird unter der **MIT**-Lizenz verteilt. Den vollständigen Text finden Sie in der Datei [`LICENSE`](../../../LICENSE).

---

> **Omega-Suite — Beobachten, steuern, prüfen, um besser abzusichern.**
>
> Eine einheitliche TUI-Oberfläche für die Omega-Scanner
