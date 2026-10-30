<!-- Copyright (c) 2026 kraynux - kraynux@proton.me - MIT License (see LICENSE file) -->
<div align="center">
  <img src="https://raw.githubusercontent.com/kraynux/kraynux/refs/heads/main/docs/assets/omega-suite.png" alt="Omega-Suite" width="384">
</div>


#  OMEGA-SUITE

**The full set of "OMEGA" scanners reunified into a single interface and a shared library**

> Developed by **kraynux** for **Omega-server**
[kraynux.snake-mackarel](https://kraynux.snake-mackarel.ts.net)

Official page: [OMEGA-SUITE](https://kraynux.snake-mackarel.ts.net/omega-suite/) &nbsp;   
Screenshots → [omega-scan](https://kraynux.snake-mackarel.ts.net/omega-scan/screenshots/) · [omega-check](https://kraynux.snake-mackarel.ts.net/omega-check/screenshots/) · [omega-deep](https://kraynux.snake-mackarel.ts.net/omega-deep/screenshots/) · [omega-fold](https://kraynux.snake-mackarel.ts.net/omega-fold/screenshots/) · [omega-track](https://kraynux.snake-mackarel.ts.net/omega-track/screenshots/) · [omega-fuzz](https://kraynux.snake-mackarel.ts.net/omega-fuzz/screenshots/) · [omega-stress](https://kraynux.snake-mackarel.ts.net/omega-stress/screenshots/) 

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../../LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux-informational.svg)](https://www.linux.org/)
[![Interface](https://img.shields.io/badge/Interface-Textual%20TUI-cyan.svg)](https://github.com/Textualize/textual)

**Languages:**
<img src="https://flagcdn.com/w20/fr.png" alt="France" style="height:14px;"> [Français](../../../README.md) · <img src="https://flagcdn.com/w20/gb.png" alt="English" style="height:14px;"> [English](README.md) · <img src="https://flagcdn.com/w20/es.png" alt="Español" style="height:14px;"> [Español](../es/README.md) · <img src="https://flagcdn.com/w20/br.png" alt="Português (Brasil)" style="height:14px;"> [Português (Brasil)](../pt-BR/README.md) · <img src="https://flagcdn.com/w20/it.png" alt="Italiano" style="height:14px;"> [Italiano](../it/README.md) · <img src="https://flagcdn.com/w20/de.png" alt="Deutsch" style="height:14px;"> [Deutsch](../de/README.md) · <img src="https://flagcdn.com/w20/nl.png" alt="Nederlands" style="height:14px;"> [Nederlands](../nl/README.md) · <img src="https://flagcdn.com/w20/pl.png" alt="Polski" style="height:14px;"> [Polski](../pl/README.md) · <img src="https://flagcdn.com/w20/ru.png" alt="Русский" style="height:14px;"> [Русский](../ru/README.md) · <img src="https://flagcdn.com/w20/cn.png" alt="中文" style="height:14px;"> [中文](../zh-CN/README.md) · <img src="https://flagcdn.com/w20/vn.png" alt="Tiếng Việt" style="height:14px;"> [Tiếng Việt](../vi/README.md) · <img src="https://flagcdn.com/w20/th.png" alt="ไทย" style="height:14px;"> [ไทย](../th/README.md) · <img src="https://flagcdn.com/w20/id.png" alt="Bahasa Indonesia" style="height:14px;"> [Bahasa Indonesia](../id/README.md) · <img src="https://flagcdn.com/w20/jp.png" alt="日本語" style="height:14px;"> [日本語](../ja/README.md) · <img src="https://flagcdn.com/w20/kr.png" alt="한국어" style="height:14px;"> [한국어](../ko/README.md) · <img src="https://flagcdn.com/w20/in.png" alt="हिन्दी" style="height:14px;"> [हिन्दी](../hi/README.md) · <img src="https://flagcdn.com/w20/ae.png" alt="العربية" style="height:14px;"> [العربية](../ar/README.md)

---
**Omega-Suite** is a unified interface for the **omega-** scanner suite:  
[omega-scan](https://github.com/kraynux/omega-scan), [omega-check](https://github.com/kraynux/omega-check), [omega-deep](https://github.com/kraynux/omega-deep), [omega-fold](https://github.com/kraynux/omega-fold), [omega-stress](https://github.com/kraynux/omega-stress), [omega-track](https://github.com/kraynux/omega-track) and [omega-fuzz](https://github.com/kraynux/omega-fuzz)  
brought together in a single TUI application (Home grid or persistent tab bar, depending on the user's choice) with a shared library [(`omega-lib`)](https://github.com/kraynux/omega-lib).


Each tool remains fully usable on its own (`omega-check scan ...`
still works) - omega-suite is an additional facade, not a
replacement.

See `~/DEV/SUITE/OMEGA-SUITE_SPECIFICATIONS.md` and
`~/DEV/SUITE/DECISIONS_ARCHITECTURE.md` (D-014/D-015) for the details of
the architecture and ergonomics choices.

## Overview

Omega-Suite acts as a **control room** for the Omega scanners, for network security.

### Goals

- Bring the 7 **omega scanner** tools together in a coherent interface, without ever modifying or replacing them.
- One theme, one render profile, one navigation style for all 7 tools - configured once instead of 7 times.
- Switch from one tool to another without losing context: each screen stack stays intact in the background.
- Stay lightweight despite bundling 7 tools: nothing is loaded into memory before it is first opened.

## Features

- **A single TUI application** (Textual) for Omega-SCAN, -CHECK, -DEEP, -FOLD, -STRESS, -TRACK and -FUZZ.
- **Two navigation styles** to choose from (Settings, restart offered immediately) : button grid from Home, or a persistent tab bar visible even deep inside a tool (History, a tool's own Settings...), without ever going back through Home.
- **Lazy loading**: each tool's code and dependencies are only imported the first time it is opened in the session - startup time and memory stay proportional to the tools actually used.
- **Shared theme and render profile**: the theme changes live for all 7 tools at once; render profile and navigation style, being more structural, offer to restart omega-suite right away.
- **Contextual help**: global shortcuts and an overview of the 7 tools' scope from Home, the active tool's own help from a tab.
- **Global export purge** for all 7 tools in one click (Suite Settings), even for tools never opened in the session.
- **Strict isolation between the 7 tools** despite sharing a single application: no style or state leaks from one tool to another.
- **Each tool stays fully usable on its own** (its own TUI and CLI, `omega-check scan ...` still works) - omega-suite is only an additional facade, never a replacement.

## Installation

The official archive is provided as a `.tar.gz`. Verify its integrity before installing:

```bash
sha256sum omega-suite.tar.gz
```

```bash
./install.sh
./omega-suite.sh
```


## Usage
### Launch

```bash
cd ~/omega-suite
./omega-suite.sh
```

### or, if the alias was created, simply type in the terminal:
```bash
suite
```
## Interface languages

The interface is available in 17 languages. The choice is made in the suite Settings (“Langue / Language”) and applies to all 7 tools after the interface restarts; the `OMEGA_SUITE_LANG` variable forces a language for one session. A separate setting, “Export language”, sets the language of the reports exported by the 7 tools. On a Linux text console (TTY), languages with a non-Latin script are shown in English for the session. The command line stays in French.

## Terminal compatibility

The interactive interface (Textual) automatically detects the terminal's capabilities (emulator, size) and adapts its structural stylesheet accordingly (`complete`/`standard`/`reduced`/`mono`), without any manual flag. CLI mode always stays plain text, independent of the terminal. Policy shared by the whole `omega-` suite (`omega-lib`, `terminal/policies.py`) - identical to `omega-check`/`omega-fire`'s.

### Profile by detected emulator

| Emulator | Initial profile |
|---|---|
| Ghostty, Alacritty, WezTerm, Kitty | `complete` |
| Konsole, GNOME Terminal, Terminator, Xfce4 Terminal | `standard` |
| xterm, urxvt, modern SSH | `reduced` |
| Linux TTY, legacy SSH | `mono` |
| Unrecognized emulator | `reduced` (default fallback) |

### Profile by terminal size

| Minimum size (columns × rows) | Profile ceiling |
|---|---|
| 120 × 32 | `complete` |
| 100 × 28 | `standard` |
| 80 × 24 | `reduced` |
| below | `mono` |

The final profile retained is **the more restrictive of the two** (emulator and size) - a Ghostty running full-screen then resized to 70 columns falls back to `mono`, even though its emulator would allow `complete`. Refreshable live with the `r` key, or overridable manually from the suite's Settings (`s` key).

## Architecture

### Design principles

- **A composition facade, never an 8th business layer**: omega-suite has no `domain/` of its own - it assembles the 7 containers already validated independently by each project, without reimplementing their logic.
- **None of the 7 tools' files are modified.** Their shared screen/widget classes are patched in memory, once, the first time that tool is actually opened in the session: CSS isolation (a tool can never inherit another tool's style), redirecting the tool's own internal "Quit" to the suite's Home tab, and injecting the tab bar when that navigation style is active.
- **`textual` is forbidden outside `interfaces/tui/`** (checked by `import-linter` on every change): `app/` stays independent from the display layer, and could in principle serve another interface.
- **Two-level lazy construction**: a tool's adapter (importing its code), then its container (SQLite database, network probes) - neither is paid for before that specific tool's first real visit.

### Data structure

```text
src/omega_suite/
├── app/              Assembly: lazy DependencyContainer, bootstrap, the 7 tools' adapters
│                     (tool_adapters.py), shared settings (theme, render profile, navigation style)
├── infrastructure/   Runtime paths (var/), settings storage (JSON)
├── interfaces/
│   ├── tui/          The only place that imports Textual: App, the suite's own screens (Home, Settings,
│   │                 Help, Splash), in-memory patching of the 7 tools' screens (screen_patching.py)
│   └── cli/          Reserved, empty for now - each tool keeps its own CLI, invoked directly
└── ports/            Contracts expected by app/ (SettingsStore)
```

## Requirements

### System

- Python 3.10+
- Linux (Textual runs on other systems, neither tested nor supported by this project)
- Any terminal - its actual capabilities are detected automatically and rendering adapts accordingly (see "Terminal compatibility" above), down to a plain TTY

### Python dependencies

Declared in `pyproject.toml`, a single virtual environment brings them all together (see `install.sh`):

- `omega-lib`: shared library (themes, terminal detection, confidence levels)
- `omega-scan`, `omega-check`, `omega-deep`, `omega-fold`, `omega-stress`, `omega-track`, `omega-fuzz`: the 7 integrated tools, each with its own transitive dependencies
- `textual`: TUI interface
- Development dependencies (`pip install -e ".[dev]"`): `pytest`, `pytest-asyncio`, `pytest-cov`, `ruff`, `mypy`, `import-linter`

### Exports

Each tool writes its own exports under `var/<tool>/exports/` and its screenshots under `var/<tool>/screenshots/` - `var/` relative to the directory where omega-suite was launched, or `$OMEGA_SUITE_VAR_DIR` to override it. This is never the same `var/` a standalone tool would use by default: the two usages (standalone or bundled in the suite) never mix. Each tool can redefine its own destination folder from its own Settings. The "Clear all exports" button (Suite Settings) empties this folder for all 7 tools at once, even ones never opened in the session - see the suite's Help (`a` key from Home) for details.

---

## Security

- Omega-suite itself makes no network requests and scans nothing: it orchestrates the display of the 7 tools, each of which keeps its own safeguards fully intact (see each tool's own scope in the suite's Help, or its own README).
- No secret or credential is ever handled by omega-suite itself. Whatever each tool stores (pinned targets, history, its own settings) stays under its own `var/<tool>/` subfolder, untouched by the suite.
- The only state that belongs to omega-suite itself (theme, render profile, navigation style) lives in `var/settings.json`, with no sensitive data.
- `import-linter` forbids any `textual` import outside `interfaces/tui/` on every change (see Architecture) - a structural guarantee, not just a convention.

## Tests and code quality

```bash
source .venv/bin/activate
pip install -e ".[dev]"
lint-imports        # checks the Dependency Rule (textual forbidden outside interfaces/tui)
pytest -q
ruff check src tests
mypy -p omega_suite
```

## Uninstallation

omega-suite touches nothing outside its own folder and the launch alias:

1. Remove the `alias suite="..."` line added by `install.sh` from `~/.bashrc` and `~/.zshrc`.
2. Delete the `omega-suite/` folder (virtual environment `.venv/`, `var/` data and settings included).

The 7 tools installed separately (or in development in their own folders) are not affected: each one remains independently installable/uninstallable, following its own README.

## License

Omega-Suite is distributed under the **MIT** license. See the [`LICENSE`](../../../LICENSE) file for the full text.

---

> **Omega-Suite — Observe, drive, audit, secure better.**
>
> A unified TUI interface for the Omega- scanners
