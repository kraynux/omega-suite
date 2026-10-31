<!-- Copyright (c) 2026 kraynux - kraynux@proton.me - Licence MIT (voir fichier LICENSE) -->
<div align="center">
  <img src="https://raw.githubusercontent.com/kraynux/kraynux/refs/heads/main/docs/assets/omega-suite.png" alt="Omega-Suite" width="384">
</div>


#  OMEGA-SUITE

**รวมเครื่องมือสแกน "OMEGA" ทั้งหมดไว้ในอินเทอร์เฟซเดียวและไลบรารีที่ใช้ร่วมกัน**

> พัฒนาโดย [kraynux](https://github.com/kraynux) สำหรับ [Omega-Server](https://kraynux.snake-mackarel.ts.net)   

หน้าอย่างเป็นทางการ: [OMEGA-SUITE](https://kraynux.snake-mackarel.ts.net/omega-suite/) &nbsp;   
ภาพหน้าจอ → [omega-scan](https://kraynux.snake-mackarel.ts.net/omega-scan/screenshots/) · [omega-check](https://kraynux.snake-mackarel.ts.net/omega-check/screenshots/) · [omega-deep](https://kraynux.snake-mackarel.ts.net/omega-deep/screenshots/) · [omega-fold](https://kraynux.snake-mackarel.ts.net/omega-fold/screenshots/) · [omega-track](https://kraynux.snake-mackarel.ts.net/omega-track/screenshots/) · [omega-fuzz](https://kraynux.snake-mackarel.ts.net/omega-fuzz/screenshots/) · [omega-stress](https://kraynux.snake-mackarel.ts.net/omega-stress/screenshots/) 

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../../LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux-informational.svg)](https://www.linux.org/)
[![Interface](https://img.shields.io/badge/Interface-Textual%20TUI-cyan.svg)](https://github.com/Textualize/textual)

**ภาษา:**
<img src="https://flagcdn.com/w20/fr.png" alt="France" style="height:14px;"> [Français](../../../README.md) · <img src="https://flagcdn.com/w20/gb.png" alt="English" style="height:14px;"> [English](../en/README.md) · <img src="https://flagcdn.com/w20/es.png" alt="Español" style="height:14px;"> [Español](../es/README.md) · <img src="https://flagcdn.com/w20/br.png" alt="Português (Brasil)" style="height:14px;"> [Português (Brasil)](../pt-BR/README.md) · <img src="https://flagcdn.com/w20/it.png" alt="Italiano" style="height:14px;"> [Italiano](../it/README.md) · <img src="https://flagcdn.com/w20/de.png" alt="Deutsch" style="height:14px;"> [Deutsch](../de/README.md) · <img src="https://flagcdn.com/w20/nl.png" alt="Nederlands" style="height:14px;"> [Nederlands](../nl/README.md) · <img src="https://flagcdn.com/w20/pl.png" alt="Polski" style="height:14px;"> [Polski](../pl/README.md) · <img src="https://flagcdn.com/w20/ru.png" alt="Русский" style="height:14px;"> [Русский](../ru/README.md) · <img src="https://flagcdn.com/w20/cn.png" alt="中文" style="height:14px;"> [中文](../zh-CN/README.md) · <img src="https://flagcdn.com/w20/vn.png" alt="Tiếng Việt" style="height:14px;"> [Tiếng Việt](../vi/README.md) · <img src="https://flagcdn.com/w20/th.png" alt="ไทย" style="height:14px;"> [ไทย](README.md) · <img src="https://flagcdn.com/w20/id.png" alt="Bahasa Indonesia" style="height:14px;"> [Bahasa Indonesia](../id/README.md) · <img src="https://flagcdn.com/w20/jp.png" alt="日本語" style="height:14px;"> [日本語](../ja/README.md) · <img src="https://flagcdn.com/w20/kr.png" alt="한국어" style="height:14px;"> [한국어](../ko/README.md) · <img src="https://flagcdn.com/w20/in.png" alt="हिन्दी" style="height:14px;"> [हिन्दी](../hi/README.md) · <img src="https://flagcdn.com/w20/ae.png" alt="العربية" style="height:14px;"> [العربية](../ar/README.md)

---
**Omega-Suite** เป็นอินเทอร์เฟซแบบรวมศูนย์ของชุดเครื่องมือสแกน **omega-**:  
[omega-scan](https://github.com/kraynux/omega-scan), [omega-check](https://github.com/kraynux/omega-check), [omega-deep](https://github.com/kraynux/omega-deep), [omega-fold](https://github.com/kraynux/omega-fold), [omega-stress](https://github.com/kraynux/omega-stress), [omega-track](https://github.com/kraynux/omega-track) และ [omega-fuzz](https://github.com/kraynux/omega-fuzz)  
รวมอยู่ในแอปพลิเคชัน TUI เดียว (ตารางปุ่มบนหน้าหลัก หรือแถบแท็บถาวร ตามที่ผู้ใช้เลือก) พร้อมไลบรารีที่ใช้ร่วมกัน [(`omega-lib`)](https://github.com/kraynux/omega-lib)


เครื่องมือแต่ละตัวยังรันแยกได้อย่างอิสระ (`omega-check scan ...`
ยังใช้งานได้) - omega-suite เป็นส่วนหน้าเพิ่มเติม ไม่ใช่
สิ่งทดแทน

ดู `~/DEV/SUITE/OMEGA-SUITE_SPECIFICATIONS.md` และ
`~/DEV/SUITE/DECISIONS_ARCHITECTURE.md` (D-014/D-015) สำหรับรายละเอียดของ
การตัดสินใจด้านสถาปัตยกรรมและการใช้งาน

## ภาพรวม

Omega-Suite ทำหน้าที่เป็น **ศูนย์ควบคุม** เครื่องมือสแกน Omega สำหรับความปลอดภัยเครือข่าย

### เป้าหมาย

- รวมเครื่องมือ **สแกน omega** ทั้ง 7 ตัวไว้ในอินเทอร์เฟซที่สอดคล้องกัน โดยไม่แก้ไขหรือแทนที่เครื่องมือเหล่านั้นเลย
- ธีมเดียว โปรไฟล์การแสดงผลเดียว รูปแบบการนำทางเดียวสำหรับทั้ง 7 เครื่องมือ - ตั้งค่าครั้งเดียวแทนที่จะ 7 ครั้ง
- สลับจากเครื่องมือหนึ่งไปอีกเครื่องมือหนึ่งโดยไม่สูญเสียบริบท: สแตกหน้าจอแต่ละชุดยังคงอยู่ครบในเบื้องหลัง
- ยังคงเบาแม้จะรวม 7 เครื่องมือ: ไม่มีอะไรถูกโหลดเข้าหน่วยความจำก่อนการเปิดใช้จริงครั้งแรก

## ฟีเจอร์

- **แอปพลิเคชัน TUI เดียว** (Textual) สำหรับ Omega-SCAN, -CHECK, -DEEP, -FOLD, -STRESS, -TRACK และ -FUZZ
- **การนำทางสองรูปแบบ** ให้เลือก (การตั้งค่า เสนอให้เริ่มใหม่ทันที): ตารางปุ่มจากหน้าหลัก หรือแถบแท็บถาวรที่มองเห็นได้แม้อยู่ลึก (ประวัติ, การตั้งค่าของเครื่องมือ...) โดยไม่ต้องกลับไปหน้าหลักเลย
- **การโหลดแบบเลื่อนเวลา**: เครื่องมือแต่ละตัว (โค้ด Python และการพึ่งพา) จะถูกนำเข้าเมื่อเปิดครั้งแรกสุดในเซสชันเท่านั้น - เวลาเริ่มต้นและหน่วยความจำจึงเป็นสัดส่วนกับเครื่องมือที่ใช้จริง
- **ธีมและโปรไฟล์การแสดงผลที่ใช้ร่วมกัน**: ธีมเปลี่ยนแบบทันทีสำหรับทั้ง 7 เครื่องมือพร้อมกัน ส่วนโปรไฟล์การแสดงผลและรูปแบบการนำทางซึ่งเป็นเชิงโครงสร้างมากกว่า จะเสนอให้เริ่ม omega-suite ใหม่ทันที
- **ความช่วยเหลือตามบริบท**: คีย์ลัดส่วนกลางและภาพรวมขอบเขตของ 7 เครื่องมือจากหน้าหลัก ความช่วยเหลือเฉพาะของเครื่องมือที่ใช้งานอยู่จากแท็บ
- **ล้างไฟล์ส่งออกทั้งหมด** ของ 7 เครื่องมือในคลิกเดียว (การตั้งค่าของชุด) แม้แต่เครื่องมือที่ไม่เคยเปิดในเซสชัน
- **การแยกอย่างเข้มงวดระหว่าง 7 เครื่องมือ** แม้จะใช้แอปพลิเคชันเดียวกัน: ไม่มีการรั่วไหลของรูปแบบหรือสถานะจากเครื่องมือหนึ่งไปอีกเครื่องมือหนึ่ง
- **เครื่องมือแต่ละตัวยังใช้งานได้อย่างอิสระเต็มที่** (มี TUI และ CLI ของตัวเอง `omega-check scan ...` ยังใช้งานได้) - omega-suite เป็นเพียงส่วนหน้าเพิ่มเติม ไม่ใช่สิ่งทดแทน

## การติดตั้ง

ไฟล์เก็บถาวรอย่างเป็นทางการอยู่ในรูปแบบ `.tar.gz` ตรวจสอบความสมบูรณ์ก่อนติดตั้ง:

```bash
sha256sum omega-suite.tar.gz
```

```bash
./install.sh
./omega-suite.sh
```


## การใช้งาน
### การเปิดใช้งาน

```bash
cd ~/omega-suite
./omega-suite.sh
```

###  หรือเพียงแค่ หากสร้าง alias แล้ว ให้พิมพ์ในเทอร์มินัล:
```bash
suite
```
## ภาษาของอินเทอร์เฟซ

อินเทอร์เฟซมีให้ใช้ 17 ภาษา เลือกได้ในการตั้งค่าของชุดเครื่องมือ (“Langue / Language”) และมีผลกับเครื่องมือทั้ง 7 หลังเริ่มอินเทอร์เฟซใหม่ ตัวแปร `OMEGA_SUITE_LANG` ใช้บังคับภาษาสำหรับหนึ่งเซสชัน การตั้งค่าแยกต่างหาก “ภาษาของการส่งออก” กำหนดภาษาของรายงานที่เครื่องมือทั้ง 7 ส่งออก บนคอนโซลข้อความของ Linux (TTY) ภาษาที่ไม่ใช้อักษรละตินจะแสดงเป็นภาษาอังกฤษในเซสชันนั้น บรรทัดคำสั่งยังคงเป็นภาษาฝรั่งเศส

## ความเข้ากันได้ของเทอร์มินัล

อินเทอร์เฟซแบบโต้ตอบ (Textual) ตรวจหาความสามารถของเทอร์มินัล (อีมูเลเตอร์ ขนาด) โดยอัตโนมัติ และปรับสไตล์ชีตเชิงโครงสร้างให้เหมาะสม (`complete`/`standard`/`reduced`/`mono`) โดยไม่ต้องใช้แฟล็กเอง โหมด CLI จะเป็นข้อความธรรมดาเสมอ ไม่ขึ้นกับเทอร์มินัล นโยบายนี้ใช้ร่วมกันทั้งชุด `omega-` (`omega-lib`, `terminal/policies.py`) — เหมือนกับของ `omega-check`/`omega-fire`

### โปรไฟล์ตามอีมูเลเตอร์ที่ตรวจพบ

| อีมูเลเตอร์ | โปรไฟล์เริ่มต้น |
|---|---|
| Ghostty, Alacritty, WezTerm, Kitty | `complete` |
| Konsole, GNOME Terminal, Terminator, Xfce4 Terminal | `standard` |
| xterm, urxvt, SSH รุ่นใหม่ | `reduced` |
| Linux TTY, SSH รุ่นเก่า | `mono` |
| อีมูเลเตอร์ที่ไม่รู้จัก | `reduced` (ค่าสำรองเริ่มต้น) |

### โปรไฟล์ตามขนาดเทอร์มินัล

| ขนาดขั้นต่ำ (คอลัมน์ × บรรทัด) | เพดานโปรไฟล์ |
|---|---|
| 120 × 32 | `complete` |
| 100 × 28 | `standard` |
| 80 × 24 | `reduced` |
| ต่ำกว่านั้น | `mono` |

โปรไฟล์สุดท้ายที่เลือกคือ **โปรไฟล์ที่เข้มงวดกว่าในสองแบบ** (อีมูเลเตอร์และขนาด) — Ghostty แบบเต็มจอที่ถูกย่อเหลือ 70 คอลัมน์จะลดลงเป็น `mono` แม้อีมูเลเตอร์ของมันจะอนุญาต `complete` ก็ตาม รีเฟรชได้ทันทีด้วยปุ่ม `r` หรือกำหนดเองได้จากการตั้งค่าของชุด (ปุ่ม `s`)

## สถาปัตยกรรม

### หลักการออกแบบ

- **ส่วนหน้าสำหรับการประกอบ ไม่ใช่ชั้นธุรกิจชั้นที่ 8**: omega-suite ไม่มี `domain/` ของตัวเอง - มันประกอบคอนเทนเนอร์ 7 ชุดที่แต่ละโปรเจกต์ตรวจสอบแล้วอย่างอิสระ โดยไม่เขียนตรรกะของพวกมันขึ้นใหม่
- **ไม่มีไฟล์ใดของ 7 เครื่องมือถูกแก้ไข** คลาสหน้าจอ/วิดเจ็ตที่ใช้ร่วมกันของพวกมันถูกแพตช์ในหน่วยความจำเพียงครั้งเดียว เมื่อเปิดเครื่องมือนั้นจริงครั้งแรกในเซสชัน: การแยก CSS (เครื่องมือหนึ่งไม่สามารถรับสไตล์ของอีกเครื่องมือหนึ่งได้เลย) การเปลี่ยนเส้นทาง « ออก » ภายในของเครื่องมือไปยังแท็บหน้าหลักของชุด และการแทรกแถบแท็บหากรูปแบบการนำทางนี้เปิดอยู่
- **ห้ามใช้ `textual` นอก `interfaces/tui/`** (ตรวจสอบโดย `import-linter` ทุกครั้งที่แก้ไข): `app/` จึงเป็นอิสระจากการแสดงผล และในทางทฤษฎีสามารถให้บริการอินเทอร์เฟซอื่นได้
- **การสร้างแบบเลื่อนเวลาสองระดับ**: อะแดปเตอร์ของเครื่องมือ (การนำเข้าโค้ด) แล้วจึงคอนเทนเนอร์ของมัน (ฐาน SQLite, เซนเซอร์เครือข่าย) - ไม่มีส่วนใดต้องจ่ายต้นทุนก่อนการเข้าใช้เครื่องมือนั้นจริงครั้งแรก

### โครงสร้างข้อมูล

```text
src/omega_suite/
├── app/              การประกอบ: DependencyContainer แบบเลื่อนเวลา, bootstrap, อะแดปเตอร์ของ 7 เครื่องมือ
│                     (tool_adapters.py), การตั้งค่าที่ใช้ร่วมกัน (ธีม, โปรไฟล์การแสดงผล, รูปแบบการนำทาง)
├── infrastructure/   พาธรันไทม์ (var/), การจัดเก็บการตั้งค่า (JSON)
├── interfaces/
│   ├── tui/          ที่เดียวที่นำเข้า Textual: App, หน้าจอของชุดเอง (หน้าหลัก, การตั้งค่า,
│   │                 ความช่วยเหลือ, Splash), แพตช์ในหน่วยความจำของหน้าจอ 7 เครื่องมือ (screen_patching.py)
│   └── cli/          สงวนไว้ ยังว่างอยู่ - เครื่องมือแต่ละตัวมีโหมด CLI ของตัวเอง เรียกใช้โดยตรง
└── ports/            สัญญาที่ app/ คาดหวัง (SettingsStore)
```

## ข้อกำหนดเบื้องต้น

### ระบบ

- Python 3.10+
- Linux (Textual ทำงานบนระบบอื่นได้ แต่โปรเจกต์นี้ไม่ได้ทดสอบหรือรองรับ)
- เทอร์มินัลใดก็ได้ - ความสามารถจริงของมันจะถูกตรวจหาโดยอัตโนมัติ และการแสดงผลจะปรับตาม (ดู « ความเข้ากันได้ของเทอร์มินัล » ด้านบน) ไปจนถึง TTY ธรรมดา

### การพึ่งพาของ Python

ประกาศไว้ใน `pyproject.toml` โดยมีสภาพแวดล้อมเสมือนเดียวรวมทั้งหมด (ดู `install.sh`):

- `omega-lib`: ไลบรารีที่ใช้ร่วมกัน (ธีม, การตรวจหาเทอร์มินัล, ระดับความเชื่อมั่น)
- `omega-scan`, `omega-check`, `omega-deep`, `omega-fold`, `omega-stress`, `omega-track`, `omega-fuzz`: เครื่องมือ 7 ตัวที่ผสานรวม แต่ละตัวมีการพึ่งพาแบบส่งต่อของตัวเอง
- `textual`: อินเทอร์เฟซ TUI
- การพึ่งพาสำหรับการพัฒนา (`pip install -e ".[dev]"`): `pytest`, `pytest-asyncio`, `pytest-cov`, `ruff`, `mypy`, `import-linter`

### การส่งออก

เครื่องมือแต่ละตัวเขียนไฟล์ส่งออกของตัวเองไว้ใน `var/<เครื่องมือ>/exports/` และภาพหน้าจอไว้ใน `var/<เครื่องมือ>/screenshots/` - `var/` สัมพันธ์กับโฟลเดอร์ที่เปิด omega-suite หรือใช้ `$OMEGA_SUITE_VAR_DIR` เพื่อกำหนดเอง ซึ่งไม่ใช่ `var/` เริ่มต้นของเครื่องมือเมื่อรันเดี่ยว: การใช้งานสองแบบ (อิสระหรือรวมในชุด) จะไม่ปะปนกันเลย เครื่องมือแต่ละตัวสามารถกำหนดโฟลเดอร์ปลายทางของตัวเองใหม่จากการตั้งค่าของตัวเอง ปุ่ม « ล้างไฟล์ส่งออกทั้งหมด » (การตั้งค่าของชุด) จะล้างโฟลเดอร์นี้สำหรับทั้ง 7 เครื่องมือในครั้งเดียว แม้แต่เครื่องมือที่ไม่เคยเปิดในเซสชัน - ดูรายละเอียดในความช่วยเหลือของชุด (ปุ่ม `a` จากหน้าหลัก)

---

## ความปลอดภัย

- omega-suite เองไม่ส่งคำขอเครือข่ายใด ๆ และไม่สแกนอะไรเลย: มันจัดการการแสดงผลของ 7 เครื่องมือ ซึ่งแต่ละตัวยังคงมีมาตรการป้องกันของตัวเองครบถ้วน (ดูขอบเขตของแต่ละตัวในความช่วยเหลือของชุด หรือใน README ของแต่ละตัว)
- omega-suite เองไม่จัดการความลับหรือข้อมูลระบุตัวตนใด ๆ สิ่งที่เครื่องมือแต่ละตัวจัดเก็บ (เป้าหมายที่ปักหมุด ประวัติ การตั้งค่าของตัวเอง) ยังคงอยู่ในโฟลเดอร์ย่อย `var/<เครื่องมือ>/` ของตัวเอง โดยชุดไม่เปลี่ยนแปลง
- สถานะเดียวที่เป็นของ omega-suite (ธีม, โปรไฟล์การแสดงผล, รูปแบบการนำทาง) อยู่ใน `var/settings.json` โดยไม่มีข้อมูลที่ละเอียดอ่อน
- `import-linter` ห้ามนำเข้า `textual` นอก `interfaces/tui/` ทุกครั้งที่แก้ไข (ดูสถาปัตยกรรม) - เป็นการรับประกันเชิงโครงสร้าง ไม่ใช่แค่ข้อตกลง

## การทดสอบและคุณภาพ

```bash
source .venv/bin/activate
pip install -e ".[dev]"
lint-imports        # ตรวจ Dependency Rule (ห้าม textual นอก interfaces/tui)
pytest -q
ruff check src tests
mypy -p omega_suite
```

## การถอนการติดตั้ง

omega-suite ไม่แตะต้องสิ่งใดนอกโฟลเดอร์ของตัวเองและ alias สำหรับเปิดใช้งาน:

1. ลบบรรทัด `alias suite="..."` ที่ `install.sh` เพิ่มไว้ใน `~/.bashrc` และ `~/.zshrc`
2. ลบโฟลเดอร์ `omega-suite/` (รวมสภาพแวดล้อมเสมือน `.venv/` ข้อมูล `var/` และการตั้งค่า)

เครื่องมือ 7 ตัวที่ติดตั้งแยก (หรือที่กำลังพัฒนาในโฟลเดอร์ของตัวเอง) จะไม่ได้รับผลกระทบ: แต่ละตัวยังติดตั้ง/ถอนการติดตั้งได้อย่างอิสระตาม README ของตัวเอง

## สัญญาอนุญาต

Omega-Suite เผยแพร่ภายใต้สัญญาอนุญาต **MIT** ดูข้อความฉบับเต็มในไฟล์ [`LICENSE`](../../../LICENSE)

---

> **Omega-Suite — สังเกต ควบคุม ตรวจสอบ เพื่อปกป้องได้ดีกว่า**
>
> อินเทอร์เฟซ TUI แบบรวมศูนย์สำหรับเครื่องมือสแกน Omega-
