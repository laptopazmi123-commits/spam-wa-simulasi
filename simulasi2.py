#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===========================================
 SIMULASI - By Azmi
 YouTube : Gkx!!!
 Version : 7.2.0
 Year    : 2024
-------------------------------------------
 - HANYA menulis ke file log lokal
 - terhubung ke WhatsApp / Telegram
 - Login: zimzz123 / 12345
===========================================
"""

import os
import sys
import time
import random
import datetime
import shutil

# ============ KONFIGURASI ============
USERNAME             = "zimzz123"
PASSWORD             = "12345"
STATUS_PENCIPTA      = "OWNER / CREATOR"
NAMA_YOUTUBE         = "Gkx!!!"
NOMOR_DEFAULT        = "0867686555"
LOG_FILE_WA          = "log_otp_wa.txt"
LOG_FILE_TG          = "log_otp_telegram.txt"
LOG_FILE_CANNON      = "log_cannon_wa.txt"
LOG_FILE_CANNON_GRUB = "log_cannon_grub.txt"
LOG_FILE_BAN         = "log_ban_grub.txt"
PAKAI_API            = True
PAKAI_BLINK          = True
PAKAI_LOGO_BESAR     = True
PAKAI_WARNA          = True
# =====================================

def get_lebar():
    try:
        return shutil.get_terminal_size().columns
    except Exception:
        return 40

LEBAR = get_lebar()

class C:
    if PAKAI_WARNA:
        RED     = "\033[1;31m"
        ORANGE  = "\033[1;33m"
        YELLOW  = "\033[1;93m"
        GREEN   = "\033[1;32m"
        CYAN    = "\033[1;36m"
        BLUE    = "\033[1;34m"
        MAGENTA = "\033[1;35m"
        WHITE   = "\033[1;37m"
        DIM     = "\033[2m"
        RESET   = "\033[0m"
        BLINK   = "\033[5m" if PAKAI_BLINK else ""
        BG_RED  = "\033[1;41m"
        BG_BLUE = "\033[1;44m"
    else:
        RED = ORANGE = YELLOW = GREEN = CYAN = BLUE = ""
        MAGENTA = WHITE = DIM = RESET = BLINK = ""
        BG_RED = BG_BLUE = ""

def buat_fire():
    if not PAKAI_API:
        return []
    w = min(LEBAR - 4, 70)
    if w < 20:
        w = 20
    pola = ["░", "▒", "▓", "█", "█", "▓", "▒", "░"]
    return [p * w for p in pola]

FIRE_LINES = buat_fire()
FIRE_COLORS = [C.YELLOW, C.ORANGE, C.RED, C.RED, C.RED, C.ORANGE, C.YELLOW, C.YELLOW]

LOGO_BESAR = r"""
  ███████╗██████╗  █████╗ ███╗   ███╗    ██╗    ██╗ █████╗ 
  ██╔════╝██╔══██╗██╔══██╗████╗ ████║    ██║    ██║██╔══██╗
  ███████╗██████╔╝███████║██╔████╔██║    ██║ █╗ ██║███████║
  ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║    ██║███╗██║██╔══██║
  ███████║██║     ██║  ██║██║ ╚═╝ ██║    ╚███╔███╔╝██║  ██║
  ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝     ╚══╝╚══╝ ╚═╝  ╚═╝

         ██████╗ ████████╗██████╗ 
        ██╔═══██╗╚══██╔══╝██╔══██╗
        ██║   ██║   ██║   ██████╔╝
        ██║   ██║   ██║   ██╔═══╝ 
        ╚██████╔╝   ██║   ██║     
         ╚═════╝    ╚═╝   ╚═╝     
"""

LOGO_KECIL = r"""
   ╔═╗╔═╗╔═╗╔╦╗  ╔═╗╔╦╗╔═╗
   ╚═╗╠═╝╠═╣║║║  ║ ║ ║ ╠═╝
   ╚═╝╩  ╩ ╩╩ ╩  ╚═╝ ╩ ╩  
