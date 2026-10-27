<!-- Copyright (c) 2026 kraynux - kraynux@proton.me - Licence MIT (voir fichier LICENSE) -->
<div align="center">
  <img src="https://raw.githubusercontent.com/kraynux/kraynux/refs/heads/main/docs/assets/omega-suite.png" alt="Omega-Suite" width="384">
</div>


#  OMEGA-SUITE

**Wszystkie skanery "OMEGA" połączone w jednym interfejsie i wspólnej bibliotece**

> Opracowane przez **kraynux** dla **Omega-server** 
[kraynux.snake-mackarel](https://kraynux.snake-mackarel.ts.net)

Oficjalna strona: [OMEGA-SUITE](https://kraynux.snake-mackarel.ts.net/omega-suite/) &nbsp;   
Zrzuty ekranu → [omega-scan](https://kraynux.snake-mackarel.ts.net/omega-scan/screenshots/) · [omega-check](https://kraynux.snake-mackarel.ts.net/omega-check/screenshots/) · [omega-deep](https://kraynux.snake-mackarel.ts.net/omega-deep/screenshots/) · [omega-fold](https://kraynux.snake-mackarel.ts.net/omega-fold/screenshots/) · [omega-track](https://kraynux.snake-mackarel.ts.net/omega-track/screenshots/) · [omega-fuzz](https://kraynux.snake-mackarel.ts.net/omega-fuzz/screenshots/) · [omega-stress](https://kraynux.snake-mackarel.ts.net/omega-stress/screenshots/) 

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../../LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux-informational.svg)](https://www.linux.org/)
[![Interface](https://img.shields.io/badge/Interface-Textual%20TUI-cyan.svg)](https://github.com/Textualize/textual)

**Języki:**
<img src="https://flagcdn.com/w20/fr.png" alt="France" style="height:14px;"> [Français](../../../README.md) · <img src="https://flagcdn.com/w20/gb.png" alt="English" style="height:14px;"> [English](../en/README.md) · <img src="https://flagcdn.com/w20/es.png" alt="Español" style="height:14px;"> [Español](../es/README.md) · <img src="https://flagcdn.com/w20/br.png" alt="Português (Brasil)" style="height:14px;"> [Português (Brasil)](../pt-BR/README.md) · <img src="https://flagcdn.com/w20/it.png" alt="Italiano" style="height:14px;"> [Italiano](../it/README.md) · <img src="https://flagcdn.com/w20/de.png" alt="Deutsch" style="height:14px;"> [Deutsch](../de/README.md) · <img src="https://flagcdn.com/w20/nl.png" alt="Nederlands" style="height:14px;"> [Nederlands](../nl/README.md) · <img src="https://flagcdn.com/w20/pl.png" alt="Polski" style="height:14px;"> [Polski](README.md) · <img src="https://flagcdn.com/w20/ru.png" alt="Русский" style="height:14px;"> [Русский](../ru/README.md) · <img src="https://flagcdn.com/w20/cn.png" alt="中文" style="height:14px;"> [中文](../zh-CN/README.md) · <img src="https://flagcdn.com/w20/vn.png" alt="Tiếng Việt" style="height:14px;"> [Tiếng Việt](../vi/README.md) · <img src="https://flagcdn.com/w20/th.png" alt="ไทย" style="height:14px;"> [ไทย](../th/README.md) · <img src="https://flagcdn.com/w20/id.png" alt="Bahasa Indonesia" style="height:14px;"> [Bahasa Indonesia](../id/README.md) · <img src="https://flagcdn.com/w20/jp.png" alt="日本語" style="height:14px;"> [日本語](../ja/README.md) · <img src="https://flagcdn.com/w20/kr.png" alt="한국어" style="height:14px;"> [한국어](../ko/README.md) · <img src="https://flagcdn.com/w20/in.png" alt="हिन्दी" style="height:14px;"> [हिन्दी](../hi/README.md) · <img src="https://flagcdn.com/w20/ae.png" alt="العربية" style="height:14px;"> [العربية](../ar/README.md)

---
**Omega-Suite** to zunifikowany interfejs pakietu narzędzi skanujących **omega-**:  
[omega-scan](https://github.com/kraynux/omega-scan), [omega-check](https://github.com/kraynux/omega-check), [omega-deep](https://github.com/kraynux/omega-deep), [omega-fold](https://github.com/kraynux/omega-fold), [omega-stress](https://github.com/kraynux/omega-stress), [omega-track](https://github.com/kraynux/omega-track) i [omega-fuzz](https://github.com/kraynux/omega-fuzz)  
połączonych w jednej aplikacji TUI (siatka na ekranie głównym lub trwały pasek kart, zależnie od wyboru użytkownika) ze wspólną biblioteką [(`omega-lib`)](https://github.com/kraynux/omega-lib).


Każde narzędzie nadal można uruchamiać samodzielnie (`omega-check scan ...`
wciąż działa) - omega-suite jest dodatkową fasadą, a nie
zamiennikiem.

Szczegóły decyzji dotyczących architektury i ergonomii znajdziesz w
`~/DEV/SUITE/OMEGA-SUITE_SPECIFICATIONS.md` i
`~/DEV/SUITE/DECISIONS_ARCHITECTURE.md` (D-014/D-015).

## Prezentacja

Omega-Suite działa jako **stanowisko dowodzenia** skanerami Omega dla bezpieczeństwa sieci

### Cele

- Połączyć 7 narzędzi **skanerów omega** w spójnym interfejsie, nigdy ich nie modyfikując ani nie zastępując.
- Jeden motyw, jeden profil renderowania, jeden styl nawigacji dla 7 narzędzi - skonfigurowane raz, a nie 7 razy.
- Przechodzić od jednego narzędzia do drugiego bez utraty kontekstu: każdy stos ekranów pozostaje nienaruszony w tle.
- Pozostać lekkim mimo 7 połączonych narzędzi: nic nie jest ładowane do pamięci przed pierwszym faktycznym otwarciem.

## Funkcje

- **Jedna aplikacja TUI** (Textual) dla Omega-SCAN, -CHECK, -DEEP, -FOLD, -STRESS, -TRACK i -FUZZ.
- **Dwa style nawigacji** do wyboru (Ustawienia, restart proponowany od razu): siatka przycisków z ekranu głównego lub trwały pasek kart widoczny nawet w głębi (Historia, Ustawienia narzędzia...), bez powrotu do ekranu głównego.
- **Leniwe ładowanie**: każde narzędzie (kod Pythona i zależności) jest importowane dopiero przy pierwszym otwarciu w sesji - czas startu i zużycie pamięci pozostają proporcjonalne do faktycznie używanych narzędzi.
- **Wspólny motyw i profil renderowania**: motyw zmienia się na gorąco dla wszystkich 7 narzędzi naraz; profil renderowania i styl nawigacji, bardziej strukturalne, proponują natychmiastowy restart omega-suite.
- **Pomoc kontekstowa**: globalne skróty i przegląd zakresu 7 narzędzi z ekranu głównego, własna pomoc aktywnego narzędzia z poziomu karty.
- **Globalne czyszczenie eksportów** 7 narzędzi jednym kliknięciem (Ustawienia pakietu), także tych nigdy nieotwartych w sesji.
- **Ścisła izolacja między 7 narzędziami** mimo wspólnej aplikacji: żadnego przecieku stylu ani stanu z jednego narzędzia do drugiego.
- **Każde narzędzie pozostaje w pełni samodzielne** (własny TUI i CLI, `omega-check scan ...` wciąż działa) - omega-suite jest tylko dodatkową fasadą, nigdy zamiennikiem.

## Instalacja

Oficjalne archiwum jest dostarczane w formacie `.tar.gz`. Przed instalacją sprawdź jego integralność:

```bash
sha256sum omega-suite.tar.gz
```

```bash
./install.sh
./omega-suite.sh
```


## Użytkowanie
### Uruchamianie

```bash
cd ~/omega-suite
./omega-suite.sh
```

###  lub po prostu, jeśli alias został utworzony, wpisz w terminalu:
```bash
suite
```
## Zgodność terminali

Interfejs interaktywny (Textual) automatycznie wykrywa możliwości terminala (emulator, rozmiar) i odpowiednio dostosowuje swój strukturalny arkusz stylów (`complete`/`standard`/`reduced`/`mono`), bez ręcznej flagi. Tryb CLI zawsze pozostaje zwykłym tekstem, niezależnym od terminala. Polityka wspólna dla całego pakietu `omega-` (`omega-lib`, `terminal/policies.py`) — identyczna jak w `omega-check`/`omega-fire`.

### Profil według wykrytego emulatora

| Emulator | Profil początkowy |
|---|---|
| Ghostty, Alacritty, WezTerm, Kitty | `complete` |
| Konsole, GNOME Terminal, Terminator, Xfce4 Terminal | `standard` |
| xterm, urxvt, nowoczesny SSH | `reduced` |
| Linux TTY, stary SSH | `mono` |
| Nierozpoznany emulator | `reduced` (domyślny wariant zapasowy) |

### Profil według rozmiaru terminala

| Minimalny rozmiar (kolumny × wiersze) | Górny limit profilu |
|---|---|
| 120 × 32 | `complete` |
| 100 × 28 | `standard` |
| 80 × 24 | `reduced` |
| poniżej | `mono` |

Ostatecznie wybrany profil to **bardziej restrykcyjny z dwóch** (emulator i rozmiar) — Ghostty na pełnym ekranie zmniejszony do 70 kolumn schodzi do `mono`, nawet jeśli jego emulator pozwalałby na `complete`. Można go odświeżać na żywo klawiszem `r` lub nadpisać ręcznie w Ustawieniach pakietu (klawisz `s`).

## Architektura

### Zasady projektowe

- **Fasada kompozycji, nigdy 8. warstwa biznesowa**: omega-suite nie ma własnego `domain/` - składa 7 kontenerów już niezależnie zweryfikowanych przez każdy projekt, bez ponownej implementacji ich logiki.
- **Żaden plik 7 narzędzi nie jest modyfikowany.** Ich wspólne klasy ekranów/widżetów są łatane w pamięci, jeden raz, przy pierwszym faktycznym otwarciu danego narzędzia w sesji: izolacja CSS (narzędzie nigdy nie może odziedziczyć stylu innego), przekierowanie wewnętrznego « Wyjdź » narzędzia na kartę główną pakietu oraz wstrzyknięcie paska kart, jeśli ten styl nawigacji jest aktywny.
- **`textual` zabroniony poza `interfaces/tui/`** (sprawdzane przez `import-linter` przy każdej zmianie): `app/` pozostaje niezależny od wyświetlania i teoretycznie mógłby obsługiwać inny interfejs.
- **Dwupoziomowa leniwa budowa**: adapter narzędzia (import jego kodu), a potem jego kontener (baza SQLite, sondy sieciowe) - żadne z nich nie jest „opłacane” przed pierwszą faktyczną wizytą w tym konkretnym narzędziu.

### Struktura danych

```text
src/omega_suite/
├── app/              Składanie: leniwy DependencyContainer, bootstrap, adaptery 7 narzędzi
│                     (tool_adapters.py), wspólne ustawienia (motyw, profil renderowania, styl nawigacji)
├── infrastructure/   Ścieżki runtime (var/), przechowywanie ustawień (JSON)
├── interfaces/
│   ├── tui/          Jedyne miejsce importujące Textual: App, własne ekrany pakietu (Start, Ustawienia,
│   │                 Pomoc, Splash), łatka w pamięci ekranów 7 narzędzi (screen_patching.py)
│   └── cli/          Zarezerwowane, na razie puste - każde narzędzie zachowuje własny tryb CLI, wywoływany bezpośrednio
└── ports/            Kontrakty oczekiwane przez app/ (SettingsStore)
```

## Wymagania

### System

- Python 3.10+
- Linux (Textual działa na innych systemach, nietestowanych i nieobsługiwanych przez ten projekt)
- Dowolny terminal - jego rzeczywiste możliwości są wykrywane automatycznie, a renderowanie się dostosowuje (zobacz « Zgodność terminali » wyżej), aż do zwykłego TTY

### Zależności Pythona

Zadeklarowane w `pyproject.toml`, jedno środowisko wirtualne obejmuje je wszystkie (zobacz `install.sh`):

- `omega-lib`: wspólna biblioteka (motywy, wykrywanie terminala, poziomy zaufania)
- `omega-scan`, `omega-check`, `omega-deep`, `omega-fold`, `omega-stress`, `omega-track`, `omega-fuzz`: 7 zintegrowanych narzędzi, każde z własnymi zależnościami przechodnimi
- `textual`: interfejs TUI
- Zależności deweloperskie (`pip install -e ".[dev]"`): `pytest`, `pytest-asyncio`, `pytest-cov`, `ruff`, `mypy`, `import-linter`

### Eksporty

Każde narzędzie zapisuje własne eksporty w `var/<narzędzie>/exports/`, a zrzuty ekranu w `var/<narzędzie>/screenshots/` - `var/` względem katalogu, z którego uruchomiono omega-suite, lub `$OMEGA_SUITE_VAR_DIR`, aby to nadpisać. Nigdy nie jest to domyślny `var/` narzędzia uruchomionego samodzielnie: oba sposoby użycia (samodzielny lub w pakiecie) nigdy się nie mieszają. Każde narzędzie może ustawić własny katalog docelowy we własnych Ustawieniach. Przycisk « Wyczyść wszystkie eksporty » (Ustawienia pakietu) opróżnia ten katalog dla wszystkich 7 narzędzi naraz, także tych nigdy nieotwartych w sesji - szczegóły w Pomocy pakietu (klawisz `a` z ekranu głównego).

---

## Bezpieczeństwo

- Sam omega-suite nie wykonuje żadnych żądań sieciowych i niczego nie skanuje: orkiestruje wyświetlanie 7 narzędzi, z których każde w pełni zachowuje własne zabezpieczenia (zobacz ich zakres w Pomocy pakietu lub w ich własnym README).
- Sam omega-suite nie przetwarza żadnych sekretów ani danych logowania. To, co przechowuje każde narzędzie (przypięte cele, historia, własne ustawienia), pozostaje w jego własnym podkatalogu `var/<narzędzie>/`, niezmienione przez pakiet.
- Jedyny własny stan omega-suite (motyw, profil renderowania, styl nawigacji) znajduje się w `var/settings.json`, bez danych wrażliwych.
- `import-linter` przy każdej zmianie zabrania importu `textual` poza `interfaces/tui/` (zobacz Architektura) - to gwarancja strukturalna, a nie zwykła konwencja.

## Testy i jakość

```bash
source .venv/bin/activate
pip install -e ".[dev]"
lint-imports        # sprawdza Dependency Rule (textual zabroniony poza interfaces/tui)
pytest -q
ruff check src tests
mypy -p omega_suite
```

## Odinstalowanie

omega-suite nie dotyka niczego poza własnym katalogiem i aliasem uruchamiania:

1. Usuń wiersz `alias suite="..."` dodany przez `install.sh` w `~/.bashrc` i `~/.zshrc`.
2. Usuń katalog `omega-suite/` (wraz ze środowiskiem wirtualnym `.venv/`, danymi `var/` i ustawieniami).

7 narzędzi zainstalowanych osobno (lub rozwijanych we własnych katalogach) pozostaje nietkniętych: każde można instalować/odinstalowywać niezależnie, zgodnie z jego własnym README.

## Licencja

Omega-Suite jest rozpowszechniany na licencji **MIT**. Pełny tekst znajdziesz w pliku [`LICENSE`](../../../LICENSE).

---

> **Omega-Suite — Obserwować, sterować, audytować, by lepiej zabezpieczać.**
>
> Zunifikowany interfejs TUI dla skanerów Omega-
