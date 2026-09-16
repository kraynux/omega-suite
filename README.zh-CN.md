<!-- Copyright (c) 2026 kraynux - kraynux@proton.me - MIT 许可证（见 LICENSE 文件） -->
<div align="center">
  <img src="docs/assets/omega-suite.png" alt="Omega-Suite" width="384">
</div>


#  OMEGA-SUITE

**将所有 "OMEGA" 扫描器统一到单一界面和共享库中**

> 由 **kraynux** 为 **Omega-server** 开发
[kraynux.snake-mackarel](https://kraynux.snake-mackarel.ts.net)

官方页面：[OMEGA-SUITE](https://kraynux.snake-mackarel.ts.net/omega-suite/) &nbsp; 预览：[Screenshots](https://kraynux.snake-mackarel.ts.net/omega-suite/screenshots/)  

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux-informational.svg)](https://www.linux.org/)
[![Interface](https://img.shields.io/badge/Interface-Textual%20TUI-cyan.svg)](https://github.com/Textualize/textual)

**语言：**
[Français](README.md) · [English](README.en.md) · [Español](README.es.md) · [Русский](README.ru.md) · [中文](README.zh-CN.md)
---
**Omega-Suite** 是 **omega-** 扫描器套件的统一界面：  
[omega-scan](https://github.com/kraynux/omega-scan)、[omega-check](https://github.com/kraynux/omega-check)、[omega-deep](https://github.com/kraynux/omega-deep)、[omega-fold](https://github.com/kraynux/omega-fold)、[omega-stress](https://github.com/kraynux/omega-stress)、[omega-track](https://github.com/kraynux/omega-track) 和 [omega-fuzz](https://github.com/kraynux/omega-fuzz)  
被整合进单一的 TUI 应用中（首页网格或常驻标签栏，由用户自行选择），并共享同一个库 [(`omega-lib`)](https://github.com/kraynux/omega-lib)。


每个工具依然可以完全独立运行（`omega-check scan ...` 照常可用）——
omega-suite 只是一个附加门面，而非替代品。

架构与易用性方面的详细决策请参阅
`~/DEV/SUITE/OMEGA-SUITE_SPECIFICATIONS.md` 和
`~/DEV/SUITE/DECISIONS_ARCHITECTURE.md`（D-014/D-015）。

## 概览

Omega-Suite 相当于 Omega 系列网络安全扫描器的**指挥中心**。

### 目标

- 将 7 个 **omega 扫描器**工具整合进一个统一、连贯的界面，且绝不修改或替代它们本身。
- 7 个工具共用同一主题、同一渲染配置、同一导航风格——只需配置一次，而不是配置 7 次。
- 在工具之间切换而不丢失上下文：每个工具的屏幕栈在后台始终保持完整。
- 尽管整合了 7 个工具，依然保持轻量：任何工具在首次真正打开之前都不会被加载进内存。

## 功能特性

- **单一 TUI 应用**（基于 Textual），涵盖 Omega-SCAN、-CHECK、-DEEP、-FOLD、-STRESS、-TRACK 和 -FUZZ。
- **两种可选导航风格**（在设置中切换，会立即提示重启）：来自首页的按钮网格，或即使深入某个工具内部（历史记录、某工具自己的设置等）也始终可见的常驻标签栏，无需返回首页即可切换工具。
- **惰性加载**：每个工具的代码及其依赖只在本次会话中首次打开时才会被导入——启动时间与内存占用始终与实际使用的工具数量成正比。
- **共享主题与渲染配置**：主题可对全部 7 个工具即时热切换；渲染配置和导航风格更偏结构性，修改后会直接提示立即重启 omega-suite。
- **上下文相关的帮助**：从首页可查看全局快捷键及 7 个工具的功能范围概览，从某个标签页内则显示该活动工具自身的帮助。
- **一键清空全部导出**（套件设置中），针对全部 7 个工具，即使某个工具本次会话从未被打开过。
- **7 个工具之间的严格隔离**：尽管共用同一个应用程序，样式或状态绝不会从一个工具泄漏到另一个工具。
- **每个工具依然可完全独立使用**（各自拥有独立的 TUI 与 CLI，`omega-check scan ...` 照常可用）——omega-suite 仅是一个附加门面，绝非替代品。

## 安装

官方发行包以 `.tar.gz` 格式提供。安装前请先校验其完整性：

```bash
sha256sum omega-suite.tar.gz
```

```bash
./install.sh
./omega-suite.sh
```


## 使用方法
### 启动

```bash
cd ~/omega-suite
./omega-suite.sh
```

### 或者，如果已创建别名，直接在终端输入：
```bash
suite
```
## 终端兼容性

交互式界面（Textual）会自动检测终端的能力（模拟器类型、尺寸），并据此调整其结构化样式表（`complete`/`standard`/`reduced`/`mono`），无需任何手动参数。CLI 模式则始终使用纯文本，不依赖终端环境。此策略由整个 `omega-` 套件共用（`omega-lib`、`terminal/policies.py`）——与 `omega-check`/`omega-fire` 完全一致。

### 按检测到的终端模拟器划分的配置

| 终端模拟器 | 初始配置 |
|---|---|
| Ghostty、Alacritty、WezTerm、Kitty | `complete` |
| Konsole、GNOME Terminal、Terminator、Xfce4 Terminal | `standard` |
| xterm、urxvt、较新的 SSH | `reduced` |
| Linux TTY、较旧的 SSH | `mono` |
| 无法识别的终端模拟器 | `reduced`（默认回退） |

### 按终端尺寸划分的配置

| 最小尺寸（列 × 行） | 配置上限 |
|---|---|
| 120 × 32 | `complete` |
| 100 × 28 | `standard` |
| 80 × 24 | `reduced` |
| 低于此尺寸 | `mono` |

最终采用的配置是**两者中更严格的一个**（终端模拟器与尺寸）——一个全屏运行的 Ghostty 若被缩小到 70 列，即使其模拟器本身支持 `complete`，也会回退到 `mono`。可通过 `r` 键实时刷新，或在套件设置中手动覆盖（`s` 键）。

## 架构

### 设计原则

- **组合门面，而非第 8 层业务逻辑**：omega-suite 没有自己的 `domain/` 层——它只是组装 7 个已由各自项目独立验证过的容器，绝不重新实现其内部逻辑。
- **7 个工具的任何文件都不会被修改。** 它们共用的屏幕/组件类只在该工具本次会话首次真正被打开时，在内存中被打补丁一次：CSS 隔离（一个工具绝不会继承另一个工具的样式）、将工具内部的"退出"重定向到套件的首页标签、以及在该导航风格生效时注入标签栏。
- **`textual` 被禁止出现在 `interfaces/tui/` 之外**（每次改动都由 `import-linter` 校验）：`app/` 始终独立于展示层，理论上可服务于另一种界面。
- **两级惰性构建**：先是某个工具的适配器（导入其代码），再是它的容器（SQLite 数据库、网络探测器）——在真正首次访问该特定工具之前，这两者都不会被构建。

### 数据结构

```text
src/omega_suite/
├── app/              组装层：惰性 DependencyContainer、bootstrap、7 个工具的适配器
│                     (tool_adapters.py)、共享设置（主题、渲染配置、导航风格）
├── infrastructure/   运行时路径（var/）、设置存储（JSON）
├── interfaces/
│   ├── tui/          唯一导入 Textual 的地方：App、套件自身的界面（首页、设置、
│   │                 帮助、启动画面）、对 7 个工具界面的内存打补丁（screen_patching.py）
│   └── cli/          预留，目前为空——每个工具保留自己的 CLI，直接调用
└── ports/            app/ 所期望的契约（SettingsStore）
```

## 前置条件

### 系统

- Python 3.10+
- Linux（Textual 也可在其他系统上运行，但本项目未对其进行测试或提供支持）
- 任意终端——其真实能力会被自动检测，渲染效果随之自适应（见上方"终端兼容性"），最低可退化到普通 TTY

### Python 依赖

均在 `pyproject.toml` 中声明，由单一虚拟环境统一管理（见 `install.sh`）：

- `omega-lib`：共享库（主题、终端检测、置信度等级）
- `omega-scan`、`omega-check`、`omega-deep`、`omega-fold`、`omega-stress`、`omega-track`、`omega-fuzz`：集成的 7 个工具，各自带有自己的传递依赖
- `textual`：TUI 界面
- 开发依赖（`pip install -e ".[dev]"`）：`pytest`、`pytest-asyncio`、`pytest-cov`、`ruff`、`mypy`、`import-linter`

### 导出文件

每个工具会把自己的导出文件写入 `var/<工具>/exports/`，截图写入 `var/<工具>/screenshots/`——`var/` 相对于启动 omega-suite 时所在的目录，也可通过 `$OMEGA_SUITE_VAR_DIR` 覆盖。这与单独启动该工具时默认使用的 `var/` 从不相同：独立使用与整合进套件使用这两种场景的数据绝不会混在一起。每个工具都可以在其自身的设置中重新指定导出目录。"清空所有导出"按钮（套件设置中）会一次性清空全部 7 个工具的该目录，即使某个工具本次会话从未被打开过——详情参见套件的帮助（在首页按 `a` 键）。

---

## 安全性

- omega-suite 本身不发起任何网络请求，也不扫描任何目标：它只负责编排 7 个工具的界面展示，每个工具都完整保留自己的安全防护措施（各工具具体的功能边界见套件帮助，或该工具自己的 README）。
- omega-suite 本身不处理任何密钥或凭据。每个工具存储的数据（已固定的目标、历史记录、自身设置）都保留在其自己的 `var/<工具>/` 子目录下，套件不会触碰这些数据。
- omega-suite 自身唯一拥有的状态（主题、渲染配置、导航风格）保存在 `var/settings.json` 中，不含任何敏感数据。
- `import-linter` 在每次改动时都会禁止在 `interfaces/tui/` 之外导入 `textual`（见"架构"一节）——这是一种结构性保证，而不仅仅是约定。

## 测试与代码质量

```bash
source .venv/bin/activate
pip install -e ".[dev]"
lint-imports        # 校验依赖规则（textual 禁止出现在 interfaces/tui 之外）
pytest -q
ruff check src tests
mypy -p omega_suite
```

## 卸载

omega-suite 不会触碰其自身目录和启动别名之外的任何内容：

1. 从 `~/.bashrc` 和 `~/.zshrc` 中删除由 `install.sh` 添加的 `alias suite="..."` 那一行。
2. 删除 `omega-suite/` 目录（包括虚拟环境 `.venv/`、`var/` 数据及各项设置）。

单独安装（或在各自目录中处于开发状态）的 7 个工具不受此操作影响：每个工具都可以按照自己的 README 独立安装或卸载。

## 许可证

Omega-Suite 基于 **MIT** 许可证发布。完整文本见 [`LICENSE`](LICENSE) 文件。

---

> **Omega-Suite —— 观察、掌控、审计，更好地保障安全。**
>
> 面向 Omega- 系列扫描器的统一 TUI 界面
