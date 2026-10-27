<!-- Copyright (c) 2026 kraynux - kraynux@proton.me - Licence MIT (voir fichier LICENSE) -->
<div align="center">
  <img src="https://raw.githubusercontent.com/kraynux/kraynux/refs/heads/main/docs/assets/omega-suite.png" alt="Omega-Suite" width="384">
</div>


#  OMEGA-SUITE

**Seluruh pemindai "OMEGA" disatukan dalam satu antarmuka dan pustaka bersama**

> Dikembangkan oleh **kraynux** untuk **Omega-server** 
[kraynux.snake-mackarel](https://kraynux.snake-mackarel.ts.net)

Halaman resmi: [OMEGA-SUITE](https://kraynux.snake-mackarel.ts.net/omega-suite/) &nbsp;   
Tangkapan layar → [omega-scan](https://kraynux.snake-mackarel.ts.net/omega-scan/screenshots/) · [omega-check](https://kraynux.snake-mackarel.ts.net/omega-check/screenshots/) · [omega-deep](https://kraynux.snake-mackarel.ts.net/omega-deep/screenshots/) · [omega-fold](https://kraynux.snake-mackarel.ts.net/omega-fold/screenshots/) · [omega-track](https://kraynux.snake-mackarel.ts.net/omega-track/screenshots/) · [omega-fuzz](https://kraynux.snake-mackarel.ts.net/omega-fuzz/screenshots/) · [omega-stress](https://kraynux.snake-mackarel.ts.net/omega-stress/screenshots/) 

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../../LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux-informational.svg)](https://www.linux.org/)
[![Interface](https://img.shields.io/badge/Interface-Textual%20TUI-cyan.svg)](https://github.com/Textualize/textual)

**Bahasa:**
<img src="https://flagcdn.com/w20/fr.png" alt="France" style="height:14px;"> [Français](../../../README.md) · <img src="https://flagcdn.com/w20/gb.png" alt="English" style="height:14px;"> [English](../en/README.md) · <img src="https://flagcdn.com/w20/es.png" alt="Español" style="height:14px;"> [Español](../es/README.md) · <img src="https://flagcdn.com/w20/br.png" alt="Português (Brasil)" style="height:14px;"> [Português (Brasil)](../pt-BR/README.md) · <img src="https://flagcdn.com/w20/it.png" alt="Italiano" style="height:14px;"> [Italiano](../it/README.md) · <img src="https://flagcdn.com/w20/de.png" alt="Deutsch" style="height:14px;"> [Deutsch](../de/README.md) · <img src="https://flagcdn.com/w20/nl.png" alt="Nederlands" style="height:14px;"> [Nederlands](../nl/README.md) · <img src="https://flagcdn.com/w20/pl.png" alt="Polski" style="height:14px;"> [Polski](../pl/README.md) · <img src="https://flagcdn.com/w20/ru.png" alt="Русский" style="height:14px;"> [Русский](../ru/README.md) · <img src="https://flagcdn.com/w20/cn.png" alt="中文" style="height:14px;"> [中文](../zh-CN/README.md) · <img src="https://flagcdn.com/w20/vn.png" alt="Tiếng Việt" style="height:14px;"> [Tiếng Việt](../vi/README.md) · <img src="https://flagcdn.com/w20/th.png" alt="ไทย" style="height:14px;"> [ไทย](../th/README.md) · <img src="https://flagcdn.com/w20/id.png" alt="Bahasa Indonesia" style="height:14px;"> [Bahasa Indonesia](README.md) · <img src="https://flagcdn.com/w20/jp.png" alt="日本語" style="height:14px;"> [日本語](../ja/README.md) · <img src="https://flagcdn.com/w20/kr.png" alt="한국어" style="height:14px;"> [한국어](../ko/README.md) · <img src="https://flagcdn.com/w20/in.png" alt="हिन्दी" style="height:14px;"> [हिन्दी](../hi/README.md) · <img src="https://flagcdn.com/w20/ae.png" alt="العربية" style="height:14px;"> [العربية](../ar/README.md)

---
**Omega-Suite** adalah antarmuka terpadu untuk rangkaian alat pemindai **omega-**:  
[omega-scan](https://github.com/kraynux/omega-scan), [omega-check](https://github.com/kraynux/omega-check), [omega-deep](https://github.com/kraynux/omega-deep), [omega-fold](https://github.com/kraynux/omega-fold), [omega-stress](https://github.com/kraynux/omega-stress), [omega-track](https://github.com/kraynux/omega-track), dan [omega-fuzz](https://github.com/kraynux/omega-fuzz)  
disatukan dalam satu aplikasi TUI (kisi di layar utama atau bilah tab tetap, sesuai pilihan pengguna) dengan pustaka bersama [(`omega-lib`)](https://github.com/kraynux/omega-lib).


Setiap alat tetap dapat dijalankan secara mandiri (`omega-check scan ...`
tetap berfungsi) - omega-suite adalah fasad tambahan, bukan
pengganti.

Lihat `~/DEV/SUITE/OMEGA-SUITE_SPECIFICATIONS.md` dan
`~/DEV/SUITE/DECISIONS_ARCHITECTURE.md` (D-014/D-015) untuk rincian
keputusan arsitektur dan ergonomi.

## Pengenalan

Omega-Suite berperan sebagai **pos kendali** pemindai Omega untuk keamanan jaringan

### Tujuan

- Menyatukan 7 alat **pemindai omega** dalam antarmuka yang konsisten, tanpa pernah mengubah atau menggantikannya.
- Satu tema, satu profil tampilan, satu gaya navigasi untuk ke-7 alat - dikonfigurasi sekali, bukan 7 kali.
- Berpindah dari satu alat ke alat lain tanpa kehilangan konteks: setiap tumpukan layar tetap utuh di latar belakang.
- Tetap ringan meskipun 7 alat disatukan: tidak ada yang dimuat ke memori sebelum pembukaan nyata pertamanya.

## Fitur

- **Satu aplikasi TUI** (Textual) untuk Omega-SCAN, -CHECK, -DEEP, -FOLD, -STRESS, -TRACK, dan -FUZZ.
- **Dua gaya navigasi** pilihan (Pengaturan, mulai ulang langsung ditawarkan): kisi tombol dari layar utama, atau bilah tab tetap yang terlihat bahkan di kedalaman (Riwayat, Pengaturan suatu alat...), tanpa pernah kembali ke layar utama.
- **Pemuatan malas**: setiap alat (kode Python dan dependensi) hanya diimpor saat pertama kali dibuka dalam sesi - waktu mulai dan memori tetap sebanding dengan alat yang benar-benar dipakai.
- **Tema dan profil tampilan bersama**: tema berganti secara langsung untuk ke-7 alat sekaligus; profil tampilan dan gaya navigasi, yang lebih struktural, menawarkan untuk segera memulai ulang omega-suite.
- **Bantuan kontekstual**: pintasan global dan ikhtisar cakupan ke-7 alat dari layar utama, bantuan khusus alat yang aktif dari sebuah tab.
- **Pembersihan ekspor global** untuk ke-7 alat dalam satu klik (Pengaturan suite), bahkan untuk alat yang tidak pernah dibuka dalam sesi.
- **Isolasi ketat antar-7 alat** meskipun berbagi satu aplikasi: tidak ada kebocoran gaya maupun status dari satu alat ke alat lain.
- **Setiap alat tetap dapat dipakai sepenuhnya secara mandiri** (TUI dan CLI sendiri, `omega-check scan ...` tetap berfungsi) - omega-suite hanyalah fasad tambahan, tidak pernah pengganti.

## Instalasi

Arsip resmi disediakan dalam format `.tar.gz`. Periksa integritasnya sebelum instalasi:

```bash
sha256sum omega-suite.tar.gz
```

```bash
./install.sh
./omega-suite.sh
```


## Penggunaan
### Menjalankan

```bash
cd ~/omega-suite
./omega-suite.sh
```

###  atau cukup, jika alias telah dibuat, ketik di terminal:
```bash
suite
```
## Kompatibilitas terminal

Antarmuka interaktif (Textual) otomatis mendeteksi kemampuan terminal (emulator, ukuran) dan menyesuaikan lembar gaya strukturalnya (`complete`/`standard`/`reduced`/`mono`), tanpa flag manual. Mode CLI selalu berupa teks biasa, tidak bergantung pada terminal. Kebijakan yang dipakai bersama seluruh suite `omega-` (`omega-lib`, `terminal/policies.py`) — sama dengan milik `omega-check`/`omega-fire`.

### Profil menurut emulator yang terdeteksi

| Emulator | Profil awal |
|---|---|
| Ghostty, Alacritty, WezTerm, Kitty | `complete` |
| Konsole, GNOME Terminal, Terminator, Xfce4 Terminal | `standard` |
| xterm, urxvt, SSH modern | `reduced` |
| TTY Linux, SSH lama | `mono` |
| Emulator tidak dikenal | `reduced` (cadangan bawaan) |

### Profil menurut ukuran terminal

| Ukuran minimum (kolom × baris) | Batas atas profil |
|---|---|
| 120 × 32 | `complete` |
| 100 × 28 | `standard` |
| 80 × 24 | `reduced` |
| di bawahnya | `mono` |

Profil akhir yang dipilih adalah **yang paling ketat dari keduanya** (emulator dan ukuran) — Ghostty layar penuh yang diperkecil menjadi 70 kolom turun ke `mono`, meskipun emulatornya mengizinkan `complete`. Dapat disegarkan langsung dengan tombol `r`, atau ditimpa secara manual dari Pengaturan suite (tombol `s`).

## Arsitektur

### Prinsip desain

- **Fasad komposisi, tidak pernah lapisan bisnis ke-8**: omega-suite tidak memiliki `domain/` sendiri - ia merakit 7 kontainer yang sudah divalidasi secara mandiri oleh setiap proyek, tanpa mengimplementasikan ulang logikanya.
- **Tidak ada file dari ke-7 alat yang diubah.** Kelas layar/widget bersama mereka ditambal di memori, satu kali saja, saat alat itu pertama kali benar-benar dibuka dalam sesi: isolasi CSS (suatu alat tidak pernah mewarisi gaya alat lain), pengalihan « Keluar » internal alat ke tab layar utama suite, dan penyisipan bilah tab jika gaya navigasi itu aktif.
- **`textual` dilarang di luar `interfaces/tui/`** (diperiksa oleh `import-linter` pada setiap perubahan): `app/` tetap independen dari tampilan dan secara teori dapat melayani antarmuka lain.
- **Konstruksi malas dua tingkat**: adaptor suatu alat (impor kodenya), lalu kontainernya (basis SQLite, sensor jaringan) - tidak satu pun dibayar sebelum kunjungan nyata pertama ke alat tersebut.

### Struktur data

```text
src/omega_suite/
├── app/              Perakitan: DependencyContainer malas, bootstrap, adaptor ke-7 alat
│                     (tool_adapters.py), pengaturan bersama (tema, profil tampilan, gaya navigasi)
├── infrastructure/   Path runtime (var/), penyimpanan pengaturan (JSON)
├── interfaces/
│   ├── tui/          Satu-satunya tempat yang mengimpor Textual: App, layar milik suite (Beranda, Pengaturan,
│   │                 Bantuan, Splash), tambalan di memori untuk layar ke-7 alat (screen_patching.py)
│   └── cli/          Dicadangkan, masih kosong - setiap alat mempertahankan mode CLI-nya sendiri, dipanggil langsung
└── ports/            Kontrak yang diharapkan app/ (SettingsStore)
```

## Prasyarat

### Sistem

- Python 3.10+
- Linux (Textual berjalan di sistem lain, yang tidak diuji maupun didukung oleh proyek ini)
- Terminal apa pun - kemampuan nyatanya dideteksi otomatis dan tampilan menyesuaikan diri (lihat « Kompatibilitas terminal » di atas), hingga TTY sederhana

### Dependensi Python

Dideklarasikan dalam `pyproject.toml`, satu lingkungan virtual menyatukan semuanya (lihat `install.sh`):

- `omega-lib`: pustaka bersama (tema, deteksi terminal, tingkat kepercayaan)
- `omega-scan`, `omega-check`, `omega-deep`, `omega-fold`, `omega-stress`, `omega-track`, `omega-fuzz`: 7 alat terintegrasi, masing-masing dengan dependensi transitifnya sendiri
- `textual`: antarmuka TUI
- Dependensi pengembangan (`pip install -e ".[dev]"`): `pytest`, `pytest-asyncio`, `pytest-cov`, `ruff`, `mypy`, `import-linter`

### Ekspor

Setiap alat menulis ekspornya sendiri di `var/<alat>/exports/` dan tangkapan layarnya di `var/<alat>/screenshots/` - `var/` relatif terhadap folder tempat omega-suite dijalankan, atau `$OMEGA_SUITE_VAR_DIR` untuk menimpanya. Ini tidak pernah `var/` bawaan alat saat dijalankan sendiri: dua cara pemakaian (mandiri atau terintegrasi dalam suite) tidak pernah bercampur. Setiap alat dapat menentukan ulang folder tujuannya sendiri dari Pengaturannya sendiri. Tombol « Kosongkan semua ekspor » (Pengaturan suite) mengosongkan folder ini untuk ke-7 alat sekaligus, bahkan yang tidak pernah dibuka dalam sesi - lihat Bantuan suite (tombol `a` dari layar utama) untuk rinciannya.

---

## Keamanan

- omega-suite sendiri tidak membuat permintaan jaringan apa pun dan tidak memindai apa pun: ia mengatur tampilan ke-7 alat, yang masing-masing tetap mempertahankan seluruh pengamannya sendiri (lihat cakupan masing-masing di Bantuan suite, atau di README-nya sendiri).
- Tidak ada rahasia maupun kredensial yang ditangani oleh omega-suite sendiri. Apa yang disimpan setiap alat (target yang disematkan, riwayat, pengaturan sendiri) tetap berada di subfoldernya sendiri `var/<alat>/`, tidak diubah oleh suite.
- Satu-satunya status milik omega-suite (tema, profil tampilan, gaya navigasi) berada di `var/settings.json`, tanpa data sensitif.
- `import-linter` melarang setiap impor `textual` di luar `interfaces/tui/` pada setiap perubahan (lihat Arsitektur) - jaminan struktural, bukan sekadar konvensi.

## Pengujian dan kualitas

```bash
source .venv/bin/activate
pip install -e ".[dev]"
lint-imports        # memeriksa Dependency Rule (textual dilarang di luar interfaces/tui)
pytest -q
ruff check src tests
mypy -p omega_suite
```

## Pencopotan

omega-suite tidak menyentuh apa pun di luar foldernya sendiri dan alias peluncurnya:

1. Hapus baris `alias suite="..."` yang ditambahkan `install.sh` di `~/.bashrc` dan `~/.zshrc`.
2. Hapus folder `omega-suite/` (termasuk lingkungan virtual `.venv/`, data `var/`, dan pengaturan).

Ke-7 alat yang dipasang terpisah (atau yang sedang dikembangkan di foldernya sendiri) tidak terpengaruh: masing-masing tetap dapat dipasang/dicopot secara mandiri, mengikuti README-nya sendiri.

## Lisensi

Omega-Suite didistribusikan di bawah lisensi **MIT**. Lihat file [`LICENSE`](../../../LICENSE) untuk teks lengkapnya.

---

> **Omega-Suite — Mengamati, mengendalikan, mengaudit, untuk mengamankan lebih baik.**
>
> Antarmuka TUI terpadu untuk pemindai Omega-
