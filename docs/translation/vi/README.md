<!-- Copyright (c) 2026 kraynux - kraynux@proton.me - Licence MIT (voir fichier LICENSE) -->
<div align="center">
  <img src="https://raw.githubusercontent.com/kraynux/kraynux/refs/heads/main/docs/assets/omega-suite.png" alt="Omega-Suite" width="384">
</div>


#  OMEGA-SUITE

**Toàn bộ các trình quét "OMEGA" được hợp nhất trong một giao diện duy nhất và một thư viện dùng chung**

> Được phát triển bởi [kraynux](https://github.com/kraynux) cho [Omega-Server](https://kraynux.snake-mackarel.ts.net)   

Trang chính thức: [OMEGA-SUITE](https://kraynux.snake-mackarel.ts.net/omega-suite/) &nbsp;   
Ảnh chụp màn hình → [omega-scan](https://kraynux.snake-mackarel.ts.net/omega-scan/screenshots/) · [omega-check](https://kraynux.snake-mackarel.ts.net/omega-check/screenshots/) · [omega-deep](https://kraynux.snake-mackarel.ts.net/omega-deep/screenshots/) · [omega-fold](https://kraynux.snake-mackarel.ts.net/omega-fold/screenshots/) · [omega-track](https://kraynux.snake-mackarel.ts.net/omega-track/screenshots/) · [omega-fuzz](https://kraynux.snake-mackarel.ts.net/omega-fuzz/screenshots/) · [omega-stress](https://kraynux.snake-mackarel.ts.net/omega-stress/screenshots/) 

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../../LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux-informational.svg)](https://www.linux.org/)
[![Interface](https://img.shields.io/badge/Interface-Textual%20TUI-cyan.svg)](https://github.com/Textualize/textual)

**Ngôn ngữ:**
<img src="https://flagcdn.com/w20/fr.png" alt="France" style="height:14px;"> [Français](../../../README.md) · <img src="https://flagcdn.com/w20/gb.png" alt="English" style="height:14px;"> [English](../en/README.md) · <img src="https://flagcdn.com/w20/es.png" alt="Español" style="height:14px;"> [Español](../es/README.md) · <img src="https://flagcdn.com/w20/br.png" alt="Português (Brasil)" style="height:14px;"> [Português (Brasil)](../pt-BR/README.md) · <img src="https://flagcdn.com/w20/it.png" alt="Italiano" style="height:14px;"> [Italiano](../it/README.md) · <img src="https://flagcdn.com/w20/de.png" alt="Deutsch" style="height:14px;"> [Deutsch](../de/README.md) · <img src="https://flagcdn.com/w20/nl.png" alt="Nederlands" style="height:14px;"> [Nederlands](../nl/README.md) · <img src="https://flagcdn.com/w20/pl.png" alt="Polski" style="height:14px;"> [Polski](../pl/README.md) · <img src="https://flagcdn.com/w20/ru.png" alt="Русский" style="height:14px;"> [Русский](../ru/README.md) · <img src="https://flagcdn.com/w20/cn.png" alt="中文" style="height:14px;"> [中文](../zh-CN/README.md) · <img src="https://flagcdn.com/w20/vn.png" alt="Tiếng Việt" style="height:14px;"> [Tiếng Việt](README.md) · <img src="https://flagcdn.com/w20/th.png" alt="ไทย" style="height:14px;"> [ไทย](../th/README.md) · <img src="https://flagcdn.com/w20/id.png" alt="Bahasa Indonesia" style="height:14px;"> [Bahasa Indonesia](../id/README.md) · <img src="https://flagcdn.com/w20/jp.png" alt="日本語" style="height:14px;"> [日本語](../ja/README.md) · <img src="https://flagcdn.com/w20/kr.png" alt="한국어" style="height:14px;"> [한국어](../ko/README.md) · <img src="https://flagcdn.com/w20/in.png" alt="हिन्दी" style="height:14px;"> [हिन्दी](../hi/README.md) · <img src="https://flagcdn.com/w20/ae.png" alt="العربية" style="height:14px;"> [العربية](../ar/README.md)

---
**Omega-Suite** là giao diện thống nhất cho bộ công cụ quét **omega-**:  
[omega-scan](https://github.com/kraynux/omega-scan), [omega-check](https://github.com/kraynux/omega-check), [omega-deep](https://github.com/kraynux/omega-deep), [omega-fold](https://github.com/kraynux/omega-fold), [omega-stress](https://github.com/kraynux/omega-stress), [omega-track](https://github.com/kraynux/omega-track) và [omega-fuzz](https://github.com/kraynux/omega-fuzz)  
được tập hợp trong một ứng dụng TUI duy nhất (lưới ở màn hình chính hoặc thanh tab cố định, tùy lựa chọn của người dùng) cùng một thư viện dùng chung [(`omega-lib`)](https://github.com/kraynux/omega-lib).


Mỗi công cụ vẫn chạy được độc lập (`omega-check scan ...`
vẫn hoạt động) - omega-suite là một lớp mặt tiền bổ sung, không phải
sự thay thế.

Xem `~/DEV/SUITE/OMEGA-SUITE_SPECIFICATIONS.md` và
`~/DEV/SUITE/DECISIONS_ARCHITECTURE.md` (D-014/D-015) để biết chi tiết các
lựa chọn về kiến trúc và công thái học.

## Giới thiệu

Omega-Suite hoạt động như một **trạm điều khiển** các trình quét Omega cho bảo mật mạng

### Mục tiêu

- Tập hợp 7 công cụ **quét omega** trong một giao diện nhất quán, không bao giờ sửa đổi hay thay thế chúng.
- Một chủ đề, một hồ sơ hiển thị, một kiểu điều hướng cho cả 7 công cụ - cấu hình một lần thay vì 7 lần.
- Chuyển từ công cụ này sang công cụ khác mà không mất ngữ cảnh: mỗi ngăn xếp màn hình vẫn nguyên vẹn ở chế độ nền.
- Vẫn nhẹ dù tập hợp 7 công cụ: không có gì được nạp vào bộ nhớ trước lần mở thực sự đầu tiên.

## Tính năng

- **Một ứng dụng TUI duy nhất** (Textual) cho Omega-SCAN, -CHECK, -DEEP, -FOLD, -STRESS, -TRACK và -FUZZ.
- **Hai kiểu điều hướng** tùy chọn (Cài đặt, đề xuất khởi động lại ngay): lưới nút từ màn hình chính, hoặc thanh tab cố định vẫn hiển thị khi đi sâu (Lịch sử, Cài đặt của một công cụ...), không bao giờ phải quay lại màn hình chính.
- **Nạp lười**: mỗi công cụ (mã Python và phụ thuộc) chỉ được nhập ở lần mở đầu tiên trong phiên - thời gian khởi động và bộ nhớ vẫn tỷ lệ với các công cụ thực sự được dùng.
- **Chủ đề và hồ sơ hiển thị dùng chung**: chủ đề thay đổi tức thì cho cả 7 công cụ; hồ sơ hiển thị và kiểu điều hướng, mang tính cấu trúc hơn, đề xuất khởi động lại omega-suite ngay.
- **Trợ giúp theo ngữ cảnh**: phím tắt chung và tổng quan phạm vi của 7 công cụ từ màn hình chính, trợ giúp riêng của công cụ đang hoạt động từ một tab.
- **Xóa toàn bộ bản xuất** của 7 công cụ chỉ với một cú nhấp (Cài đặt của bộ), kể cả những công cụ chưa từng mở trong phiên.
- **Cô lập nghiêm ngặt giữa 7 công cụ** dù dùng chung một ứng dụng: không rò rỉ kiểu dáng hay trạng thái từ công cụ này sang công cụ khác.
- **Mỗi công cụ vẫn dùng được hoàn toàn độc lập** (TUI và CLI riêng, `omega-check scan ...` vẫn hoạt động) - omega-suite chỉ là một lớp mặt tiền bổ sung, không bao giờ là sự thay thế.

## Cài đặt

Tệp lưu trữ chính thức được cung cấp ở định dạng `.tar.gz`. Hãy kiểm tra tính toàn vẹn trước khi cài đặt:

```bash
sha256sum omega-suite.tar.gz
```

```bash
./install.sh
./omega-suite.sh
```


## Sử dụng
### Khởi chạy

```bash
cd ~/omega-suite
./omega-suite.sh
```

###  hoặc đơn giản, nếu đã tạo alias, gõ trong terminal:
```bash
suite
```
## Ngôn ngữ giao diện

Giao diện có 17 ngôn ngữ. Lựa chọn nằm trong Thiết lập của bộ công cụ (“Langue / Language”) và áp dụng cho cả 7 công cụ sau khi khởi động lại giao diện; biến `OMEGA_SUITE_LANG` buộc dùng một ngôn ngữ trong một phiên. Một thiết lập riêng, “Ngôn ngữ xuất”, quyết định ngôn ngữ của báo cáo do 7 công cụ xuất ra. Trên console văn bản Linux (TTY), các ngôn ngữ không dùng chữ Latinh được hiển thị bằng tiếng Anh trong phiên đó. Dòng lệnh vẫn bằng tiếng Pháp.

## Khả năng tương thích terminal

Giao diện tương tác (Textual) tự động phát hiện khả năng của terminal (trình giả lập, kích thước) và điều chỉnh bảng kiểu cấu trúc tương ứng (`complete`/`standard`/`reduced`/`mono`), không cần cờ thủ công. Chế độ CLI luôn là văn bản thuần, không phụ thuộc terminal. Chính sách dùng chung cho cả bộ `omega-` (`omega-lib`, `terminal/policies.py`) — giống hệt `omega-check`/`omega-fire`.

### Hồ sơ theo trình giả lập được phát hiện

| Trình giả lập | Hồ sơ ban đầu |
|---|---|
| Ghostty, Alacritty, WezTerm, Kitty | `complete` |
| Konsole, GNOME Terminal, Terminator, Xfce4 Terminal | `standard` |
| xterm, urxvt, SSH hiện đại | `reduced` |
| TTY Linux, SSH cũ | `mono` |
| Trình giả lập không nhận diện được | `reduced` (dự phòng mặc định) |

### Hồ sơ theo kích thước terminal

| Kích thước tối thiểu (cột × dòng) | Trần hồ sơ |
|---|---|
| 120 × 32 | `complete` |
| 100 × 28 | `standard` |
| 80 × 24 | `reduced` |
| nhỏ hơn | `mono` |

Hồ sơ cuối cùng được chọn là **hồ sơ hạn chế hơn trong hai** (trình giả lập và kích thước) — một Ghostty toàn màn hình bị thu nhỏ còn 70 cột sẽ hạ xuống `mono`, dù trình giả lập của nó cho phép `complete`. Có thể làm mới trực tiếp bằng phím `r`, hoặc ghi đè thủ công trong Cài đặt của bộ (phím `s`).

## Kiến trúc

### Nguyên tắc thiết kế

- **Mặt tiền tổ hợp, không bao giờ là lớp nghiệp vụ thứ 8**: omega-suite không có `domain/` riêng - nó lắp ráp 7 container mà mỗi dự án đã tự xác thực độc lập, không cài đặt lại logic của chúng.
- **Không tệp nào của 7 công cụ bị sửa đổi.** Các lớp màn hình/widget dùng chung của chúng được vá trong bộ nhớ, chỉ một lần, ở lần mở thực sự đầu tiên của công cụ đó trong phiên: cô lập CSS (một công cụ không bao giờ thừa hưởng kiểu dáng của công cụ khác), chuyển hướng « Thoát » nội bộ của công cụ về tab chính của bộ, và chèn thanh tab nếu kiểu điều hướng này đang bật.
- **Cấm `textual` bên ngoài `interfaces/tui/`** (được `import-linter` kiểm tra ở mỗi thay đổi): `app/` vẫn độc lập với hiển thị và về lý thuyết có thể phục vụ một giao diện khác.
- **Xây dựng lười hai cấp**: adapter của một công cụ (nhập mã của nó), rồi container của nó (cơ sở SQLite, đầu dò mạng) - không cái nào phải trả giá trước lần ghé thăm thực sự đầu tiên của chính công cụ đó.

### Cấu trúc dữ liệu

```text
src/omega_suite/
├── app/              Lắp ráp: DependencyContainer lười, bootstrap, adapter của 7 công cụ
│                     (tool_adapters.py), cài đặt dùng chung (chủ đề, hồ sơ hiển thị, kiểu điều hướng)
├── infrastructure/   Đường dẫn runtime (var/), lưu trữ cài đặt (JSON)
├── interfaces/
│   ├── tui/          Nơi duy nhất nhập Textual: App, các màn hình riêng của bộ (Trang chủ, Cài đặt,
│   │                 Trợ giúp, Splash), vá trong bộ nhớ các màn hình của 7 công cụ (screen_patching.py)
│   └── cli/          Dành riêng, hiện vẫn trống - mỗi công cụ giữ chế độ CLI riêng, được gọi trực tiếp
└── ports/            Các hợp đồng mà app/ mong đợi (SettingsStore)
```

## Yêu cầu

### Hệ thống

- Python 3.10+
- Linux (Textual chạy trên các hệ thống khác, không được dự án này kiểm thử hay hỗ trợ)
- Một terminal bất kỳ - khả năng thực tế của nó được phát hiện tự động và phần hiển thị tự điều chỉnh (xem « Khả năng tương thích terminal » ở trên), cho đến một TTY đơn giản

### Phụ thuộc Python

Được khai báo trong `pyproject.toml`, một môi trường ảo duy nhất gom tất cả (xem `install.sh`):

- `omega-lib`: thư viện dùng chung (chủ đề, phát hiện terminal, mức độ tin cậy)
- `omega-scan`, `omega-check`, `omega-deep`, `omega-fold`, `omega-stress`, `omega-track`, `omega-fuzz`: 7 công cụ tích hợp, mỗi công cụ có các phụ thuộc bắc cầu riêng
- `textual`: giao diện TUI
- Phụ thuộc phát triển (`pip install -e ".[dev]"`): `pytest`, `pytest-asyncio`, `pytest-cov`, `ruff`, `mypy`, `import-linter`

### Xuất dữ liệu

Mỗi công cụ ghi bản xuất riêng vào `var/<công-cụ>/exports/` và ảnh chụp màn hình vào `var/<công-cụ>/screenshots/` - `var/` tương đối với thư mục khởi chạy omega-suite, hoặc `$OMEGA_SUITE_VAR_DIR` để ghi đè. Đó không bao giờ là `var/` mặc định của công cụ khi chạy riêng: hai cách dùng (độc lập hoặc tích hợp trong bộ) không bao giờ trộn lẫn. Mỗi công cụ có thể đặt lại thư mục đích riêng trong Cài đặt của chính nó. Nút « Xóa tất cả bản xuất » (Cài đặt của bộ) làm trống thư mục này cho cả 7 công cụ cùng lúc, kể cả công cụ chưa từng mở trong phiên - xem Trợ giúp của bộ (phím `a` từ màn hình chính) để biết chi tiết.

---

## Bảo mật

- Bản thân omega-suite không gửi yêu cầu mạng nào và không quét gì cả: nó điều phối việc hiển thị 7 công cụ, mỗi công cụ giữ nguyên toàn bộ các cơ chế bảo vệ riêng (xem phạm vi của từng công cụ trong Trợ giúp của bộ, hoặc trong README riêng của chúng).
- Bản thân omega-suite không xử lý bí mật hay thông tin định danh nào. Những gì mỗi công cụ lưu trữ (mục tiêu đã ghim, lịch sử, cài đặt riêng) vẫn nằm trong thư mục con riêng `var/<công-cụ>/`, không bị bộ thay đổi.
- Trạng thái riêng duy nhất của omega-suite (chủ đề, hồ sơ hiển thị, kiểu điều hướng) nằm trong `var/settings.json`, không chứa dữ liệu nhạy cảm.
- `import-linter` cấm mọi lệnh nhập `textual` bên ngoài `interfaces/tui/` ở mỗi thay đổi (xem Kiến trúc) - một bảo đảm mang tính cấu trúc, không chỉ là quy ước.

## Kiểm thử và chất lượng

```bash
source .venv/bin/activate
pip install -e ".[dev]"
lint-imports        # kiem tra Dependency Rule (cam textual ngoai interfaces/tui)
pytest -q
ruff check src tests
mypy -p omega_suite
```

## Gỡ cài đặt

omega-suite không động đến gì ngoài thư mục của chính nó và alias khởi chạy:

1. Xóa dòng `alias suite="..."` mà `install.sh` đã thêm vào `~/.bashrc` và `~/.zshrc`.
2. Xóa thư mục `omega-suite/` (bao gồm môi trường ảo `.venv/`, dữ liệu `var/` và cài đặt).

7 công cụ được cài riêng (hoặc đang phát triển trong thư mục riêng của chúng) không bị ảnh hưởng: mỗi công cụ vẫn cài đặt/gỡ cài đặt độc lập được, theo README riêng.

## Giấy phép

Omega-Suite được phân phối theo giấy phép **MIT**. Xem tệp [`LICENSE`](../../../LICENSE) để đọc toàn văn.

---

> **Omega-Suite — Quan sát, điều khiển, kiểm toán, để bảo vệ tốt hơn.**
>
> Một giao diện TUI thống nhất cho các trình quét Omega-
