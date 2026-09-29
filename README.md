# 🔥 SIMULASI SPAM WA - By Azmi (v3.0)

> ⚠️ **SIMULASI EDUKASI** — Hanya menulis ke log lokal. TIDAK terhubung ke WhatsApp / internet.

Script Python interaktif untuk belajar **loop, file I/O, warna terminal, threading, dan live clock** dengan tema "pengiriman pesan berulang".

---

## 📑 Daftar Isi

1. [Fitur](#-fitur)
2. [Persyaratan](#-persyaratan)
3. [Instalasi Termux](#-instalasi-termux-dari-nol)
4. [Cara Run dari GitHub](#-cara-run-dari-github-ke-termux)
5. [Preview Tampilan](#-preview-tampilan)
6. [Contoh Penggunaan](#-contoh-penggunaan)
7. [Struktur File](#-struktur-file)
8. [Troubleshooting](#-troubleshooting)
9. [Disclaimer](#-disclaimer)

---

## ✨ Fitur

| Fitur | Keterangan |
|-------|------------|
| 🔥 Efek Garis Api | 8 baris ASCII gradasi kuning → merah |
| 💥 Logo "SPAM WA" | ASCII art besar warna kuning |
| ✨ Teks Blink | "SIMULASI - EDUKASI ONLY" kedip merah |
| 🎨 Logo "SIMULASI" | ASCII art warna cyan |
| 📦 Box Author | Nama pembuat: **AZMI** |
| 📅 Hari Indonesia | SENIN, SELASA, ..., MINGGU |
| 📆 Tanggal Live | Auto update tiap hari |
| 🗓️ Bulan Indonesia | JANUARI, FEBRUARI, ..., DESEMBER |
| 📅 Tahun Live | Auto update tiap tahun |
| ⏰ Jam Live WIB | HH:MM:SS update tiap detik |
| 🧵 Threading | Jam tetap jalan tanpa ganggu menu |
| 💾 Log Lokal | Simpan ke `log_simulasi.txt` |
| 🎨 Menu Warna | ANSI color interaktif |
| 🛡️ Validasi Input | Nomor, pesan, jumlah, delay |
| 🎲 Random Gagal 5% | Simulasi realistis |

---

## 📋 Persyaratan

- 📱 **Android** (Termux) / 💻 **Linux** / 🍎 **macOS**
- 🐍 **Python 3.7+**
- 🔧 **Git** (untuk clone dari GitHub)
- 📦 **Tidak butuh library eksternal** (murni standard library)

---

## 📥 Instalasi Termux (dari nol)

### Step 1 — Install Termux
Download dari **F-Droid** (JANGAN dari Play Store — sudah deprecated):
👉 https://f-droid.org/packages/com.termux/

### Step 2 — Buka Termux
Akan muncul prompt seperti:
```
~ $
```

### Step 3 — Update & Upgrade
```bash
pkg update && pkg upgrade -y
```
> ⏳ Tunggu 1-3 menit. Kalau ada prompt, ketik `y` lalu Enter.

### Step 4 — Install Git & Python
```bash
pkg install git python -y
```

### Step 5 — Cek Instalasi
```bash
git --version
python --version
```
Harus muncul versi keduanya (contoh: `git version 2.x.x` dan `Python 3.11.x`).

---

## 🚀 Cara Run dari GitHub ke Termux

### 🅰️ CARA 1 — Clone via HTTPS (Rekomendasi)

#### 1. Buka Repo di Browser
Cari repo kamu di GitHub, contoh:
```
https://github.com/laptopazmi123-commits/spam-wa-simulas
```

#### 2. Copy URL Repo
Klik tombol hijau **`<> Code`** → tab **HTTPS** → copy URL.

Contoh URL yang didapat:
```
[https://github.com/azmi/wa-simulasi-azmi.git](https://github.com/azmi/wa-simulasi-azmi.git)](https://github.com/laptopazmi123-commits/spam-wa-simulasi)
```

#### 3. Clone di Termux
```bash
cd ~
spam-wa-simulasi
```

> ⚠️ Kalau repo **PRIVATE**, pakai Personal Access Token (lihat Cara 3).

#### 4. Masuk Folder
```bash
cd spam-wa-simulasi
```

#### 5. Cek Isi Folder
```bash
ls -la
```
Harus muncul `simulasi.py`, `README.md`, dll.

#### 6. Jalankan
```bash
python simulasi.py
```

✅ **Selesai!**

---

### 🅱️ CARA 2 — Download ZIP (Kalau Gak Mau Ribet Git)

#### 1. Buka Repo di GitHub
#### 2. Klik Tombol Hijau `<> Code` → **Download ZIP**
#### 3. Pindahkan ZIP ke Termux
```bash
termux-setup-storage
```
Ketik **Allow/izinkan** saat muncul popup.

#### 4. Masuk ke Folder Download HP
```bash
cd ~/storage/downloads
ls
```

#### 5. Extract ZIP
```bash
pkg install unzip -y
unzip spam-wa-simulasi-main.zip
```

#### 6. Masuk Folder Hasil Extract
```bash
cd spam-wa-simulasi
```

#### 7. Jalankan
```bash
python simulasi.py
```

✅ **Selesai!**

---

### 🅲 CARA 3 — Clone Repo PRIVATE (Pakai Token)

#### 1. Bikin Personal Access Token
1. Buka: https://github.com/settings/tokens
2. Klik **Generate new token** → **classic**
3. Nama: `termux-azmi`
4. Centang scope: **`repo`**
5. Klik **Generate token**
6. **COPY TOKEN** (hanya muncul sekali!)

Contoh token:
```
ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

#### 2. Clone di Termux
```bash
git clone https://TOKEN_KAMU@github.com/azmi/wa-simulasi-azmi.git
```

Contoh nyata:
```bash
git clone https://ghp_abc123xyz@github.com/azmi/wa-simulasi-azmi.git
```

#### 3. Masuk & Jalankan
```bash
cd wa-simulasi-azmi
python simulasi.py
```

> ⚠️ Jangan share token ke siapa pun. Kalau bocor, langsung **revoke** di halaman settings.

---

### 🔄 CARA 4 — Update File dari GitHub

Kalau sudah pernah clone, terus file di GitHub diupdate:

```bash
cd ~/wa-simulasi-azmi
git pull
```

Kalau ada konflik:
```bash
git reset --hard origin/main
git pull
```

---

## 🧪 CONTOH SIMULASI LENGKAP (Step-by-Step)

Misal repo: `https://github.com/azmi/wa-simulasi-azmi`

```bash
# 1. Buka Termux, update
pkg update && pkg upgrade -y

# 2. Install Git + Python
pkg install git python -y

# 3. Pindah ke home
cd ~

# 4. Clone repo
git clone https://github.com/azmi/wa-simulasi-azmi.git

# 5. Masuk folder
cd wa-simulasi-azmi

# 6. Lihat isi
ls -la

# 7. Jalankan
python simulasi.py
```

---

## 🖼️ Preview Tampilan

### Tampilan Menu Utama
```
  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
  █████████████████████████████████████████████████████████████████████
  █████████████████████████████████████████████████████████████████████
  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

  ███████╗██████╗  █████╗ ███╗   ███╗    ██╗    ██╗ █████╗
  ██╔════╝██╔══██╗██╔══██╗████╗ ████║    ██║    ██║██╔══██╗
  ███████╗██████╔╝███████║██╔████╔██║    ██║ █╗ ██║███████║
  ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║    ██║███╗██║██╔══██║
  ███████║██║     ██║  ██║██║ ╚═╝ ██║    ╚███╔███╔╝██║  ██║
  ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝     ╚══╝╚══╝ ╚═╝  ╚═╝

         ═══════ [ SIMULASI - EDUKASI ONLY ] ═══════

   ███████╗██╗███╗   ███╗██╗   ██╗██╗      █████╗ ███████╗██╗
   ██╔════╝██║████╗ ████║██║   ██║██║     ██╔══██╗██╔════╝██║
   ███████╗██║██╔████╔██║██║   ██║██║     ███████║███████╗██║
   ╚════██║██║██║╚██╔╝██║██║   ██║██║     ██╔══██║╚════██║██║
   ███████║██║██║ ╚═╝ ██║╚██████╔╝███████╗██║  ██║███████║██║
   ╚══════╝╚═╝╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝

  ╔══════════════════════════════════════════════════════╗
  ║           🔥 Created by : AZMI 🔥                    ║
  ║           ⚠  Tidak kirim ke WhatsApp asli            ║
  ╚══════════════════════════════════════════════════════╝
   📅 SELASA, 24 SEPTEMBER 2024  ⏰ 14:35:07 WIB
  ────────────────────────────────────────────────────────
  Nomor default : 085758524193

  [1] Mulai Simulasi
  [2] Lihat Log
  [3] Hapus Log
  [4] Info / Disclaimer
  [5] Keluar

  Pilih >
```

### Live Clock (update tiap detik)
```
 📅 SELASA, 24 SEPTEMBER 2024  ⏰ 14:35:07 WIB
 📅 SELASA, 24 SEPTEMBER 2024  ⏰ 14:35:08 WIB
 📅 SELASA, 24 SEPTEMBER 2024  ⏰ 14:35:09 WIB
```

### Saat Simulasi Jalan
```
[i] Target  : 085758524193
[i] Pesan   : Halo ini simulasi
[i] Jumlah  : 5
[i] Delay   : 0.5s
[i] MODE    : SIMULASI LOKAL (tidak kirim ke WA)

[1/5] [2024-09-24 14:35:10] [TERCATAT] -> 085758524193 : Halo ini simulasi
[2/5] [2024-09-24 14:35:11] [TERCATAT] -> 085758524193 : Halo ini simulasi
...

==========================================================
                [ RINGKASAN SIMULASI ]
==========================================================
  Target    : 085758524193
  Sukses    : 5
  Gagal     : 0
  Log file  : log_simulasi.txt
==========================================================
```

---

## 🎮 Contoh Penggunaan

### Skenario 1 — Simulasi 5 Pesan ke Nomor Default
```
Pilih > 1
Nomor target [085758524193] > (Enter aja untuk pakai default)
Pesan > Halo ini simulasi
Jumlah  > 5
Delay(s)> 0.5
```

### Skenario 2 — Simulasi 20 Pesan Delay Cepat
```
Pilih > 1
Nomor target [085758524193] > 085758524193
Pesan > Testing 123
Jumlah  > 20
Delay(s)> 0.2
```

### Skenario 3 — Lihat Log
```
Pilih > 2
```

### Skenario 4 — Hapus Log
```
Pilih > 3
Yakin hapus? (y/n) > y
```

### Skenario 5 — Keluar
```
Pilih > 5
```
Atau tekan **CTRL + C**.

---

## 📂 Struktur File

```
wa-simulasi-azmi/
├── simulasi.py          # Script utama (Author: Azmi)
├── README.md            # Dokumentasi ini
├── .gitignore           # Biar log gak keupload
└── log_simulasi.txt     # Auto-generated saat simulasi jalan
```

### Isi `.gitignore` (opsional):
```
log_simulasi.txt
__pycache__/
*.pyc
```

---

## 🛠️ Troubleshooting

| ❌ Masalah | ✅ Solusi |
|-----------|----------|
| `git: command not found` | `pkg install git -y` |
| `python: command not found` | `pkg install python -y` |
| `fatal: could not read Username` | Repo private → pakai token (Cara 3) |
| `Permission denied` | `chmod +x simulasi.py` |
| `No such file or directory` | Cek nama folder: `ls ~` |
| `Authentication failed` | Token expired / salah → bikin token baru |
| `unzip: command not found` | `pkg install unzip -y` |
| Tidak bisa akses folder HP | `termux-setup-storage` |
| `IndentationError` | File corrupt → clone ulang |
| Repo tidak ketemu (404) | Cek URL, pastikan repo public / token valid |
| Warna tidak muncul | Normal — sebagian terminal tidak support ANSI |
| Jam tidak update | Pastikan pakai Termux terbaru dari F-Droid |

---

## 🎯 Cara Keluar dari Nano

Kalau nyangkut di editor `nano`:

1. Tekan **CTRL + O** → **Enter** (untuk save)
2. Tekan **CTRL + X** (untuk keluar)

Kalau tidak mau save:
1. Tekan **CTRL + X**
2. Ketik **N** → Enter

---

## 🎁 BONUS — Jalankan Sekali Klik di Termux

Buat **alias** biar gampang:

### 1. Buka file bashrc
```bash
nano ~/.bashrc
```

### 2. Tambahkan di baris paling bawah
```bash
alias spam='cd ~/wa-simulasi-azmi && python simulasi.py'
```

Simpan: **CTRL+O** → Enter → **CTRL+X**

### 3. Reload
```bash
source ~/.bashrc
```

### 4. Sekarang tinggal ketik:
```bash
spam
```
Langsung jalan! 🔥

---

## 🧹 Uninstall / Bersihkan

Hapus folder project:
```bash
rm -rf ~/wa-simulasi-azmi
```

Hapus Python & Git (kalau mau):
```bash
pkg uninstall python git -y
```

---

## ⚠️ Disclaimer

**Script ini dibuat 100% untuk tujuan EDUKASI.**

- ✅ Boleh dipakai untuk: belajar Python, logika loop, threading, ANSI color
- ❌ DILARANG dipakai untuk: spam WA ke orang lain

**Peringatan hukum:**
- Spam WA = pelanggaran **UU ITE Pasal 27 & 29**
- Ancaman pidana: **penjara hingga 4 tahun** + denda
- Akun WhatsApp bisa di-**ban permanen** oleh Meta

Script ini **TIDAK** terhubung ke WhatsApp, API, atau internet apa pun. Nomor `085758524193` hanya ditulis sebagai **teks di file log lokal** di HP kamu sendiri.

Kalau mau otomasi WhatsApp yang legal, gunakan **WhatsApp Cloud API** resmi dari Meta.

---

## 👨‍💻 Author

**Azmi**
- 📅 Tahun: 2024
- 📌 Versi: 3.0.0
- 🎯 Tujuan: Edukasi & portofolio
- 🐙 GitHub: [@azmi](https://github.com/laptopazmi123-commits/spam-wa-simulasi)

---

## 📜 Lisensi

Script ini bebas dipakai untuk **belajar pribadi**.
Dilarang dijual atau dipakai untuk aktivitas ilegal.

---

**Made with 🔥 by Azmi — 2024**
**Stay legal, stay ethical. 🛡️**
