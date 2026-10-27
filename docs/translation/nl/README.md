<!-- Copyright (c) 2026 kraynux - kraynux@proton.me - Licence MIT (voir fichier LICENSE) -->
<div align="center">
  <img src="https://raw.githubusercontent.com/kraynux/kraynux/refs/heads/main/docs/assets/omega-suite.png" alt="Omega-Suite" width="384">
</div>


#  OMEGA-SUITE

**Alle "OMEGA"-scanners samengebracht in één interface en een gedeelde bibliotheek**

> Ontwikkeld door **kraynux** voor **Omega-server** 
[kraynux.snake-mackarel](https://kraynux.snake-mackarel.ts.net)

Officiële pagina: [OMEGA-SUITE](https://kraynux.snake-mackarel.ts.net/omega-suite/) &nbsp;   
Schermafbeeldingen → [omega-scan](https://kraynux.snake-mackarel.ts.net/omega-scan/screenshots/) · [omega-check](https://kraynux.snake-mackarel.ts.net/omega-check/screenshots/) · [omega-deep](https://kraynux.snake-mackarel.ts.net/omega-deep/screenshots/) · [omega-fold](https://kraynux.snake-mackarel.ts.net/omega-fold/screenshots/) · [omega-track](https://kraynux.snake-mackarel.ts.net/omega-track/screenshots/) · [omega-fuzz](https://kraynux.snake-mackarel.ts.net/omega-fuzz/screenshots/) · [omega-stress](https://kraynux.snake-mackarel.ts.net/omega-stress/screenshots/) 

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../../LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux-informational.svg)](https://www.linux.org/)
[![Interface](https://img.shields.io/badge/Interface-Textual%20TUI-cyan.svg)](https://github.com/Textualize/textual)

**Talen:**
<img src="https://flagcdn.com/w20/fr.png" alt="France" style="height:14px;"> [Français](../../../README.md) · <img src="https://flagcdn.com/w20/gb.png" alt="English" style="height:14px;"> [English](../en/README.md) · <img src="https://flagcdn.com/w20/es.png" alt="Español" style="height:14px;"> [Español](../es/README.md) · <img src="https://flagcdn.com/w20/br.png" alt="Português (Brasil)" style="height:14px;"> [Português (Brasil)](../pt-BR/README.md) · <img src="https://flagcdn.com/w20/it.png" alt="Italiano" style="height:14px;"> [Italiano](../it/README.md) · <img src="https://flagcdn.com/w20/de.png" alt="Deutsch" style="height:14px;"> [Deutsch](../de/README.md) · <img src="https://flagcdn.com/w20/nl.png" alt="Nederlands" style="height:14px;"> [Nederlands](README.md) · <img src="https://flagcdn.com/w20/pl.png" alt="Polski" style="height:14px;"> [Polski](../pl/README.md) · <img src="https://flagcdn.com/w20/ru.png" alt="Русский" style="height:14px;"> [Русский](../ru/README.md) · <img src="https://flagcdn.com/w20/cn.png" alt="中文" style="height:14px;"> [中文](../zh-CN/README.md) · <img src="https://flagcdn.com/w20/vn.png" alt="Tiếng Việt" style="height:14px;"> [Tiếng Việt](../vi/README.md) · <img src="https://flagcdn.com/w20/th.png" alt="ไทย" style="height:14px;"> [ไทย](../th/README.md) · <img src="https://flagcdn.com/w20/id.png" alt="Bahasa Indonesia" style="height:14px;"> [Bahasa Indonesia](../id/README.md) · <img src="https://flagcdn.com/w20/jp.png" alt="日本語" style="height:14px;"> [日本語](../ja/README.md) · <img src="https://flagcdn.com/w20/kr.png" alt="한국어" style="height:14px;"> [한국어](../ko/README.md) · <img src="https://flagcdn.com/w20/in.png" alt="हिन्दी" style="height:14px;"> [हिन्दी](../hi/README.md) · <img src="https://flagcdn.com/w20/ae.png" alt="العربية" style="height:14px;"> [العربية](../ar/README.md)

---
**Omega-Suite** is een geïntegreerde interface voor de scannerhulpmiddelen van de **omega-**-suite:  
[omega-scan](https://github.com/kraynux/omega-scan), [omega-check](https://github.com/kraynux/omega-check), [omega-deep](https://github.com/kraynux/omega-deep), [omega-fold](https://github.com/kraynux/omega-fold), [omega-stress](https://github.com/kraynux/omega-stress), [omega-track](https://github.com/kraynux/omega-track) en [omega-fuzz](https://github.com/kraynux/omega-fuzz)  
samengebracht in één TUI-toepassing (raster op het startscherm of blijvende tabbalk, naar keuze van de gebruiker) met een gedeelde bibliotheek [(`omega-lib`)](https://github.com/kraynux/omega-lib).


Elk hulpmiddel blijft zelfstandig uitvoerbaar (`omega-check scan ...`
werkt nog steeds) - omega-suite is een extra façade, geen
vervanging.

Zie `~/DEV/SUITE/OMEGA-SUITE_SPECIFICATIONS.md` en
`~/DEV/SUITE/DECISIONS_ARCHITECTURE.md` (D-014/D-015) voor de details van de
keuzes op het gebied van architectuur en ergonomie.

## Presentatie

Omega-Suite fungeert als **bedieningspost** van de Omega-scanners voor netwerkbeveiliging

### Doelstellingen

- De 7 **omega-scanners** samenbrengen in één samenhangende interface, zonder ze ooit te wijzigen of te vervangen.
- Eén thema, één weergaveprofiel, één navigatiestijl voor de 7 hulpmiddelen - één keer ingesteld in plaats van 7 keer.
- Van het ene hulpmiddel naar het andere gaan zonder de context te verliezen: elke schermstapel blijft op de achtergrond intact.
- Licht blijven ondanks de 7 samengebrachte hulpmiddelen: niets wordt in het geheugen geladen vóór de eerste echte opening.

## Functies

- **Eén TUI-toepassing** (Textual) voor Omega-SCAN, -CHECK, -DEEP, -FOLD, -STRESS, -TRACK en -FUZZ.
- **Twee navigatiestijlen** naar keuze (Instellingen, herstart wordt meteen voorgesteld): knoppenraster vanaf het startscherm, of blijvende tabbalk die ook dieper zichtbaar blijft (Geschiedenis, Instellingen van een hulpmiddel...), zonder ooit terug te hoeven naar het startscherm.
- **Lui laden**: elk hulpmiddel (Python-code en afhankelijkheden) wordt pas bij de allereerste opening in de sessie geïmporteerd - opstarttijd en geheugengebruik blijven evenredig aan de werkelijk gebruikte hulpmiddelen.
- **Gedeeld thema en weergaveprofiel**: het thema wisselt live voor alle 7 hulpmiddelen tegelijk; weergaveprofiel en navigatiestijl, die structureler zijn, stellen voor omega-suite meteen te herstarten.
- **Contextuele hulp**: globale sneltoetsen en overzicht van de reikwijdte van de 7 hulpmiddelen vanaf het startscherm, eigen hulp van het actieve hulpmiddel vanuit een tab.
- **Globaal leegmaken van de exports** van de 7 hulpmiddelen met één klik (Instellingen van de suite), ook van die nooit in de sessie zijn geopend.
- **Strikte isolatie tussen de 7 hulpmiddelen** ondanks het delen van één toepassing: geen lekken van stijl of toestand van het ene hulpmiddel naar het andere.
- **Elk hulpmiddel blijft volledig zelfstandig bruikbaar** (eigen TUI en CLI, `omega-check scan ...` werkt nog steeds) - omega-suite is er slechts een extra façade voor, nooit een vervanging.

## Installatie

Het officiële archief wordt geleverd in `.tar.gz`-formaat. Controleer de integriteit vóór de installatie:

```bash
sha256sum omega-suite.tar.gz
```

```bash
./install.sh
./omega-suite.sh
```


## Gebruik
### Starten

```bash
cd ~/omega-suite
./omega-suite.sh
```

###  of eenvoudig, als de alias is aangemaakt, typ in de terminal:
```bash
suite
```
## Terminalcompatibiliteit

De interactieve interface (Textual) detecteert automatisch de mogelijkheden van de terminal (emulator, grootte) en past haar structurele stylesheet daarop aan (`complete`/`standard`/`reduced`/`mono`), zonder handmatige vlag. De CLI-modus blijft altijd platte tekst, onafhankelijk van de terminal. Beleid dat door de hele `omega-`-suite wordt gedeeld (`omega-lib`, `terminal/policies.py`) — identiek aan dat van `omega-check`/`omega-fire`.

### Profiel volgens de gedetecteerde emulator

| Emulator | Beginprofiel |
|---|---|
| Ghostty, Alacritty, WezTerm, Kitty | `complete` |
| Konsole, GNOME Terminal, Terminator, Xfce4 Terminal | `standard` |
| xterm, urxvt, moderne SSH | `reduced` |
| Linux-TTY, oude SSH | `mono` |
| Niet-herkende emulator | `reduced` (standaardterugval) |

### Profiel volgens de terminalgrootte

| Minimale grootte (kolommen × regels) | Profielplafond |
|---|---|
| 120 × 32 | `complete` |
| 100 × 28 | `standard` |
| 80 × 24 | `reduced` |
| kleiner | `mono` |

Het uiteindelijk gekozen profiel is **het meest beperkende van de twee** (emulator en grootte) — een Ghostty op volledig scherm die naar 70 kolommen wordt verkleind, valt terug naar `mono`, ook al zou de emulator `complete` toestaan. Live te vernieuwen met de toets `r`, of handmatig te overschrijven in de Instellingen van de suite (toets `s`).

## Architectuur

### Ontwerpprincipes

- **Compositiefaçade, nooit een 8e bedrijfslaag**: omega-suite heeft geen eigen `domain/` - het zet de 7 containers samen die elk project al onafhankelijk heeft gevalideerd, zonder hun logica opnieuw te implementeren.
- **Geen enkel bestand van de 7 hulpmiddelen wordt gewijzigd.** Hun gedeelde scherm-/widgetklassen worden in het geheugen gepatcht, één keer, bij de eerste echte opening van dat hulpmiddel in de sessie: CSS-isolatie (een hulpmiddel kan nooit de stijl van een ander erven), omleiding van het interne « Afsluiten » van het hulpmiddel naar de starttab van de suite, en invoegen van de tabbalk als die navigatiestijl actief is.
- **`textual` verboden buiten `interfaces/tui/`** (bij elke wijziging gecontroleerd door `import-linter`): `app/` blijft onafhankelijk van de weergave en zou in theorie een andere interface kunnen bedienen.
- **Lui opbouwen op twee niveaus**: de adapter van een hulpmiddel (import van zijn code), daarna zijn container (SQLite-database, netwerksondes) - geen van beide wordt betaald vóór het eerste echte bezoek aan precies dat hulpmiddel.

### Gegevensstructuur

```text
src/omega_suite/
├── app/              Samenstelling: luie DependencyContainer, bootstrap, adapters van de 7 hulpmiddelen
│                     (tool_adapters.py), gedeelde instellingen (thema, weergaveprofiel, navigatiestijl)
├── infrastructure/   Runtimepaden (var/), opslag van de instellingen (JSON)
├── interfaces/
│   ├── tui/          Enige plek die Textual importeert: App, eigen schermen van de suite (Start, Instellingen,
│   │                 Hulp, Splash), patch in het geheugen van de schermen van de 7 hulpmiddelen (screen_patching.py)
│   └── cli/          Gereserveerd, tot nu toe leeg - elk hulpmiddel behoudt zijn eigen CLI-modus, rechtstreeks aangeroepen
└── ports/            Contracten die app/ verwacht (SettingsStore)
```

## Vereisten

### Systeem

- Python 3.10+
- Linux (Textual werkt op andere systemen, die door dit project niet getest of ondersteund worden)
- Een terminal, welke dan ook - de werkelijke mogelijkheden worden automatisch gedetecteerd en de weergave past zich aan (zie « Terminalcompatibiliteit » hierboven), tot een eenvoudige TTY toe

### Python-afhankelijkheden

Gedeclareerd in `pyproject.toml`, één virtuele omgeving brengt ze allemaal samen (zie `install.sh`):

- `omega-lib`: gedeelde bibliotheek (thema's, terminaldetectie, betrouwbaarheidsniveaus)
- `omega-scan`, `omega-check`, `omega-deep`, `omega-fold`, `omega-stress`, `omega-track`, `omega-fuzz`: de 7 geïntegreerde hulpmiddelen, elk met zijn eigen transitieve afhankelijkheden
- `textual`: TUI-interface
- Ontwikkelafhankelijkheden (`pip install -e ".[dev]"`): `pytest`, `pytest-asyncio`, `pytest-cov`, `ruff`, `mypy`, `import-linter`

### Exports

Elk hulpmiddel schrijft zijn eigen exports naar `var/<hulpmiddel>/exports/` en zijn schermafbeeldingen naar `var/<hulpmiddel>/screenshots/` - `var/` relatief ten opzichte van de map waarin omega-suite is gestart, of `$OMEGA_SUITE_VAR_DIR` om dat te overschrijven. Het is nooit de standaard-`var/` van het hulpmiddel dat alleen wordt gestart: de twee vormen van gebruik (zelfstandig of geïntegreerd in de suite) raken nooit vermengd. Elk hulpmiddel kan zijn eigen doelmap opnieuw instellen in zijn eigen Instellingen. De knop « Alle exports leegmaken » (Instellingen van de suite) maakt deze map voor alle 7 hulpmiddelen tegelijk leeg, ook voor die nooit in de sessie zijn geopend - zie de Hulp van de suite (toets `a` vanaf het startscherm) voor de details.

---

## Beveiliging

- omega-suite zelf doet geen enkel netwerkverzoek en scant niets: het orkestreert de weergave van de 7 hulpmiddelen, die elk hun eigen beveiligingen volledig behouden (zie hun respectieve reikwijdte in de Hulp van de suite, of in hun eigen README).
- Geen enkel geheim of identificatiegegeven wordt door omega-suite zelf verwerkt. Wat elk hulpmiddel opslaat (vastgezette doelen, geschiedenis, eigen instellingen) blijft in zijn eigen submap `var/<hulpmiddel>/`, onveranderd door de suite.
- De enige eigen toestand van omega-suite (thema, weergaveprofiel, navigatiestijl) staat in `var/settings.json`, zonder gevoelige gegevens.
- `import-linter` verbiedt bij elke wijziging elke import van `textual` buiten `interfaces/tui/` (zie Architectuur) - een structurele garantie, geen loutere afspraak.

## Tests en kwaliteit

```bash
source .venv/bin/activate
pip install -e ".[dev]"
lint-imports        # controleert de Dependency Rule (textual buiten interfaces/tui verboden)
pytest -q
ruff check src tests
mypy -p omega_suite
```

## Verwijderen

omega-suite raakt niets aan buiten zijn eigen map en de start-alias:

1. De regel `alias suite="..."` verwijderen die `install.sh` aan `~/.bashrc` en `~/.zshrc` heeft toegevoegd.
2. De map `omega-suite/` verwijderen (virtuele omgeving `.venv/`, gegevens `var/` en instellingen inbegrepen).

De 7 apart geïnstalleerde hulpmiddelen (of die in ontwikkeling in hun eigen mappen) worden niet geraakt: elk blijft zelfstandig te installeren/verwijderen, volgens zijn eigen README.

## Licentie

Omega-Suite wordt verspreid onder de **MIT**-licentie. Zie het bestand [`LICENSE`](../../../LICENSE) voor de volledige tekst.

---

> **Omega-Suite — Observeren, besturen, auditen, om beter te beveiligen.**
>
> Een geïntegreerde TUI-interface voor de Omega-scanners
