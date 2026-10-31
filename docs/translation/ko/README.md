<!-- Copyright (c) 2026 kraynux - kraynux@proton.me - Licence MIT (voir fichier LICENSE) -->
<div align="center">
  <img src="https://raw.githubusercontent.com/kraynux/kraynux/refs/heads/main/docs/assets/omega-suite.png" alt="Omega-Suite" width="384">
</div>


#  OMEGA-SUITE

**"OMEGA" 스캐너 전체를 하나의 인터페이스와 공유 라이브러리로 통합**

> [kraynux](https://github.com/kraynux)가 [Omega-Server](https://kraynux.snake-mackarel.ts.net)를 위해 개발   

공식 페이지: [OMEGA-SUITE](https://kraynux.snake-mackarel.ts.net/omega-suite/) &nbsp;   
스크린샷 → [omega-scan](https://kraynux.snake-mackarel.ts.net/omega-scan/screenshots/) · [omega-check](https://kraynux.snake-mackarel.ts.net/omega-check/screenshots/) · [omega-deep](https://kraynux.snake-mackarel.ts.net/omega-deep/screenshots/) · [omega-fold](https://kraynux.snake-mackarel.ts.net/omega-fold/screenshots/) · [omega-track](https://kraynux.snake-mackarel.ts.net/omega-track/screenshots/) · [omega-fuzz](https://kraynux.snake-mackarel.ts.net/omega-fuzz/screenshots/) · [omega-stress](https://kraynux.snake-mackarel.ts.net/omega-stress/screenshots/) 

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../../LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux-informational.svg)](https://www.linux.org/)
[![Interface](https://img.shields.io/badge/Interface-Textual%20TUI-cyan.svg)](https://github.com/Textualize/textual)

**언어:**
<img src="https://flagcdn.com/w20/fr.png" alt="France" style="height:14px;"> [Français](../../../README.md) · <img src="https://flagcdn.com/w20/gb.png" alt="English" style="height:14px;"> [English](../en/README.md) · <img src="https://flagcdn.com/w20/es.png" alt="Español" style="height:14px;"> [Español](../es/README.md) · <img src="https://flagcdn.com/w20/br.png" alt="Português (Brasil)" style="height:14px;"> [Português (Brasil)](../pt-BR/README.md) · <img src="https://flagcdn.com/w20/it.png" alt="Italiano" style="height:14px;"> [Italiano](../it/README.md) · <img src="https://flagcdn.com/w20/de.png" alt="Deutsch" style="height:14px;"> [Deutsch](../de/README.md) · <img src="https://flagcdn.com/w20/nl.png" alt="Nederlands" style="height:14px;"> [Nederlands](../nl/README.md) · <img src="https://flagcdn.com/w20/pl.png" alt="Polski" style="height:14px;"> [Polski](../pl/README.md) · <img src="https://flagcdn.com/w20/ru.png" alt="Русский" style="height:14px;"> [Русский](../ru/README.md) · <img src="https://flagcdn.com/w20/cn.png" alt="中文" style="height:14px;"> [中文](../zh-CN/README.md) · <img src="https://flagcdn.com/w20/vn.png" alt="Tiếng Việt" style="height:14px;"> [Tiếng Việt](../vi/README.md) · <img src="https://flagcdn.com/w20/th.png" alt="ไทย" style="height:14px;"> [ไทย](../th/README.md) · <img src="https://flagcdn.com/w20/id.png" alt="Bahasa Indonesia" style="height:14px;"> [Bahasa Indonesia](../id/README.md) · <img src="https://flagcdn.com/w20/jp.png" alt="日本語" style="height:14px;"> [日本語](../ja/README.md) · <img src="https://flagcdn.com/w20/kr.png" alt="한국어" style="height:14px;"> [한국어](README.md) · <img src="https://flagcdn.com/w20/in.png" alt="हिन्दी" style="height:14px;"> [हिन्दी](../hi/README.md) · <img src="https://flagcdn.com/w20/ae.png" alt="العربية" style="height:14px;"> [العربية](../ar/README.md)

---
**Omega-Suite**는 **omega-** 스캐너 도구 모음의 통합 인터페이스입니다:  
[omega-scan](https://github.com/kraynux/omega-scan), [omega-check](https://github.com/kraynux/omega-check), [omega-deep](https://github.com/kraynux/omega-deep), [omega-fold](https://github.com/kraynux/omega-fold), [omega-stress](https://github.com/kraynux/omega-stress), [omega-track](https://github.com/kraynux/omega-track), [omega-fuzz](https://github.com/kraynux/omega-fuzz)  
를 하나의 TUI 애플리케이션(사용자 선택에 따라 홈 그리드 또는 상시 탭 표시줄)으로 묶고 공유 라이브러리 [(`omega-lib`)](https://github.com/kraynux/omega-lib)를 갖추었습니다.


각 도구는 여전히 단독으로 실행할 수 있습니다(`omega-check scan ...`
는 그대로 작동) - omega-suite는 추가 파사드이며
대체물이 아닙니다.

아키텍처와 사용성에 관한 결정의 자세한 내용은
`~/DEV/SUITE/OMEGA-SUITE_SPECIFICATIONS.md`와
`~/DEV/SUITE/DECISIONS_ARCHITECTURE.md`(D-014/D-015)를 참조하십시오.

## 소개

Omega-Suite는 네트워크 보안을 위한 Omega 스캐너들의 **조종석** 역할을 합니다

### 목표

- 7개의 **omega 스캐너**를 일관된 하나의 인터페이스로 모으되, 결코 수정하거나 대체하지 않는다.
- 7개 도구에 테마 하나, 렌더링 프로필 하나, 탐색 방식 하나 - 7번이 아니라 한 번만 설정한다.
- 맥락을 잃지 않고 도구 사이를 오간다: 각 화면 스택은 백그라운드에서 그대로 유지된다.
- 7개 도구를 모았어도 가볍게 유지한다: 실제로 처음 열기 전에는 아무것도 메모리에 올리지 않는다.

## 기능

- Omega-SCAN, -CHECK, -DEEP, -FOLD, -STRESS, -TRACK, -FUZZ를 위한 **단일 TUI 애플리케이션**(Textual).
- 선택 가능한 **두 가지 탐색 방식**(설정, 즉시 재시작 제안): 홈의 버튼 그리드, 또는 깊이 들어가도(기록, 도구의 설정...) 계속 보이는 상시 탭 표시줄. 홈으로 돌아갈 필요가 없습니다.
- **지연 로딩**: 각 도구(Python 코드와 의존성)는 세션에서 처음 열 때만 가져옵니다 - 시작 시간과 메모리는 실제로 쓰는 도구에 비례합니다.
- **공유 테마와 렌더링 프로필**: 테마는 7개 도구 모두에서 동시에 즉시 바뀝니다. 더 구조적인 렌더링 프로필과 탐색 방식은 omega-suite를 바로 재시작하도록 제안합니다.
- **상황별 도움말**: 홈에서는 전역 단축키와 7개 도구의 범위 개요, 탭에서는 활성 도구 고유의 도움말.
- 7개 도구의 **내보내기 일괄 정리**를 한 번의 클릭으로(도구 모음 설정), 세션에서 한 번도 열지 않은 도구도 포함.
- 하나의 애플리케이션을 공유하지만 **7개 도구 사이는 엄격히 격리**: 한 도구에서 다른 도구로 스타일이나 상태가 새지 않습니다.
- **각 도구는 완전히 독립적으로도 사용 가능**(고유 TUI와 CLI, `omega-check scan ...`는 그대로 작동) - omega-suite는 추가 파사드일 뿐 결코 대체물이 아닙니다.

## 설치

공식 아카이브는 `.tar.gz` 형식으로 제공됩니다. 설치 전에 무결성을 확인하십시오:

```bash
sha256sum omega-suite.tar.gz
```

```bash
./install.sh
./omega-suite.sh
```


## 사용법
### 실행

```bash
cd ~/omega-suite
./omega-suite.sh
```

###  또는 별칭을 만들었다면 터미널에서 다음을 입력하기만 하면 됩니다:
```bash
suite
```
## 인터페이스 언어

인터페이스는 17개 언어를 지원합니다. 제품군 설정(“Langue / Language”)에서 선택하며, 인터페이스를 다시 시작하면 7개 도구 모두에 적용됩니다. 변수 `OMEGA_SUITE_LANG`으로 한 세션 동안 언어를 강제할 수 있습니다. 별도의 설정 “내보내기 언어”가 7개 도구가 내보내는 보고서의 언어를 정합니다. Linux 텍스트 콘솔(TTY)에서는 라틴 문자가 아닌 언어가 해당 세션 동안 영어로 표시됩니다. 명령줄은 프랑스어로 유지됩니다.

## 터미널 호환성

대화형 인터페이스(Textual)는 터미널의 기능(에뮬레이터, 크기)을 자동으로 감지하고 그에 맞게 구조 스타일시트(`complete`/`standard`/`reduced`/`mono`)를 조정하며, 수동 플래그가 필요 없습니다. CLI 모드는 터미널과 무관하게 항상 일반 텍스트입니다. `omega-` 도구 모음 전체가 공유하는 정책(`omega-lib`, `terminal/policies.py`) — `omega-check`/`omega-fire`와 동일합니다.

### 감지된 에뮬레이터에 따른 프로필

| 에뮬레이터 | 초기 프로필 |
|---|---|
| Ghostty, Alacritty, WezTerm, Kitty | `complete` |
| Konsole, GNOME Terminal, Terminator, Xfce4 Terminal | `standard` |
| xterm, urxvt, 최신 SSH | `reduced` |
| Linux TTY, 오래된 SSH | `mono` |
| 인식되지 않은 에뮬레이터 | `reduced`(기본 대체) |

### 터미널 크기에 따른 프로필

| 최소 크기(열 × 줄) | 프로필 상한 |
|---|---|
| 120 × 32 | `complete` |
| 100 × 28 | `standard` |
| 80 × 24 | `reduced` |
| 그 미만 | `mono` |

최종 선택되는 프로필은 **두 가지 중 더 제한적인 쪽**(에뮬레이터와 크기)입니다 — 전체 화면 Ghostty를 70열로 줄이면 에뮬레이터가 `complete`를 허용하더라도 `mono`로 내려갑니다. `r` 키로 바로 새로 고치거나, 도구 모음 설정(`s` 키)에서 수동으로 지정할 수 있습니다.

## 아키텍처

### 설계 원칙

- **조립을 위한 파사드이며 결코 8번째 비즈니스 계층이 아님**: omega-suite에는 고유한 `domain/`이 없습니다 - 각 프로젝트가 독립적으로 이미 검증한 7개 컨테이너를 조립할 뿐, 그 로직을 다시 구현하지 않습니다.
- **7개 도구의 파일은 하나도 수정하지 않습니다.** 공유 화면/위젯 클래스는 세션에서 해당 도구를 실제로 처음 열 때 단 한 번 메모리에서 패치됩니다: CSS 격리(한 도구가 다른 도구의 스타일을 물려받는 일은 없음), 도구 내부의 « 종료 »를 도구 모음의 홈 탭으로 돌리기, 그리고 이 탐색 방식이 켜져 있으면 탭 표시줄 삽입.
- **`interfaces/tui/` 밖에서 `textual` 사용 금지**(변경할 때마다 `import-linter`로 검증): `app/`은 표시와 독립적이며, 이론상 다른 인터페이스에도 쓰일 수 있습니다.
- **2단계 지연 구성**: 도구의 어댑터(코드 가져오기), 그다음 그 컨테이너(SQLite 데이터베이스, 네트워크 프로브) - 둘 다 해당 도구를 실제로 처음 방문하기 전에는 비용이 들지 않습니다.

### 데이터 구조

```text
src/omega_suite/
├── app/              조립: 지연 DependencyContainer, 부트스트랩, 7개 도구의 어댑터
│                     (tool_adapters.py), 공유 설정(테마, 렌더링 프로필, 탐색 방식)
├── infrastructure/   런타임 경로(var/), 설정 저장(JSON)
├── interfaces/
│   ├── tui/          Textual을 가져오는 유일한 곳: App, 도구 모음 고유 화면(홈, 설정,
│   │                 도움말, Splash), 7개 도구 화면의 메모리 내 패치(screen_patching.py)
│   └── cli/          예약됨, 지금은 비어 있음 - 각 도구는 고유 CLI 모드를 유지하며 직접 호출됨
└── ports/            app/이 기대하는 계약(SettingsStore)
```

## 사전 요구 사항

### 시스템

- Python 3.10+
- Linux(Textual은 다른 시스템에서도 작동하지만, 이 프로젝트는 테스트하거나 지원하지 않음)
- 어떤 터미널이든 가능 - 실제 기능이 자동으로 감지되고 렌더링이 그에 맞춰 조정됩니다(위의 « 터미널 호환성 » 참조), 단순한 TTY까지

### Python 의존성

`pyproject.toml`에 선언되어 있으며, 하나의 가상 환경이 모두를 묶습니다(`install.sh` 참조):

- `omega-lib`: 공유 라이브러리(테마, 터미널 감지, 신뢰 수준)
- `omega-scan`, `omega-check`, `omega-deep`, `omega-fold`, `omega-stress`, `omega-track`, `omega-fuzz`: 통합된 7개 도구, 각각 고유한 전이 의존성을 가짐
- `textual`: TUI 인터페이스
- 개발 의존성(`pip install -e ".[dev]"`): `pytest`, `pytest-asyncio`, `pytest-cov`, `ruff`, `mypy`, `import-linter`

### 내보내기

각 도구는 자기 내보내기를 `var/<도구>/exports/`에, 스크린샷을 `var/<도구>/screenshots/`에 씁니다 - `var/`는 omega-suite를 실행한 폴더 기준이며, `$OMEGA_SUITE_VAR_DIR`로 바꿀 수 있습니다. 이는 도구를 단독으로 실행할 때의 기본 `var/`와 결코 같지 않습니다: 두 가지 사용 방식(단독 또는 도구 모음에 통합)은 절대 섞이지 않습니다. 각 도구는 자기 설정에서 대상 폴더를 다시 지정할 수 있습니다. « 모든 내보내기 비우기 » 버튼(도구 모음 설정)은 세션에서 한 번도 열지 않은 도구까지 포함해 7개 도구의 이 폴더를 한 번에 비웁니다 - 자세한 내용은 도구 모음 도움말(홈에서 `a` 키)을 참조하십시오.

---

## 보안

- omega-suite 자체는 어떤 네트워크 요청도 하지 않으며 아무것도 스캔하지 않습니다: 7개 도구의 표시를 조율할 뿐이며, 각 도구는 고유한 안전장치를 모두 그대로 유지합니다(각각의 범위는 도구 모음 도움말이나 각자의 README 참조).
- omega-suite 자체는 비밀이나 자격 증명을 전혀 다루지 않습니다. 각 도구가 저장하는 것(고정한 대상, 기록, 고유 설정)은 각자의 하위 폴더 `var/<도구>/`에 남으며 도구 모음이 바꾸지 않습니다.
- omega-suite 고유의 유일한 상태(테마, 렌더링 프로필, 탐색 방식)는 `var/settings.json`에 있으며 민감한 데이터는 없습니다.
- `import-linter`는 변경할 때마다 `interfaces/tui/` 밖에서의 `textual` 가져오기를 금지합니다(아키텍처 참조) - 단순한 관례가 아니라 구조적 보장입니다.

## 테스트와 품질

```bash
source .venv/bin/activate
pip install -e ".[dev]"
lint-imports        # Dependency Rule 검증(interfaces/tui 밖에서 textual 금지)
pytest -q
ruff check src tests
mypy -p omega_suite
```

## 제거

omega-suite는 자기 폴더와 실행 별칭 외에는 아무것도 건드리지 않습니다:

1. `install.sh`가 `~/.bashrc`와 `~/.zshrc`에 추가한 `alias suite="..."` 줄을 지웁니다.
2. `omega-suite/` 폴더를 삭제합니다(가상 환경 `.venv/`, 데이터 `var/`, 설정 포함).

따로 설치된 7개 도구(또는 각자의 폴더에서 개발 중인 도구)는 영향을 받지 않습니다: 각 도구는 자기 README에 따라 독립적으로 설치/제거할 수 있습니다.

## 라이선스

Omega-Suite는 **MIT** 라이선스로 배포됩니다. 전체 내용은 [`LICENSE`](../../../LICENSE) 파일을 참조하십시오.

---

> **Omega-Suite — 관찰하고, 조종하고, 감사하여 더 잘 보호한다.**
>
> Omega- 스캐너를 위한 통합 TUI 인터페이스
