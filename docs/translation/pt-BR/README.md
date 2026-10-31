<!-- Copyright (c) 2026 kraynux - kraynux@proton.me - Licence MIT (voir fichier LICENSE) -->
<div align="center">
  <img src="https://raw.githubusercontent.com/kraynux/kraynux/refs/heads/main/docs/assets/omega-suite.png" alt="Omega-Suite" width="384">
</div>


#  OMEGA-SUITE

**O conjunto dos scanners "OMEGA" reunidos em uma única interface e uma biblioteca compartilhada**

> Desenvolvido por [kraynux](https://github.com/kraynux) para [Omega-Server](https://kraynux.snake-mackarel.ts.net)   

Página oficial: [OMEGA-SUITE](https://kraynux.snake-mackarel.ts.net/omega-suite/) &nbsp;   
Capturas de tela → [omega-scan](https://kraynux.snake-mackarel.ts.net/omega-scan/screenshots/) · [omega-check](https://kraynux.snake-mackarel.ts.net/omega-check/screenshots/) · [omega-deep](https://kraynux.snake-mackarel.ts.net/omega-deep/screenshots/) · [omega-fold](https://kraynux.snake-mackarel.ts.net/omega-fold/screenshots/) · [omega-track](https://kraynux.snake-mackarel.ts.net/omega-track/screenshots/) · [omega-fuzz](https://kraynux.snake-mackarel.ts.net/omega-fuzz/screenshots/) · [omega-stress](https://kraynux.snake-mackarel.ts.net/omega-stress/screenshots/) 

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../../LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux-informational.svg)](https://www.linux.org/)
[![Interface](https://img.shields.io/badge/Interface-Textual%20TUI-cyan.svg)](https://github.com/Textualize/textual)

**Idiomas:**
<img src="https://flagcdn.com/w20/fr.png" alt="France" style="height:14px;"> [Français](../../../README.md) · <img src="https://flagcdn.com/w20/gb.png" alt="English" style="height:14px;"> [English](../en/README.md) · <img src="https://flagcdn.com/w20/es.png" alt="Español" style="height:14px;"> [Español](../es/README.md) · <img src="https://flagcdn.com/w20/br.png" alt="Português (Brasil)" style="height:14px;"> [Português (Brasil)](README.md) · <img src="https://flagcdn.com/w20/it.png" alt="Italiano" style="height:14px;"> [Italiano](../it/README.md) · <img src="https://flagcdn.com/w20/de.png" alt="Deutsch" style="height:14px;"> [Deutsch](../de/README.md) · <img src="https://flagcdn.com/w20/nl.png" alt="Nederlands" style="height:14px;"> [Nederlands](../nl/README.md) · <img src="https://flagcdn.com/w20/pl.png" alt="Polski" style="height:14px;"> [Polski](../pl/README.md) · <img src="https://flagcdn.com/w20/ru.png" alt="Русский" style="height:14px;"> [Русский](../ru/README.md) · <img src="https://flagcdn.com/w20/cn.png" alt="中文" style="height:14px;"> [中文](../zh-CN/README.md) · <img src="https://flagcdn.com/w20/vn.png" alt="Tiếng Việt" style="height:14px;"> [Tiếng Việt](../vi/README.md) · <img src="https://flagcdn.com/w20/th.png" alt="ไทย" style="height:14px;"> [ไทย](../th/README.md) · <img src="https://flagcdn.com/w20/id.png" alt="Bahasa Indonesia" style="height:14px;"> [Bahasa Indonesia](../id/README.md) · <img src="https://flagcdn.com/w20/jp.png" alt="日本語" style="height:14px;"> [日本語](../ja/README.md) · <img src="https://flagcdn.com/w20/kr.png" alt="한국어" style="height:14px;"> [한국어](../ko/README.md) · <img src="https://flagcdn.com/w20/in.png" alt="हिन्दी" style="height:14px;"> [हिन्दी](../hi/README.md) · <img src="https://flagcdn.com/w20/ae.png" alt="العربية" style="height:14px;"> [العربية](../ar/README.md)

---
**Omega-Suite** é uma interface unificada da suíte de ferramentas scanners **omega-**:  
[omega-scan](https://github.com/kraynux/omega-scan), [omega-check](https://github.com/kraynux/omega-check), [omega-deep](https://github.com/kraynux/omega-deep), [omega-fold](https://github.com/kraynux/omega-fold), [omega-stress](https://github.com/kraynux/omega-stress), [omega-track](https://github.com/kraynux/omega-track) e [omega-fuzz](https://github.com/kraynux/omega-fuzz)  
reunidas em um único aplicativo TUI (grade na tela inicial ou barra de abas persistente, conforme a escolha do usuário) com uma biblioteca compartilhada [(`omega-lib`)](https://github.com/kraynux/omega-lib).


Cada ferramenta continua executável de forma autônoma (`omega-check scan ...`
continua funcionando) - o omega-suite é uma fachada adicional, não uma
substituição.

Veja `~/DEV/SUITE/OMEGA-SUITE_SPECIFICATIONS.md` e
`~/DEV/SUITE/DECISIONS_ARCHITECTURE.md` (D-014/D-015) para o detalhe das
escolhas de arquitetura e de ergonomia.

## Apresentação

O Omega-Suite atua como um **posto de comando** dos scanners Omega para a segurança de rede

### Objetivos

- Reunir as 7 ferramentas **scanners omega** em uma interface coerente, sem nunca modificá-las nem substituí-las.
- Um único tema, um único perfil de renderização, um único estilo de navegação para as 7 ferramentas - configurados uma vez, em vez de 7 vezes.
- Passar de uma ferramenta para outra sem perder o contexto: cada pilha de telas permanece intacta em segundo plano.
- Continuar leve apesar das 7 ferramentas reunidas: nada é carregado na memória antes da primeira abertura real.

## Funcionalidades

- **Um único aplicativo TUI** (Textual) para Omega-SCAN, -CHECK, -DEEP, -FOLD, -STRESS, -TRACK e -FUZZ.
- **Dois estilos de navegação** à escolha (Configurações, reinício proposto imediatamente): grade de botões a partir da tela inicial, ou barra de abas persistente visível mesmo em profundidade (Histórico, Configurações de uma ferramenta...), sem nunca voltar à tela inicial.
- **Carregamento preguiçoso**: cada ferramenta (código Python e dependências) só é importada na sua primeiríssima abertura na sessão - o tempo de inicialização e a memória continuam proporcionais às ferramentas realmente usadas.
- **Tema e perfil de renderização compartilhados**: o tema muda a quente para as 7 ferramentas ao mesmo tempo; o perfil de renderização e o estilo de navegação, mais estruturais, propõem reiniciar o omega-suite na hora.
- **Ajuda contextual**: atalhos globais e panorama do escopo das 7 ferramentas a partir da tela inicial, ajuda própria da ferramenta ativa a partir de uma aba.
- **Limpeza global das exportações** das 7 ferramentas em um clique (Configurações da suíte), mesmo das que nunca foram abertas na sessão.
- **Isolamento estrito entre as 7 ferramentas** apesar de compartilharem um único aplicativo: nenhum vazamento de estilo nem de estado de uma ferramenta para outra.
- **Cada ferramenta continua utilizável com total autonomia** (TUI e CLI próprias, `omega-check scan ...` continua funcionando) - o omega-suite é apenas uma fachada adicional, nunca uma substituição.

## Instalação

O arquivo oficial é fornecido no formato `.tar.gz`. Verifique sua integridade antes da instalação:

```bash
sha256sum omega-suite.tar.gz
```

```bash
./install.sh
./omega-suite.sh
```


## Uso
### Inicialização

```bash
cd ~/omega-suite
./omega-suite.sh
```

###  ou simplesmente, se o alias tiver sido criado, digite no terminal:
```bash
suite
```
## Idiomas da interface

A interface está disponível em 17 idiomas. A escolha é feita nas Configurações da suíte (“Langue / Language”) e vale para as 7 ferramentas após reiniciar a interface; a variável `OMEGA_SUITE_LANG` força um idioma durante uma sessão. Uma configuração separada, “Idioma das exportações”, define o idioma dos relatórios exportados pelas 7 ferramentas. Em um console de texto Linux (TTY), os idiomas de escrita não latina são exibidos em inglês durante a sessão. A linha de comando continua em francês.

## Compatibilidade de terminais

A interface interativa (Textual) detecta automaticamente as capacidades do terminal (emulador, tamanho) e adapta sua folha de estilo estrutural de acordo (`complete`/`standard`/`reduced`/`mono`), sem flag manual. O modo CLI continua sempre em texto simples, independente do terminal. Política compartilhada por toda a suíte `omega-` (`omega-lib`, `terminal/policies.py`) — idêntica à do `omega-check`/`omega-fire`.

### Perfil conforme o emulador detectado

| Emulador | Perfil inicial |
|---|---|
| Ghostty, Alacritty, WezTerm, Kitty | `complete` |
| Konsole, GNOME Terminal, Terminator, Xfce4 Terminal | `standard` |
| xterm, urxvt, SSH moderno | `reduced` |
| TTY Linux, SSH antigo | `mono` |
| Emulador não reconhecido | `reduced` (padrão de recuo) |

### Perfil conforme o tamanho do terminal

| Tamanho mínimo (colunas × linhas) | Teto de perfil |
|---|---|
| 120 × 32 | `complete` |
| 100 × 28 | `standard` |
| 80 × 24 | `reduced` |
| abaixo disso | `mono` |

O perfil final escolhido é **o mais restritivo dos dois** (emulador e tamanho) — um Ghostty em tela cheia redimensionado para 70 colunas cai para `mono`, mesmo que seu emulador permitisse `complete`. Pode ser atualizado ao vivo pela tecla `r`, ou substituído manualmente nas Configurações da suíte (tecla `s`).

## Arquitetura

### Princípios de design

- **Fachada de composição, nunca uma 8ª camada de negócio**: o omega-suite não tem `domain/` próprio - ele monta os 7 contêineres já validados de forma independente por cada projeto, sem reimplementar sua lógica.
- **Nenhum arquivo das 7 ferramentas é modificado.** Suas classes de telas/widgets compartilhados são corrigidas em memória, uma única vez, na primeira abertura real dessa ferramenta na sessão: isolamento de CSS (uma ferramenta nunca herda o estilo de outra), redirecionamento do « Sair » interno da ferramenta para a aba inicial da suíte, e injeção da barra de abas se esse estilo de navegação estiver ativo.
- **`textual` proibido fora de `interfaces/tui/`** (verificado pelo `import-linter` a cada modificação): `app/` permanece independente da exibição e poderia, em teoria, servir a outra interface.
- **Construção preguiçosa em dois níveis**: o adaptador de uma ferramenta (importação do seu código), depois seu contêiner (base SQLite, sondas de rede) - nenhum dos dois é pago antes da primeira visita real a essa ferramenta específica.

### Estrutura dos dados

```text
src/omega_suite/
├── app/              Montagem: DependencyContainer preguiçoso, bootstrap, adaptadores das 7 ferramentas
│                     (tool_adapters.py), configurações compartilhadas (tema, perfil de renderização, estilo de navegação)
├── infrastructure/   Caminhos de runtime (var/), armazenamento das configurações (JSON)
├── interfaces/
│   ├── tui/          Único lugar que importa o Textual: App, telas próprias da suíte (Início, Configurações,
│   │                 Ajuda, Splash), patch em memória das telas das 7 ferramentas (screen_patching.py)
│   └── cli/          Reservado, vazio até agora - cada ferramenta mantém seu próprio modo CLI, chamado diretamente
└── ports/            Contratos esperados por app/ (SettingsStore)
```

## Pré-requisitos

### Sistema

- Python 3.10+
- Linux (o Textual funciona em outros sistemas, não testados nem suportados por este projeto)
- Um terminal, qualquer que seja - suas capacidades reais são detectadas automaticamente e a renderização se adapta (veja « Compatibilidade de terminais » acima), até um simples TTY

### Dependências Python

Declaradas em `pyproject.toml`, um único ambiente virtual reúne todas elas (veja `install.sh`):

- `omega-lib`: biblioteca compartilhada (temas, detecção de terminal, níveis de confiança)
- `omega-scan`, `omega-check`, `omega-deep`, `omega-fold`, `omega-stress`, `omega-track`, `omega-fuzz`: as 7 ferramentas integradas, cada uma com suas próprias dependências transitivas
- `textual`: interface TUI
- Dependências de desenvolvimento (`pip install -e ".[dev]"`): `pytest`, `pytest-asyncio`, `pytest-cov`, `ruff`, `mypy`, `import-linter`

### Exportações

Cada ferramenta grava suas próprias exportações em `var/<ferramenta>/exports/` e suas capturas de tela em `var/<ferramenta>/screenshots/` - `var/` relativo à pasta onde o omega-suite foi iniciado, ou `$OMEGA_SUITE_VAR_DIR` para substituí-lo. Nunca é o `var/` padrão da ferramenta iniciada sozinha: os dois usos (autônomo ou integrado à suíte) nunca se misturam. Cada ferramenta pode redefinir sua própria pasta de destino nas próprias Configurações. O botão « Esvaziar todas as exportações » (Configurações da suíte) esvazia essa pasta para as 7 ferramentas de uma vez, mesmo as nunca abertas na sessão - veja a Ajuda da suíte (tecla `a` a partir da tela inicial) para o detalhe.

---

## Segurança

- O próprio omega-suite não faz nenhuma requisição de rede e não escaneia nada: ele orquestra a exibição das 7 ferramentas, e cada uma mantém integralmente suas próprias salvaguardas (veja o escopo de cada uma na Ajuda da suíte, ou no próprio README).
- Nenhum segredo nem identificador é manipulado pelo próprio omega-suite. O que cada ferramenta armazena (alvos fixados, histórico, configurações próprias) permanece em sua própria subpasta `var/<ferramenta>/`, sem alteração pela suíte.
- O único estado próprio do omega-suite (tema, perfil de renderização, estilo de navegação) fica em `var/settings.json`, sem dado sensível.
- O `import-linter` proíbe qualquer importação de `textual` fora de `interfaces/tui/` a cada modificação (veja Arquitetura) - uma garantia estrutural, não uma simples convenção.

## Testes e qualidade

```bash
source .venv/bin/activate
pip install -e ".[dev]"
lint-imports        # verifica a Dependency Rule (textual proibido fora de interfaces/tui)
pytest -q
ruff check src tests
mypy -p omega_suite
```

## Desinstalação

O omega-suite não toca em nada fora de sua própria pasta e do alias de inicialização:

1. Remover a linha `alias suite="..."` adicionada pelo `install.sh` em `~/.bashrc` e `~/.zshrc`.
2. Excluir a pasta `omega-suite/` (ambiente virtual `.venv/`, dados `var/` e configurações incluídos).

As 7 ferramentas instaladas separadamente (ou em desenvolvimento em suas próprias pastas) não são afetadas: cada uma continua instalável/desinstalável de forma independente, seguindo seu próprio README.

## Licença

O Omega-Suite é distribuído sob a licença **MIT**. Consulte o arquivo [`LICENSE`](../../../LICENSE) para o texto completo.

---

> **Omega-Suite — Observar, pilotar, auditar, para proteger melhor.**
>
> Uma interface TUI unificada para os scanners Omega-
