<!-- Copyright (c) 2026 kraynux - kraynux@proton.me - Licence MIT (voir fichier LICENSE) -->
<div align="center">
  <img src="https://raw.githubusercontent.com/kraynux/kraynux/refs/heads/main/docs/assets/omega-suite.png" alt="Omega-Suite" width="384">
</div>


#  OMEGA-SUITE

**L'insieme degli scanner "OMEGA" riuniti in un'unica interfaccia e una libreria condivisa**

> Sviluppato da **kraynux** per **Omega-server** 
[kraynux.snake-mackarel](https://kraynux.snake-mackarel.ts.net)

Pagina ufficiale: [OMEGA-SUITE](https://kraynux.snake-mackarel.ts.net/omega-suite/) &nbsp;   
Screenshot → [omega-scan](https://kraynux.snake-mackarel.ts.net/omega-scan/screenshots/) · [omega-check](https://kraynux.snake-mackarel.ts.net/omega-check/screenshots/) · [omega-deep](https://kraynux.snake-mackarel.ts.net/omega-deep/screenshots/) · [omega-fold](https://kraynux.snake-mackarel.ts.net/omega-fold/screenshots/) · [omega-track](https://kraynux.snake-mackarel.ts.net/omega-track/screenshots/) · [omega-fuzz](https://kraynux.snake-mackarel.ts.net/omega-fuzz/screenshots/) · [omega-stress](https://kraynux.snake-mackarel.ts.net/omega-stress/screenshots/) 

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../../LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux-informational.svg)](https://www.linux.org/)
[![Interface](https://img.shields.io/badge/Interface-Textual%20TUI-cyan.svg)](https://github.com/Textualize/textual)

**Lingue:**
<img src="https://flagcdn.com/w20/fr.png" alt="France" style="height:14px;"> [Français](../../../README.md) · <img src="https://flagcdn.com/w20/gb.png" alt="English" style="height:14px;"> [English](../en/README.md) · <img src="https://flagcdn.com/w20/es.png" alt="Español" style="height:14px;"> [Español](../es/README.md) · <img src="https://flagcdn.com/w20/br.png" alt="Português (Brasil)" style="height:14px;"> [Português (Brasil)](../pt-BR/README.md) · <img src="https://flagcdn.com/w20/it.png" alt="Italiano" style="height:14px;"> [Italiano](README.md) · <img src="https://flagcdn.com/w20/de.png" alt="Deutsch" style="height:14px;"> [Deutsch](../de/README.md) · <img src="https://flagcdn.com/w20/nl.png" alt="Nederlands" style="height:14px;"> [Nederlands](../nl/README.md) · <img src="https://flagcdn.com/w20/pl.png" alt="Polski" style="height:14px;"> [Polski](../pl/README.md) · <img src="https://flagcdn.com/w20/ru.png" alt="Русский" style="height:14px;"> [Русский](../ru/README.md) · <img src="https://flagcdn.com/w20/cn.png" alt="中文" style="height:14px;"> [中文](../zh-CN/README.md) · <img src="https://flagcdn.com/w20/vn.png" alt="Tiếng Việt" style="height:14px;"> [Tiếng Việt](../vi/README.md) · <img src="https://flagcdn.com/w20/th.png" alt="ไทย" style="height:14px;"> [ไทย](../th/README.md) · <img src="https://flagcdn.com/w20/id.png" alt="Bahasa Indonesia" style="height:14px;"> [Bahasa Indonesia](../id/README.md) · <img src="https://flagcdn.com/w20/jp.png" alt="日本語" style="height:14px;"> [日本語](../ja/README.md) · <img src="https://flagcdn.com/w20/kr.png" alt="한국어" style="height:14px;"> [한국어](../ko/README.md) · <img src="https://flagcdn.com/w20/in.png" alt="हिन्दी" style="height:14px;"> [हिन्दी](../hi/README.md) · <img src="https://flagcdn.com/w20/ae.png" alt="العربية" style="height:14px;"> [العربية](../ar/README.md)

---
**Omega-Suite** è un'interfaccia unificata della suite di strumenti scanner **omega-**:  
[omega-scan](https://github.com/kraynux/omega-scan), [omega-check](https://github.com/kraynux/omega-check), [omega-deep](https://github.com/kraynux/omega-deep), [omega-fold](https://github.com/kraynux/omega-fold), [omega-stress](https://github.com/kraynux/omega-stress), [omega-track](https://github.com/kraynux/omega-track) e [omega-fuzz](https://github.com/kraynux/omega-fuzz)  
riuniti in un'unica applicazione TUI (griglia nella schermata iniziale o barra di schede persistente, a scelta dell'utente) con una libreria condivisa [(`omega-lib`)](https://github.com/kraynux/omega-lib).


Ogni strumento resta eseguibile in modo autonomo (`omega-check scan ...`
continua a funzionare) - omega-suite è una facciata aggiuntiva, non una
sostituzione.

Vedi `~/DEV/SUITE/OMEGA-SUITE_SPECIFICATIONS.md` e
`~/DEV/SUITE/DECISIONS_ARCHITECTURE.md` (D-014/D-015) per il dettaglio delle
scelte di architettura e di ergonomia.

## Presentazione

Omega-Suite agisce come una **postazione di comando** degli scanner Omega per la sicurezza di rete

### Obiettivi

- Riunire i 7 strumenti **scanner omega** in un'interfaccia coerente, senza mai modificarli né sostituirli.
- Un solo tema, un solo profilo di rendering, un solo stile di navigazione per i 7 strumenti - configurati una volta, invece di 7 volte.
- Passare da uno strumento all'altro senza perdere il contesto: ogni pila di schermate resta intatta in background.
- Restare leggero nonostante i 7 strumenti riuniti: nulla viene caricato in memoria prima della prima apertura reale.

## Funzionalità

- **Un'unica applicazione TUI** (Textual) per Omega-SCAN, -CHECK, -DEEP, -FOLD, -STRESS, -TRACK e -FUZZ.
- **Due stili di navigazione** a scelta (Impostazioni, riavvio proposto subito): griglia di pulsanti dalla schermata iniziale, o barra di schede persistente visibile anche in profondità (Cronologia, Impostazioni di uno strumento...), senza mai ripassare dalla schermata iniziale.
- **Caricamento pigro**: ogni strumento (codice Python e dipendenze) viene importato solo alla sua primissima apertura nella sessione - il tempo di avvio e la memoria restano proporzionali agli strumenti effettivamente usati.
- **Tema e profilo di rendering condivisi**: il tema cambia a caldo per i 7 strumenti insieme; profilo di rendering e stile di navigazione, più strutturali, propongono di riavviare subito omega-suite.
- **Aiuto contestuale**: scorciatoie globali e panoramica dell'ambito dei 7 strumenti dalla schermata iniziale, aiuto specifico dello strumento attivo da una scheda.
- **Pulizia globale delle esportazioni** dei 7 strumenti con un clic (Impostazioni della suite), anche di quelli mai aperti nella sessione.
- **Isolamento rigoroso tra i 7 strumenti** nonostante la condivisione di un'unica applicazione: nessuna fuga di stile né di stato da uno strumento all'altro.
- **Ogni strumento resta utilizzabile in piena autonomia** (TUI e CLI proprie, `omega-check scan ...` continua a funzionare) - omega-suite ne è solo una facciata aggiuntiva, mai una sostituzione.

## Installazione

L'archivio ufficiale è fornito in formato `.tar.gz`. Verificane l'integrità prima dell'installazione:

```bash
sha256sum omega-suite.tar.gz
```

```bash
./install.sh
./omega-suite.sh
```


## Utilizzo
### Avvio

```bash
cd ~/omega-suite
./omega-suite.sh
```

###  o semplicemente, se l'alias è stato creato, digita nel terminale:
```bash
suite
```
## Lingue dell'interfaccia

L'interfaccia è disponibile in 17 lingue. La scelta si fa nelle Impostazioni della suite («Langue / Language») e vale per i 7 strumenti dopo il riavvio dell'interfaccia; la variabile `OMEGA_SUITE_LANG` forza una lingua per una sessione. Un'impostazione a parte, «Lingua delle esportazioni», fissa la lingua dei report esportati dai 7 strumenti. Su una console di testo Linux (TTY), le lingue con scrittura non latina vengono mostrate in inglese per la sessione. La riga di comando resta in francese.

## Compatibilità dei terminali

L'interfaccia interattiva (Textual) rileva automaticamente le capacità del terminale (emulatore, dimensione) e adatta di conseguenza il proprio foglio di stile strutturale (`complete`/`standard`/`reduced`/`mono`), senza flag manuali. La modalità CLI resta sempre in testo semplice, indipendente dal terminale. Politica condivisa da tutta la suite `omega-` (`omega-lib`, `terminal/policies.py`) — identica a quella di `omega-check`/`omega-fire`.

### Profilo in base all'emulatore rilevato

| Emulatore | Profilo iniziale |
|---|---|
| Ghostty, Alacritty, WezTerm, Kitty | `complete` |
| Konsole, GNOME Terminal, Terminator, Xfce4 Terminal | `standard` |
| xterm, urxvt, SSH moderno | `reduced` |
| TTY Linux, SSH datato | `mono` |
| Emulatore non riconosciuto | `reduced` (ripiego predefinito) |

### Profilo in base alla dimensione del terminale

| Dimensione minima (colonne × righe) | Tetto del profilo |
|---|---|
| 120 × 32 | `complete` |
| 100 × 28 | `standard` |
| 80 × 24 | `reduced` |
| al di sotto | `mono` |

Il profilo finale scelto è **il più restrittivo dei due** (emulatore e dimensione) — un Ghostty a schermo intero ridimensionato a 70 colonne scende a `mono`, anche se il suo emulatore consentirebbe `complete`. Aggiornabile in tempo reale con il tasto `r`, o forzabile manualmente dalle Impostazioni della suite (tasto `s`).

## Architettura

### Principi di progettazione

- **Facciata di composizione, mai un 8° livello di business**: omega-suite non ha un proprio `domain/` - assembla i 7 container già convalidati in modo indipendente da ciascun progetto, senza reimplementarne la logica.
- **Nessun file dei 7 strumenti viene modificato.** Le loro classi di schermate/widget condivisi vengono modificate in memoria, una sola volta, alla prima apertura reale di quello strumento nella sessione: isolamento CSS (uno strumento non può mai ereditare lo stile di un altro), reindirizzamento del « Esci » interno dello strumento verso la scheda iniziale della suite, e iniezione della barra di schede se questo stile di navigazione è attivo.
- **`textual` vietato al di fuori di `interfaces/tui/`** (verificato da `import-linter` a ogni modifica): `app/` resta indipendente dalla visualizzazione e potrebbe, in teoria, servire un'altra interfaccia.
- **Costruzione pigra su due livelli**: l'adattatore di uno strumento (importazione del suo codice), poi il suo container (base SQLite, sonde di rete) - nessuno dei due viene pagato prima della prima visita reale a quello strumento preciso.

### Struttura dei dati

```text
src/omega_suite/
├── app/              Assemblaggio: DependencyContainer pigro, bootstrap, adattatori dei 7 strumenti
│                     (tool_adapters.py), impostazioni condivise (tema, profilo di rendering, stile di navigazione)
├── infrastructure/   Percorsi di runtime (var/), archiviazione delle impostazioni (JSON)
├── interfaces/
│   ├── tui/          Unico punto che importa Textual: App, schermate proprie della suite (Home, Impostazioni,
│   │                 Aiuto, Splash), patch in memoria delle schermate dei 7 strumenti (screen_patching.py)
│   └── cli/          Riservato, vuoto finora - ogni strumento mantiene la propria modalità CLI, invocata direttamente
└── ports/            Contratti attesi da app/ (SettingsStore)
```

## Prerequisiti

### Sistema

- Python 3.10+
- Linux (Textual funziona su altri sistemi, non testati né supportati da questo progetto)
- Un terminale, qualunque esso sia - le sue capacità reali vengono rilevate automaticamente e il rendering si adatta (vedi « Compatibilità dei terminali » sopra), fino a una semplice TTY

### Dipendenze Python

Dichiarate in `pyproject.toml`, un unico ambiente virtuale le riunisce tutte (vedi `install.sh`):

- `omega-lib`: libreria condivisa (temi, rilevamento del terminale, livelli di confidenza)
- `omega-scan`, `omega-check`, `omega-deep`, `omega-fold`, `omega-stress`, `omega-track`, `omega-fuzz`: i 7 strumenti integrati, ciascuno con le proprie dipendenze transitive
- `textual`: interfaccia TUI
- Dipendenze di sviluppo (`pip install -e ".[dev]"`): `pytest`, `pytest-asyncio`, `pytest-cov`, `ruff`, `mypy`, `import-linter`

### Esportazioni

Ogni strumento scrive le proprie esportazioni in `var/<strumento>/exports/` e i propri screenshot in `var/<strumento>/screenshots/` - `var/` relativo alla cartella da cui è stato avviato omega-suite, oppure `$OMEGA_SUITE_VAR_DIR` per sovrascriverlo. Non è mai il `var/` predefinito dello strumento avviato da solo: i due usi (autonomo o integrato nella suite) non si mescolano mai. Ogni strumento può ridefinire la propria cartella di destinazione dalle proprie Impostazioni. Il pulsante « Svuota tutte le esportazioni » (Impostazioni della suite) svuota questa cartella per i 7 strumenti in una volta, anche per quelli mai aperti nella sessione - vedi l'Aiuto della suite (tasto `a` dalla schermata iniziale) per il dettaglio.

---

## Sicurezza

- omega-suite stesso non fa alcuna richiesta di rete e non scansiona nulla: orchestra la visualizzazione dei 7 strumenti, ognuno dei quali mantiene integralmente le proprie salvaguardie (vedi il rispettivo ambito nell'Aiuto della suite, o nel loro README).
- Nessun segreto né credenziale viene gestito da omega-suite stesso. Ciò che ogni strumento memorizza (bersagli fissati, cronologia, impostazioni proprie) resta nella propria sottocartella `var/<strumento>/`, invariato dalla suite.
- L'unico stato proprio di omega-suite (tema, profilo di rendering, stile di navigazione) si trova in `var/settings.json`, senza dati sensibili.
- `import-linter` vieta qualsiasi importazione di `textual` al di fuori di `interfaces/tui/` a ogni modifica (vedi Architettura) - una garanzia strutturale, non una semplice convenzione.

## Test e qualità

```bash
source .venv/bin/activate
pip install -e ".[dev]"
lint-imports        # verifica la Dependency Rule (textual vietato fuori da interfaces/tui)
pytest -q
ruff check src tests
mypy -p omega_suite
```

## Disinstallazione

omega-suite non tocca nulla al di fuori della propria cartella e dell'alias di avvio:

1. Rimuovere la riga `alias suite="..."` aggiunta da `install.sh` in `~/.bashrc` e `~/.zshrc`.
2. Eliminare la cartella `omega-suite/` (ambiente virtuale `.venv/`, dati `var/` e impostazioni inclusi).

I 7 strumenti installati separatamente (o in sviluppo nelle proprie cartelle) non vengono toccati: ognuno resta installabile/disinstallabile in modo indipendente, seguendo il proprio README.

## Licenza

Omega-Suite è distribuito con licenza **MIT**. Consulta il file [`LICENSE`](../../../LICENSE) per il testo completo.

---

> **Omega-Suite — Osservare, pilotare, verificare, per proteggere meglio.**
>
> Un'interfaccia TUI unificata per gli scanner Omega-