"""

def pakai_logo_besar():
    return PAKAI_LOGO_BESAR and LEBAR >= 60

def clear():
    os.system("clear" if os.name == "posix" else "cls")

def print_fire():
    for baris, warna in zip(FIRE_LINES, FIRE_COLORS):
        print(warna + "  " + baris + C.RESET)

def print_logo():
    if pakai_logo_besar():
        print(C.YELLOW + LOGO_BESAR + C.RESET)
        print(C.RED + C.BLINK + "              ═══════ [ ⚡ ⚡ ⚡ ] ═══════" + C.RESET)
    else:
        print(C.YELLOW + LOGO_KECIL + C.RESET)
        print(C.RED + C.BLINK + "        [ ⚡ ⚡ ⚡ ]" + C.RESET)

def print_banner():
    clear()
    if PAKAI_API:
        print_fire()
    print_logo()
    print(C.MAGENTA + "  ╔══════════════════════════════════════════════════════╗")
    print(C.MAGENTA + "  ║" + C.WHITE + "           🔥 Created by : " + C.YELLOW + "AZMI" + C.WHITE + " 🔥                  " + C.MAGENTA + "║")
    print(C.MAGENTA + "  ║" + C.WHITE + f"           👑 Status    : " + C.GREEN + f"{STATUS_PENCIPTA:<12}" + C.WHITE + "              " + C.MAGENTA + "║")
    print(C.MAGENTA + "  ║" + C.WHITE + f"           ▶  YouTube   : " + C.RED + f"{NAMA_YOUTUBE:<12}" + C.WHITE + "              " + C.MAGENTA + "║")
    print(C.MAGENTA + "  ║" + C.WHITE + "           ⚠  Tidak kirim ke WA/Telegram asli         " + C.MAGENTA + "║")
    print(C.MAGENTA + "  ╚══════════════════════════════════════════════════════╝" + C.RESET)
    print(C.ORANGE + "  " + "─"*min(LEBAR-4, 56) + C.RESET)

def login():
    max_percobaan = 3
    percobaan = 0
    while percobaan < max_percobaan:
        clear()
        if PAKAI_API:
            print_fire()
        print_logo()
        print(C.MAGENTA + "  ╔══════════════════════════════════════════════════════╗")
        print(C.MAGENTA + "  ║" + C.WHITE + "              🔐 LOGIN Diperlukan 🔐                  " + C.MAGENTA + "║")
        print(C.MAGENTA + "  ║" + C.WHITE + "                                                      " + C.MAGENTA + "║")
        print(C.MAGENTA + "  ║" + C.WHITE + f"           👑 Status  : " + C.RED + f"{'BELUM DIKETAHUI':<20}" + C.WHITE + "      " + C.MAGENTA + "║")
        print(C.MAGENTA + "  ║" + C.WHITE + f"           ▶  YouTube : " + C.RED + f"{NAMA_YOUTUBE:<20}" + C.WHITE + "      " + C.MAGENTA + "║")
        print(C.MAGENTA + "  ╚══════════════════════════════════════════════════════╝" + C.RESET)
        print()
        print(f"  {C.CYAN}Username : {C.RESET}", end="")
        user = input().strip()
        print(f"  {C.CYAN}Password : {C.RESET}", end="")
        pw = input().strip()
        if user == USERNAME and pw == PASSWORD:
            print(f"\n  {C.GREEN}[✓] Login berhasil! Selamat datang, {USERNAME}.{C.RESET}")
            print(f"  {C.YELLOW}👑 Status  : {STATUS_PENCIPTA}{C.RESET}")
            print(f"  {C.RED}▶  YouTube : {NAMA_YOUTUBE}{C.RESET}")
            time.sleep(1.5)
            return True
        else:
            percobaan += 1
            sisa = max_percobaan - percobaan
            print(f"\n  {C.RED}[✗] Username/Password salah! Sisa percobaan: {sisa}{C.RESET}")
            time.sleep(1.5)
    clear()
    print(C.RED)
    print("  ╔══════════════════════════════════════════════════════╗")
    print("  ║           ❌ AKSES DITOLAK - 3x SALAH ❌              ║")
    print("  ║              Program akan keluar...                  ║")
    print("  ╚══════════════════════════════════════════════════════╝")
    print(C.RESET)
    time.sleep(2)
    return False

def generate_otp():
    return str(random.randint(100000, 999999))

def tulis_log(file_log, platform, nomor, isi, status="TERCATAT"):
    waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    baris = f"[{waktu}] [{status}] [{platform}] -> {nomor} : {isi}"
    with open(file_log, "a", encoding="utf-8") as f:
        f.write(baris + "\n")
    return baris

def validasi_nomor(nomor):
    n = nomor.replace("+","").replace("-","").replace(" ","")
    return n.isdigit() and 10 <= len(n) <= 15

def progress_bar(current, total, width=None):
    if width is None:
        width = min(LEBAR - 30, 30)
        if width < 10:
            width = 10
    persen = current / total
    filled = int(width * persen)
    bar = "█" * filled + "░" * (width - filled)
    return f"[{bar}] {int(persen*100):3d}%"

# ====== SPAM OTP ======
def spam_otp(platform, file_log, warna_platform):
    print()
    print(warna_platform + "  ╔══════════════════════════════════════════════╗")
    print(warna_platform + f"  ║        📨 SPAM OTP - {platform.upper():<20}    ║")
    print(warna_platform + "  ╚══════════════════════════════════════════════╝" + C.RESET)
    print()
    nomor = input(f"  {C.CYAN}Nomor target [{NOMOR_DEFAULT}] > {C.RESET}").strip()
    if not nomor:
        nomor = NOMOR_DEFAULT
    if not validasi_nomor(nomor):
        print(f"\n{C.RED}[!] Nomor tidak valid.{C.RESET}")
        input("  Enter...")
        return
    try:
        jumlah = int(input(f"  {C.CYAN}Jumlah OTP  > {C.RESET}"))
        delay  = float(input(f"  {C.CYAN}Delay(s)    > {C.RESET}"))
        if jumlah <= 0 or delay < 0:
            raise ValueError
    except ValueError:
        print(f"\n{C.RED}[!] Angka tidak valid.{C.RESET}")
        input("  Enter...")
        return
    print()
    print(f"  {C.CYAN}Platform    : {C.WHITE}{platform.upper()}{C.RESET}")
    print(f"  {C.CYAN}Target      : {C.WHITE}{nomor}{C.RESET}")
    print(f"  {C.CYAN}Jumlah      : {C.WHITE}{jumlah}{C.RESET}")
    print(f"  {C.CYAN}Delay       : {C.WHITE}{delay}s{C.RESET}")
    print(f"  {C.RED}MODE        : {C.YELLOW}LOKAL (tidak kirim ke {platform}){C.RESET}")
    print()
    time.sleep(1)
    sukses, gagal = 0, 0
    for i in range(1, jumlah + 1):
        try:
            otp = generate_otp()
            if random.random() < 0.05:
                log = tulis_log(file_log, platform, nomor, f"KODE OTP = {otp}", "GAGAL")
                print(f"{C.RED}[{i}/{jumlah}] {log}{C.RESET}")
                gagal += 1
            else:
                log = tulis_log(file_log, platform, nomor, f"KODE OTP = {otp}", "TERCATAT")
                print(f"{C.GREEN}[{i}/{jumlah}] {log}{C.RESET}")
                sukses += 1
            time.sleep(delay)
        except KeyboardInterrupt:
            print(f"\n{C.RED}[!] Dihentikan (Ctrl+C){C.RESET}")
            break
        except Exception as e:
            print(f"{C.RED}[!] Error: {e}{C.RESET}")
            gagal += 1
    print("\n" + C.ORANGE + "="*min(LEBAR-4, 58) + C.RESET)
    print(C.CYAN + f"           [ RINGKASAN SPAM OTP {platform.upper()} ]" + C.RESET)
    print(C.ORANGE + "="*min(LEBAR-4, 58) + C.RESET)
    print(f"  Platform  : {C.WHITE}{platform.upper()}{C.RESET}")
    print(f"  Target    : {C.WHITE}{nomor}{C.RESET}")
    print(f"  Sukses    : {C.GREEN}{sukses}{C.RESET}")
    print(f"  Gagal     : {C.RED}{gagal}{C.RESET}")
    print(f"  Log file  : {C.YELLOW}{file_log}{C.RESET}")
    print(C.ORANGE + "="*min(LEBAR-4, 58) + C.RESET)
    print(f"{C.YELLOW}[i] OTP di atas adalah random.HATI-HATI MENGUNAKAN.{C.RESET}\n")

# ====== CANNON WA ======
def submenu_cannon():
    while True:
        print_banner()
        print(C.RED + "  ╔══════════════════════════════════════════════════════╗")
        print(C.RED + "  ║        💣  C A N N O N   W A  💣                     ║")
        print(C.RED + "  ║           (Simulasi Massal - Local Only)             ║")
        print(C.RED + "  ╚══════════════════════════════════════════════════════╝" + C.RESET)
        print()
        print(f"  {C.CYAN}[1]{C.RESET} {C.WHITE}💣 Mulai Cannon{C.RESET}")
        print(f"  {C.CYAN}[2]{C.RESET} {C.WHITE}📂 Buka Riwayat Cannon{C.RESET}")
        print(f"  {C.CYAN}[3]{C.RESET} {C.WHITE}🗑️  Hapus Riwayat Cannon{C.RESET}")
        print(f"  {C.CYAN}[0]{C.RESET} {C.WHITE}⬅️  Kembali{C.RESET}")
        pilih = input(f"\n  {C.CYAN}Pilih > {C.RESET}").strip()
        if pilih == "1":
            print_banner()
            cannon_wa()
            input("\n  Enter untuk kembali...")
        elif pilih == "2":
            buka_cannon()
            input("\n  Enter untuk kembali...")
        elif pilih == "3":
            hapus_riwayat_cannon()
            input("\n  Enter untuk kembali...")
        elif pilih == "0":
            return
        else:
            print(f"\n{C.RED}[!] Pilihan tidak valid.{C.RESET}")
            time.sleep(1)

def cannon_wa():
    print()
    print(C.RED + "  ╔══════════════════════════════════════════════════════╗")
    print(C.RED + "  ║        💣  CANNON WA - MULAI  💣                     ║")
    print(C.RED + "  ╚══════════════════════════════════════════════════════╝" + C.RESET)
    print()
    nomor = input(f"  {C.CYAN}Nomor target [{NOMOR_DEFAULT}] > {C.RESET}").strip()
    if not nomor:
        nomor = NOMOR_DEFAULT
    if not validasi_nomor(nomor):
        print(f"\n{C.RED}[!] Nomor tidak valid.{C.RESET}")
        input("  Enter...")
        return
    try:
        jumlah = int(input(f"  {C.CYAN}Jumlah OTP  > {C.RESET}"))
        delay  = float(input(f"  {C.CYAN}Delay(s)    > {C.RESET}"))
        if jumlah <= 0 or delay < 0:
            raise ValueError
    except ValueError:
        print(f"\n{C.RED}[!] Angka tidak valid.{C.RESET}")
        input("  Enter...")
        return
    print()
    input(f"  {C.YELLOW}Tekan ENTER untuk memulai CANNON...{C.RESET}")
    print()
    print(C.RED + C.BLINK + "  ╔══════════════════════════════════════════════════════╗")
    print(C.RED + C.BLINK + "  ║              💣  D I M U L A I  💣                   ║")
    print(C.RED + C.BLINK + "  ╚══════════════════════════════════════════════════════╝" + C.RESET)
    print()
    sesi_id = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    tulis_log(LOG_FILE_CANNON, "CANNON-WA", nomor, f"--- SESI {sesi_id} DIMULAI (target={jumlah}) ---", "INFO")
    sukses, gagal = 0, 0
    waktu_mulai = time.time()
    for i in range(1, jumlah + 1):
        try:
            otp = generate_otp()
            if random.random() < 0.05:
                tulis_log(LOG_FILE_CANNON, "CANNON-WA", nomor, f"KODE OTP = {otp}", "GAGAL")
                gagal += 1
                warna_status = C.RED
                status_teks = "GAGAL"
            else:
                tulis_log(LOG_FILE_CANNON, "CANNON-WA", nomor, f"KODE OTP = {otp}", "TERCATAT")
                sukses += 1
                warna_status = C.GREEN
                status_teks = "OK"
            bar = progress_bar(i, jumlah)
            sys.stdout.write(f"\r  {warna_status}[{i:>3}/{jumlah}] {bar} OTP:{C.YELLOW}{otp}{C.RESET} {warna_status}{status_teks}{C.RESET}")
            sys.stdout.flush()
            time.sleep(delay)
        except KeyboardInterrupt:
            print(f"\n\n  {C.RED}[!] CANNON dihentikan{C.RESET}")
            break
        except Exception as e:
            print(f"\n  {C.RED}[!] Error: {e}{C.RESET}")
            gagal += 1
    durasi = time.time() - waktu_mulai
    tulis_log(LOG_FILE_CANNON, "CANNON-WA", nomor, f"--- SESI {sesi_id} SELESAI (sukses={sukses}, gagal={gagal}, durasi={durasi:.2f}s) ---", "INFO")
    print("\n")
    print(C.ORANGE + "  " + "═"*min(LEBAR-4, 58) + C.RESET)
    print(C.RED + "     💣  [ RINGKASAN CANNON WA ]  💣" + C.RESET)
    print(C.ORANGE + "  " + "═"*min(LEBAR-4, 58) + C.RESET)
    print(f"  {C.CYAN}Sesi ID     : {C.WHITE}{sesi_id}{C.RESET}")
    print(f"  {C.CYAN}Target      : {C.WHITE}{nomor}{C.RESET}")
    print(f"  {C.CYAN}Total       : {C.WHITE}{jumlah}{C.RESET}")
    print(f"  {C.CYAN}Sukses      : {C.GREEN}{sukses}{C.RESET}")
    print(f"  {C.CYAN}Gagal       : {C.RED}{gagal}{C.RESET}")
    print(f"  {C.CYAN}Durasi      : {C.WHITE}{durasi:.2f} detik{C.RESET}")
    print(f"  {C.CYAN}Log file    : {C.YELLOW}{LOG_FILE_CANNON}{C.RESET}")
    print(C.ORANGE + "  " + "═"*min(LEBAR-4, 58) + C.RESET)
    print(f"  {C.YELLOW}[i] Ini cuma simulasi. Tidak ada yang terkirim ke WA.{C.RESET}\n")

def buka_cannon():
    print()
    print(C.CYAN + "  ╔══════════════════════════════════════════════════════╗")
    print(C.CYAN + "  ║        📂  BUKA CANNON - RIWAYAT  📂                 ║")
    print(C.CYAN + "  ╚══════════════════════════════════════════════════════╝" + C.RESET)
    print()
    if not os.path.exists(LOG_FILE_CANNON):
        print(f"  {C.YELLOW}[!] Belum ada riwayat CANNON.{C.RESET}\n")
        return
    with open(LOG_FILE_CANNON, "r", encoding="utf-8") as f:
        print(f.read())

def hapus_riwayat_cannon():
    print()
    if not os.path.exists(LOG_FILE_CANNON):
        print(f"  {C.YELLOW}[!] Tidak ada riwayat.{C.RESET}\n")
        return
    k = input(f"  {C.YELLOW}Yakin hapus? (y/n) > {C.RESET}").strip().lower()
    if k == "y":
        os.remove(LOG_FILE_CANNON)
        print(f"\n  {C.GREEN}[✓] Dihapus.{C.RESET}\n")

# ====== CANNON GRUB WA ======
def submenu_cannon_grub():
    while True:
        print_banner()
        print(C.RED + "  ╔══════════════════════════════════════════════════════╗")
        print(C.RED + "  ║      💣  C A N N O N   G R U B   W A  💣             ║")
        print(C.RED + "  ║         (Massal ke Grup - Local Only)       ║")
        print(C.RED + "  ╚══════════════════════════════════════════════════════╝" + C.RESET)
        print()
        print(f"  {C.CYAN}[1]{C.RESET} {C.WHITE}💣 Mulai Cannon Grub{C.RESET}")
        print(f"  {C.CYAN}[2]{C.RESET} {C.WHITE}📂 Buka Riwayat Cannon Grub{C.RESET}")
        print(f"  {C.CYAN}[3]{C.RESET} {C.WHITE}🗑️  Hapus Riwayat Cannon Grub{C.RESET}")
        print(f"  {C.CYAN}[0]{C.RESET} {C.WHITE}⬅️  Kembali{C.RESET}")
        pilih = input(f"\n  {C.CYAN}Pilih > {C.RESET}").strip()
        if pilih == "1":
            print_banner()
            cannon_grub_wa()
            input("\n  Enter untuk kembali...")
        elif pilih == "2":
            buka_cannon_grub()
            input("\n  Enter untuk kembali...")
        elif pilih == "3":
            hapus_riwayat_cannon_grub()
            input("\n  Enter untuk kembali...")
        elif pilih == "0":
            return
        else:
            print(f"\n{C.RED}[!] Pilihan tidak valid.{C.RESET}")
            time.sleep(1)

def cannon_grub_wa():
    print()
    print(C.RED + "  ╔══════════════════════════════════════════════════════╗")
    print(C.RED + "  ║      💣  CANNON GRUB WA - MULAI  💣                  ║")
    print(C.RED + "  ╚══════════════════════════════════════════════════════╝" + C.RESET)
    print()
    nama_grup = input(f"  {C.CYAN}Nama Grup > {C.RESET}").strip()
    if not nama_grup:
        print(f"\n{C.RED}[!] Nama grup tidak boleh kosong.{C.RESET}")
        input("  Enter...")
        return
    link_grup = input(f"  {C.CYAN}Link Grup > {C.RESET}").strip()
    if not link_grup:
        print(f"\n{C.RED}[!] Link grup tidak boleh kosong.{C.RESET}")
        input("  Enter...")
        return
    try:
        jumlah = int(input(f"  {C.CYAN}Jumlah Kirim > {C.RESET}"))
        delay  = float(input(f"  {C.CYAN}Delay (detik) > {C.RESET}"))
        if jumlah <= 0 or delay < 0:
            raise ValueError
    except ValueError:
        print(f"\n{C.RED}[!] Angka tidak valid.{C.RESET}")
        input("  Enter...")
        return
    print()
    print(C.ORANGE + "  " + "═"*min(LEBAR-4, 58) + C.RESET)
    print(C.YELLOW + "  📋 KONFIRMASI CANNON GRUB WA" + C.RESET)
    print(C.ORANGE + "  " + "═"*min(LEBAR-4, 58) + C.RESET)
    print(f"  {C.CYAN}Nama Grup     : {C.WHITE}{nama_grup}{C.RESET}")
    print(f"  {C.CYAN}Link Grup     : {C.WHITE}{link_grup}{C.RESET}")
    print(f"  {C.CYAN}Jumlah Kirim  : {C.WHITE}{jumlah}x{C.RESET}")
    print(f"  {C.CYAN}Delay         : {C.WHITE}{delay} detik{C.RESET}")
    print(C.ORANGE + "  " + "═"*min(LEBAR-4, 58) + C.RESET)
    input(f"  {C.YELLOW}Tekan ENTER untuk memulai...{C.RESET}")
    print()
    print(C.RED + C.BLINK + "  ╔══════════════════════════════════════════════════════╗")
    print(C.RED + C.BLINK + "  ║           💣  D I M U L A I  💣                      ║")
    print(C.RED + C.BLINK + "  ║     CANNON GRUB WA sedang berjalan...                ║")
    print(C.RED + C.BLINK + "  ╚══════════════════════════════════════════════════════╝" + C.RESET)
    print()
    sesi_id = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    tulis_log(LOG_FILE_CANNON_GRUB, "CANNON-GRUB", nama_grup, f"--- SESI {sesi_id} DIMULAI (link={link_grup}, jumlah={jumlah}x, delay={delay}s) ---", "INFO")
    sukses, gagal = 0, 0
    waktu_mulai = time.time()
    for i in range(1, jumlah + 1):
        try:
            if random.random() < 0.07:
                tulis_log(LOG_FILE_CANNON_GRUB, "CANNON-GRUB", nama_grup, f"KIRIM#{i:03d} link={link_grup}", "GAGAL")
                gagal += 1
                warna_status = C.RED
                status_teks = "SKIP"
            else:
                tulis_log(LOG_FILE_CANNON_GRUB, "CANNON-GRUB", nama_grup, f"KIRIM#{i:03d} link={link_grup}", "TERCATAT")
                sukses += 1
                warna_status = C.GREEN
                status_teks = "OK"
            bar = progress_bar(i, jumlah)
            sys.stdout.write(f"\r  {warna_status}[KIRIM {i:>3}/{jumlah}] {bar} {warna_status}{status_teks}{C.RESET}")
            sys.stdout.flush()
            time.sleep(delay)
        except KeyboardInterrupt:
            print(f"\n\n  {C.RED}[!] CANNON GRUB dihentikan{C.RESET}")
            break
        except Exception as e:
            print(f"\n  {C.RED}[!] Error: {e}{C.RESET}")
            gagal += 1
    durasi = time.time() - waktu_mulai
    tulis_log(LOG_FILE_CANNON_GRUB, "CANNON-GRUB", nama_grup, f"--- SESI {sesi_id} SELESAI (sukses={sukses}, gagal={gagal}, durasi={durasi:.2f}s) ---", "INFO")
    print("\n")
    print(C.ORANGE + "  " + "═"*min(LEBAR-4, 58) + C.RESET)
    print(C.RED + "     💣  [ RINGKASAN CANNON GRUB WA ]  💣" + C.RESET)
    print(C.ORANGE + "  " + "═"*min(LEBAR-4, 58) + C.RESET)
    print(f"  {C.CYAN}Sesi ID       : {C.WHITE}{sesi_id}{C.RESET}")
    print(f"  {C.CYAN}Nama Grup     : {C.WHITE}{nama_grup}{C.RESET}")
    print(f"  {C.CYAN}Link Grup     : {C.WHITE}{link_grup}{C.RESET}")
    print(f"  {C.CYAN}Jumlah Kirim  : {C.WHITE}{jumlah}x{C.RESET}")
    print(f"  {C.CYAN}Delay         : {C.WHITE}{delay} detik{C.RESET}")
    print(f"  {C.CYAN}Berhasil      : {C.GREEN}{sukses}{C.RESET}")
    print(f"  {C.CYAN}Gagal/Skip    : {C.RED}{gagal}{C.RESET}")
    print(f"  {C.CYAN}Durasi        : {C.WHITE}{durasi:.2f} detik{C.RESET}")
    print(f"  {C.CYAN}Log file      : {C.YELLOW}{LOG_FILE_CANNON_GRUB}{C.RESET}")
    print(C.ORANGE + "  " + "═"*min(LEBAR-4, 58) + C.RESET)
    print(f"  {C.YELLOW}[i] HAHAHAHAHHA SIAPA SURUH NGEHINA. MAMPUS GRUB LU.{C.RESET
