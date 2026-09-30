# 🔥 SPAM OTP - SIMULASI EDUKASI - By Azmi

> ⚠️ **SIMULASI EDUKASI** — Hanya menulis ke log lokal. TIDAK terhubung ke WhatsApp / Telegram / internet.

Script Python interaktif untuk belajar **loop, file I/O, warna terminal, login system, dan random generator** dengan tema simulasi pengiriman OTP.

---

## 📑 Daftar Isi

1. [Fitur](#-fitur)
2. [Persyaratan](#-persyaratan)
3. [Instalasi Termux](#-instalasi-termux-dari-nol)
4. [Cara Clone dari GitHub](#-cara-clone-dari-github-ke-termux)
5. [Login Default](#-login-default)
6. [Preview Tampilan](#-preview-tampilan)
7. [Contoh Penggunaan](#-contoh-penggunaan)
8. [Struktur File](#-struktur-file)
9. [Troubleshooting](#-troubleshooting)
10. [Disclaimer](#-disclaimer)
11. [Author](#-author)

---

## ✨ Fitur

| Fitur | Keterangan |
|-------|------------|
| 🔐 Login System | Username `zimzz123` + Password `12345` |
| 👑 Status Pencipta | Tampil `BELUM DIKETAHUI` sebelum login, `OWNER / CREATOR` sesudah |
| ▶  YouTube | Nama channel: `Gkx!!!` |
| 🔥 Efek Garis Api | 8 baris ASCII gradasi kuning → merah |
| 💥 Logo "SPAM OTP" | ASCII art besar warna kuning |
| ✨ Teks Blink | `[ ⚡ ⚡ ⚡ ]` kedip merah |
| 📨 2 Menu Spam | SPAM OTP WA & SPAM OTP TELEGRAM |
| 📞 Input Nomor Target | Muncul saat pilih menu 1 atau 2 |
| 🎲 Kode OTP Random | 6 digit acak per pesan |
| 💾 Log Terpisah | `log_otp_wa.txt` & `log_otp_telegram.txt` |
| 🎨 Menu Warna | ANSI color interaktif |
| 🛡️ Validasi Input | Nomor, jumlah, delay |
| 🎲 Random Gagal 5% | Simulasi realistis |
| 🚫 Batas Login | 3x salah → keluar |

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

## 🚀 Cara Clone dari GitHub ke Termux

### 🅰️ CARA 1 — Clone via HTTPS (Rekomendasi)

#### 1. Copy URL Repo
Repo: `https://github.com/laptopazmi123-commits/spam-wa-simulasi`

#### 2. Clone di Termux

```bash
cd ~
git clone https://github.com/laptopazmi123-commits/spam-wa-simulasi.git
```

> ⚠️ Kalau repo **PRIVATE**, pakai Personal Access Token (lihat Cara 3).

#### 3. Masuk Folder

```bash
cd spam-wa-simulasi
```

#### 4. Cek Isi Folder

```bash
ls -la
```
Harus muncul `azmi.py`, `README.md`, dll.

#### 5. Jalankan

```bash
python azmi.py
```

✅ **Selesai!**

---

### 🅱️ CARA 2 — Download ZIP (Kalau Gak Mau Ribet Git)

#### 1. Buka Repo di GitHub
`https://github.com/laptopazmi123-commits/spam-wa-simulasi`

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
cd spam-wa-simulasi-main
```

#### 7. Jalankan

```bash
python azmi.py
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
git clone https://TOKEN_KAMU@github.com/laptopazmi123-commits/spam-wa-simulasi.git
```

Contoh nyata:
```bash
git clone https://ghp_abc123xyz@github.com/laptopazmi123-commits/spam-wa-simulasi.git
```

#### 3. Masuk & Jalankan

```bash
cd spam-wa-simulasi
python azmi.py
```

> ⚠️ Jangan share token ke siapa pun. Kalau bocor, langsung **revoke** di halaman settings.

---

### 🔄 CARA 4 — Update File dari GitHub

Kalau sudah pernah clone, terus file di GitHub diupdate:

```bash
cd ~/spam-wa-simulasi
git pull
```

Kalau ada konflik:
```bash
git reset --hard origin/main
git pull
```

---

## 🔐 Login Default

Setelah program jalan, kamu akan diminta login:

| Field | Value |
|-------|-------|
| 👤 Username | `zimzz123` |
| 🔑 Password | `12345` |

> ⚠️ **Batas 3x salah** → program otomatis keluar.

Kalau mau ganti, edit di `azmi.py`:
```python
USERNAME = "zimzz123"
PASSWORD = "12345"
```

---

## 🧪 CONTOH SIMULASI LENGKAP (Step-by-Step)

```bash
# 1. Buka Termux, update
pkg update && pkg upgrade -y

# 2. Install Git + Python
pkg install git python -y

# 3. Pindah ke home
cd ~

# 4. Clone repo
git clone https://github.com/laptopazmi123-commits/spam-wa-simulasi.git

# 5. Masuk folder
cd spam-wa-simulasi

# 6. Lihat isi
ls -la

# 7. Jalankan
python azmi.py
```

---

## 🖼️ Preview Tampilan

### Tampilan Login Awal
```
  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
  █████████████████████████████████████████████████████████████████████
  █████████████████████████████████████████████████████████████████████
  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

  ╔══════════════════════════════════════════════════════╗
  ║              🔐 LOGIN Diperlukan 🔐                  ║
  ║                                                      ║
  ║           👑 Status  : BELUM DIKETAHUI               ║
  ║           ▶  YouTube : Gkx!!!                        ║
  ╚══════════════════════════════════════════════════════╝

  Username : zimzz123
  Password : 12345

  [✓] Login berhasil! Selamat datang, zimzz123.
  👑 Status  : OWNER / CREATOR
  ▶  YouTube : Gkx!!!
```

### Tampilan Menu Utama (Setelah Login)
```
  ╔══════════════════════════════════════════════════════╗
  ║           🔥 Created by : AZMI 🔥                    ║
  ║           👑 Status    : OWNER / CREATOR             ║
  ║           ▶  YouTube   : Gkx!!!                      ║
  ║           ⚠  Tidak kirim ke WA/Telegram asli         ║
  ╚══════════════════════════════════════════════════════╝
  ────────────────────────────────────────────────────────
  👤 Login sebagai : zimzz123
  👑 Status        : OWNER / CREATOR
  ▶  YouTube       : Gkx!!!
  📞 Nomor default : 0867686555

  [1] SPAM OTP WA
  [2] SPAM OTP TELEGRAM
  [3] Lihat Log
  [4] Hapus Log
  [5] Info / Disclaimer
  [6] Keluar

  Pilih >
```

### Saat SPAM OTP Jalan
```
  ╔══════════════════════════════════════════════╗
  ║        📨 SPAM OTP - WHATSAPP                ║
  ╚══════════════════════════════════════════════╝

  Nomor target [0867686555] > 0867686555
  Jumlah OTP  > 5
  Delay(s)    > 0.5

  Platform    : WHATSAPP
  Target      : 0867686555
  Jumlah      : 5
  Delay       : 0.5s
  MODE        : LOKAL (tidak kirim ke WhatsApp)
  👑 Status    : OWNER / CREATOR
  ▶  YouTube   : Gkx!!!

[1/5] [2024-09-24 15:00:01] [TERCATAT] [WhatsApp] -> 0867686555 : KODE OTP = 482913
[2/5] [2024-09-24 15:00:02] [TERCATAT] [WhatsApp] -> 0867686555 : KODE OTP = 157204
[3/5] [2024-09-24 15:00:02] [TERCATAT] [WhatsApp] -> 0867686555 : KODE OTP = 893416
...
```

### Ringkasan
```
==========================================================
           [ RINGKASAN SPAM OTP WHATSAPP ]
==========================================================
  Platform  : WHATSAPP
  Target    : 0867686555
  Sukses    : 5
  Gagal     : 0
  Log file  : log_otp_wa.txt
  Operator  : zimzz123 (OWNER / CREATOR)
  YouTube   : Gkx!!!
==========================================================
[i] OTP di atas adalah random/palsu.
    Tidak ada yang benar-benar terkirim.
```

---

## 🎮 Contoh Penggunaan

### Skenario 1 — Login + SPAM OTP WA 5x
```
Username : zimzz123
Password : 12345
Pilih > 1
Nomor target [0867686555] > (Enter)
Jumlah OTP  > 5
Delay(s)    > 0.5
```

### Skenario 2 — SPAM OTP Telegram 10x
```
Pilih > 2
Nomor target [0867686555] > 0867686555
Jumlah OTP  > 10
Delay(s)    > 1
```

### Skenario 3 — Lihat Log WA
```
Pilih > 3
Pilih > 1
```

### Skenario 4 — Hapus Semua Log
```
Pilih > 4
Pilih > 3
```

### Skenario 5 — Keluar
```
Pilih > 6
```
Atau tekan **CTRL + C**.

---

## 📂 Struktur File

```
spam-wa-simulasi/
├── azmi.py                  # Script utama (Author: Azmi)
├── README.md                # Dokumentasi ini
├── .gitignore               # Biar log gak keupload
├── log_otp_wa.txt           # Auto-generated saat spam WA
└── log_otp_telegram.txt     # Auto-generated saat spam Telegram
```

### Isi `.gitignore` (opsional):
```
log_otp_wa.txt
log_otp_telegram.txt
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
| `Permission denied` | `chmod +x azmi.py` |
| `No such file or directory` | Cek nama folder: `ls ~` |
| `Authentication failed` | Token expired / salah → bikin token baru |
| `unzip: command not found` | `pkg install unzip -y` |
| Tidak bisa akses folder HP | `termux-setup-storage` |
| `IndentationError` | File corrupt → clone ulang |
| Repo tidak ketemu (404) | Cek URL, pastikan repo public / token valid |
| Warna tidak muncul | Normal — sebagian terminal tidak support ANSI |
| Login salah terus | Pastikan `zimzz123` / `12345` (huruf kecil) |
| 3x salah login | Program keluar otomatis — restart & coba lagi |

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
alias spam='cd ~/spam-wa-simulasi && python azmi.py'
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
rm -rf ~/spam-wa-simulasi
```

Hapus Python & Git (kalau mau):
```bash
pkg uninstall python git -y
```

---

## ⚠️ Disclaimer

**Script ini dibuat 100% untuk tujuan EDUKASI.**

### ✅ Boleh dipakai untuk:
- Belajar Python & logika loop
- Belajar file I/O
- Belajar ANSI color di terminal
- Belajar sistem login sederhana
- Portofolio coding

### ❌ DILARANG dipakai untuk:
- Spam OTP ke orang lain
- Menipu / mengelabui orang
- Aktivitas ilegal apa pun
- Menjual sebagai jasa spam

### ⚖️ Peringatan Hukum:
- Spam OTP = pelanggaran **UU ITE Pasal 27 & 29**
- Ancaman pidana: **penjara hingga 4 tahun** + denda
- Akun WhatsApp / Telegram bisa di-**ban permanen**
- Pelaku bisa dituntut **perdata & pidana**

### 🔒 Tentang Script Ini:
- **TIDAK** terhubung ke WhatsApp, Telegram, API, atau internet apa pun
- **HANYA** menulis ke file log lokal di HP kamu sendiri
- Kode OTP yang muncul adalah **RANDOM/PALSU** (bukan OTP asli)
- Nomor `0867686555` hanya ditulis sebagai **teks di file log lokal**
- Login `zimzz123` / `12345` hanya untuk **belajar sistem login**

Kalau mau otomasi WhatsApp yang legal, gunakan **WhatsApp Cloud API** resmi dari Meta.
Kalau mau otomasi Telegram yang legal, gunakan **Telegram Bot API** resmi.

---

## 👨‍💻 Author

**Azmi**
- 📅 Tahun: 2024
- 📌 Versi: 5.3.0
- ▶  YouTube: **Gkx!!!**
- 🎯 Tujuan: Edukasi & portofolio
- 🐙 GitHub: [@laptopazmi123-commits](https://github.com/laptopazmi123-commits)

---

## 📜 Lisensi

Script ini bebas dipakai untuk **belajar pribadi**.
Dilarang dijual atau dipakai untuk aktivitas ilegal.

---

**Made with 🔥 by Azmi — 2024**
**▶  YouTube: Gkx!!!**
**Stay legal, stay ethical. 🛡️**
