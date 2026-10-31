<!-- Copyright (c) 2026 kraynux - kraynux@proton.me - Licencia MIT (consulta el archivo LICENSE) -->
<div align="center">
  <img src="https://raw.githubusercontent.com/kraynux/kraynux/refs/heads/main/docs/assets/omega-suite.png" alt="Omega-Suite" width="384">
</div>


#  OMEGA-SUITE

**Todos los escáneres "OMEGA" reunificados en una sola interfaz y una biblioteca compartida**

> Desarrollado por [kraynux](https://github.com/kraynux) para [Omega-Server](https://kraynux.snake-mackarel.ts.net)   

Página oficial: [OMEGA-SUITE](https://kraynux.snake-mackarel.ts.net/omega-suite/) &nbsp;   
Capturas de pantalla → [omega-scan](https://kraynux.snake-mackarel.ts.net/omega-scan/screenshots/) · [omega-check](https://kraynux.snake-mackarel.ts.net/omega-check/screenshots/) · [omega-deep](https://kraynux.snake-mackarel.ts.net/omega-deep/screenshots/) · [omega-fold](https://kraynux.snake-mackarel.ts.net/omega-fold/screenshots/) · [omega-track](https://kraynux.snake-mackarel.ts.net/omega-track/screenshots/) · [omega-fuzz](https://kraynux.snake-mackarel.ts.net/omega-fuzz/screenshots/) · [omega-stress](https://kraynux.snake-mackarel.ts.net/omega-stress/screenshots/) 

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../../LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux-informational.svg)](https://www.linux.org/)
[![Interface](https://img.shields.io/badge/Interface-Textual%20TUI-cyan.svg)](https://github.com/Textualize/textual)

**Idiomas:**
<img src="https://flagcdn.com/w20/fr.png" alt="France" style="height:14px;"> [Français](../../../README.md) · <img src="https://flagcdn.com/w20/gb.png" alt="English" style="height:14px;"> [English](../en/README.md) · <img src="https://flagcdn.com/w20/es.png" alt="Español" style="height:14px;"> [Español](README.md) · <img src="https://flagcdn.com/w20/br.png" alt="Português (Brasil)" style="height:14px;"> [Português (Brasil)](../pt-BR/README.md) · <img src="https://flagcdn.com/w20/it.png" alt="Italiano" style="height:14px;"> [Italiano](../it/README.md) · <img src="https://flagcdn.com/w20/de.png" alt="Deutsch" style="height:14px;"> [Deutsch](../de/README.md) · <img src="https://flagcdn.com/w20/nl.png" alt="Nederlands" style="height:14px;"> [Nederlands](../nl/README.md) · <img src="https://flagcdn.com/w20/pl.png" alt="Polski" style="height:14px;"> [Polski](../pl/README.md) · <img src="https://flagcdn.com/w20/ru.png" alt="Русский" style="height:14px;"> [Русский](../ru/README.md) · <img src="https://flagcdn.com/w20/cn.png" alt="中文" style="height:14px;"> [中文](../zh-CN/README.md) · <img src="https://flagcdn.com/w20/vn.png" alt="Tiếng Việt" style="height:14px;"> [Tiếng Việt](../vi/README.md) · <img src="https://flagcdn.com/w20/th.png" alt="ไทย" style="height:14px;"> [ไทย](../th/README.md) · <img src="https://flagcdn.com/w20/id.png" alt="Bahasa Indonesia" style="height:14px;"> [Bahasa Indonesia](../id/README.md) · <img src="https://flagcdn.com/w20/jp.png" alt="日本語" style="height:14px;"> [日本語](../ja/README.md) · <img src="https://flagcdn.com/w20/kr.png" alt="한국어" style="height:14px;"> [한국어](../ko/README.md) · <img src="https://flagcdn.com/w20/in.png" alt="हिन्दी" style="height:14px;"> [हिन्दी](../hi/README.md) · <img src="https://flagcdn.com/w20/ae.png" alt="العربية" style="height:14px;"> [العربية](../ar/README.md)

---
**Omega-Suite** es una interfaz unificada para la suite de herramientas escáner **omega-**:  
[omega-scan](https://github.com/kraynux/omega-scan), [omega-check](https://github.com/kraynux/omega-check), [omega-deep](https://github.com/kraynux/omega-deep), [omega-fold](https://github.com/kraynux/omega-fold), [omega-stress](https://github.com/kraynux/omega-stress), [omega-track](https://github.com/kraynux/omega-track) y [omega-fuzz](https://github.com/kraynux/omega-fuzz)  
reunidas en una sola aplicación TUI (cuadrícula de Inicio o barra de pestañas persistente, según la elección del usuario) con una biblioteca compartida [(`omega-lib`)](https://github.com/kraynux/omega-lib).


Cada herramienta se puede seguir ejecutando de forma totalmente autónoma
(`omega-check scan ...` sigue funcionando) - omega-suite es una fachada
adicional, no un reemplazo.

Consulta `~/DEV/SUITE/OMEGA-SUITE_SPECIFICATIONS.md` y
`~/DEV/SUITE/DECISIONS_ARCHITECTURE.md` (D-014/D-015) para el detalle de
las decisiones de arquitectura y ergonomía.

## Presentación

Omega-Suite actúa como un **puesto de control** de los escáneres Omega para la seguridad de red.

### Objetivos

- Reunir las 7 herramientas **escáner omega** en una interfaz coherente, sin modificarlas ni reemplazarlas nunca.
- Un único tema, un único perfil de renderizado, un único estilo de navegación para las 7 herramientas - configurados una sola vez, en lugar de 7.
- Pasar de una herramienta a otra sin perder el contexto: la pila de pantallas de cada herramienta permanece intacta en segundo plano.
- Mantenerse ligero pese a reunir 7 herramientas: nada se carga en memoria antes de abrirse por primera vez.

## Funcionalidades

- **Una sola aplicación TUI** (Textual) para Omega-SCAN, -CHECK, -DEEP, -FOLD, -STRESS, -TRACK y -FUZZ.
- **Dos estilos de navegación** a elegir (Ajustes, con reinicio propuesto de inmediato): cuadrícula de botones desde Inicio, o barra de pestañas persistente visible incluso en profundidad (Historial, Ajustes propios de una herramienta...), sin tener que volver nunca a Inicio.
- **Carga diferida**: el código y las dependencias de cada herramienta solo se importan la primera vez que se abre en la sesión - el tiempo de arranque y la memoria se mantienen proporcionales a las herramientas realmente usadas.
- **Tema y perfil de renderizado compartidos**: el tema cambia en caliente para las 7 herramientas a la vez; el perfil de renderizado y el estilo de navegación, más estructurales, proponen reiniciar omega-suite de inmediato.
- **Ayuda contextual**: atajos globales y panorama del alcance de las 7 herramientas desde Inicio, ayuda propia de la herramienta activa desde una pestaña.
- **Purga global de las exportaciones** de las 7 herramientas en un clic (Ajustes de la suite), incluso para las que nunca se abrieron en la sesión.
- **Aislamiento estricto entre las 7 herramientas** pese a compartir una sola aplicación: ninguna fuga de estilo ni de estado de una herramienta a otra.
- **Cada herramienta sigue siendo utilizable de forma totalmente autónoma** (TUI y CLI propios, `omega-check scan ...` sigue funcionando) - omega-suite es solo una fachada adicional, nunca un reemplazo.

## Instalación

El archivo oficial se distribuye en formato `.tar.gz`. Verifica su integridad antes de instalarlo:

```bash
sha256sum omega-suite.tar.gz
```

```bash
./install.sh
./omega-suite.sh
```


## Uso
### Puesta en marcha

```bash
cd ~/omega-suite
./omega-suite.sh
```

### o, más simple, si se creó el alias, escribe en la terminal:
```bash
suite
```
## Idiomas de la interfaz

La interfaz está disponible en 17 idiomas. Se elige en los Ajustes de la suite («Langue / Language») y se aplica a las 7 herramientas tras reiniciar la interfaz; la variable `OMEGA_SUITE_LANG` fuerza un idioma durante una sesión. Un ajuste aparte, «Idioma de las exportaciones», fija el idioma de los informes exportados por las 7 herramientas. En una consola de texto Linux (TTY), los idiomas de escritura no latina se muestran en inglés durante la sesión. La línea de comandos sigue en francés.

## Compatibilidad de terminales

La interfaz interactiva (Textual) detecta automáticamente las capacidades de la terminal (emulador, tamaño) y adapta en consecuencia su hoja de estilos estructural (`complete`/`standard`/`reduced`/`mono`), sin ningún parámetro manual. El modo CLI siempre se mantiene en texto plano, independiente de la terminal. Política compartida por toda la suite `omega-` (`omega-lib`, `terminal/policies.py`) — idéntica a la de `omega-check`/`omega-fire`.

### Perfil según el emulador detectado

| Emulador | Perfil inicial |
|---|---|
| Ghostty, Alacritty, WezTerm, Kitty | `complete` |
| Konsole, GNOME Terminal, Terminator, Xfce4 Terminal | `standard` |
| xterm, urxvt, SSH moderno | `reduced` |
| TTY de Linux, SSH antiguo | `mono` |
| Emulador no reconocido | `reduced` (valor por defecto) |

### Perfil según el tamaño de la terminal

| Tamaño mínimo (columnas × líneas) | Techo de perfil |
|---|---|
| 120 × 32 | `complete` |
| 100 × 28 | `standard` |
| 80 × 24 | `reduced` |
| por debajo | `mono` |

El perfil final es **el más restrictivo de los dos** (emulador y tamaño) — un Ghostty a pantalla completa redimensionado a 70 columnas vuelve a `mono`, aunque su emulador permitiría `complete`. Se puede refrescar en vivo con la tecla `r`, o forzar manualmente desde los Ajustes de la suite (tecla `s`).

## Arquitectura

### Principios de diseño

- **Fachada de composición, nunca una octava capa de negocio**: omega-suite no tiene `domain/` propio - ensambla los 7 contenedores ya validados de forma independiente por cada proyecto, sin reimplementar su lógica.
- **No se modifica ningún archivo de las 7 herramientas.** Sus clases de pantallas/widgets compartidas se parchean en memoria, una sola vez, en la primera apertura real de esa herramienta en la sesión: aislamiento CSS (una herramienta nunca puede heredar el estilo de otra), redirección del "Salir" interno de la herramienta hacia la pestaña Inicio de la suite, e inyección de la barra de pestañas si ese estilo de navegación está activo.
- **`textual` está prohibido fuera de `interfaces/tui/`** (verificado por `import-linter` en cada cambio): `app/` permanece independiente de la capa de presentación, y en teoría podría servir a otra interfaz.
- **Construcción diferida en dos niveles**: el adaptador de una herramienta (importa su código), luego su contenedor (base SQLite, sondas de red) - ninguno de los dos se paga antes de la primera visita real a esa herramienta en concreto.

### Estructura de datos

```text
src/omega_suite/
├── app/              Ensamblaje: DependencyContainer diferido, bootstrap, adaptadores de las 7 herramientas
│                     (tool_adapters.py), ajustes compartidos (tema, perfil de renderizado, estilo de navegación)
├── infrastructure/   Rutas de tiempo de ejecución (var/), almacenamiento de ajustes (JSON)
├── interfaces/
│   ├── tui/          Único lugar que importa Textual: App, pantallas propias de la suite (Inicio, Ajustes,
│   │                 Ayuda, Splash), parcheo en memoria de las pantallas de las 7 herramientas (screen_patching.py)
│   └── cli/          Reservado, vacío por ahora - cada herramienta conserva su propio CLI, invocado directamente
└── ports/            Contratos que espera app/ (SettingsStore)
```

## Requisitos

### Sistema

- Python 3.10+
- Linux (Textual funciona en otros sistemas, ni probados ni soportados por este proyecto)
- Cualquier terminal - sus capacidades reales se detectan automáticamente y el renderizado se adapta en consecuencia (ver "Compatibilidad de terminales" más arriba), hasta llegar a una TTY básica

### Dependencias de Python

Declaradas en `pyproject.toml`, un único entorno virtual las reúne todas (ver `install.sh`):

- `omega-lib`: biblioteca compartida (temas, detección de terminal, niveles de confianza)
- `omega-scan`, `omega-check`, `omega-deep`, `omega-fold`, `omega-stress`, `omega-track`, `omega-fuzz`: las 7 herramientas integradas, cada una con sus propias dependencias transitivas
- `textual`: interfaz TUI
- Dependencias de desarrollo (`pip install -e ".[dev]"`): `pytest`, `pytest-asyncio`, `pytest-cov`, `ruff`, `mypy`, `import-linter`

### Exportaciones

Cada herramienta escribe sus propias exportaciones en `var/<herramienta>/exports/` y sus capturas de pantalla en `var/<herramienta>/screenshots/` - `var/` relativo a la carpeta desde la que se lanzó omega-suite, o `$OMEGA_SUITE_VAR_DIR` para redefinirla. Nunca es el `var/` por defecto de la herramienta lanzada sola: los dos usos (autónomo o integrado en la suite) nunca se mezclan. Cada herramienta puede redefinir su propia carpeta de destino desde sus propios Ajustes. El botón "Vaciar todas las exportaciones" (Ajustes de la suite) vacía esa carpeta para las 7 herramientas de golpe, incluso las que nunca se abrieron en la sesión - consulta la Ayuda de la suite (tecla `a` desde Inicio) para más detalles.

---

## Seguridad

- Omega-suite en sí no realiza ninguna petición de red ni escanea nada: orquesta la presentación de las 7 herramientas, cada una de las cuales conserva íntegramente sus propias salvaguardas (consulta el alcance de cada una en la Ayuda de la suite, o en su propio README).
- Omega-suite en sí no maneja ningún secreto ni credencial. Lo que cada herramienta almacena (objetivos fijados, historial, ajustes propios) permanece bajo su propia subcarpeta `var/<herramienta>/`, sin que la suite lo toque.
- El único estado propio de omega-suite (tema, perfil de renderizado, estilo de navegación) vive en `var/settings.json`, sin ningún dato sensible.
- `import-linter` prohíbe cualquier importación de `textual` fuera de `interfaces/tui/` en cada cambio (ver Arquitectura) - una garantía estructural, no una simple convención.

## Pruebas y calidad

```bash
source .venv/bin/activate
pip install -e ".[dev]"
lint-imports        # verifica la Dependency Rule (textual prohibido fuera de interfaces/tui)
pytest -q
ruff check src tests
mypy -p omega_suite
```

## Desinstalación

omega-suite no toca nada fuera de su propia carpeta y del alias de lanzamiento:

1. Elimina la línea `alias suite="..."` añadida por `install.sh` en `~/.bashrc` y `~/.zshrc`.
2. Elimina la carpeta `omega-suite/` (entorno virtual `.venv/`, datos `var/` y ajustes incluidos).

Las 7 herramientas instaladas por separado (o en desarrollo en sus propias carpetas) no se ven afectadas: cada una sigue siendo instalable/desinstalable de forma independiente, siguiendo su propio README.

## Licencia

Omega-Suite se distribuye bajo licencia **MIT**. Consulta el archivo [`LICENSE`](../../../LICENSE) para el texto completo.

---

> **Omega-Suite — Observar, pilotar, auditar, para proteger mejor.**
>
> Una interfaz TUI unificada para los escáneres Omega-
