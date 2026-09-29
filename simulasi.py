#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===========================================
 SPAM OTP - ......
 Author  : Azmi
 Version : 4.1.0
 Year    : 2024
-------------------------------------------
 - HANYA menulis ke file log lokal
 - TIDAK terhubung ke WhatsApp / Telegram
 - Target default: 0867686555
===========================================
"""

import os
import sys
import time
import random
import datetime
import threading
import shutil

# ============ KONFIGURASI ============
NOMOR_DEFAULT    = "0867686555"
LOG_FILE_WA      = "log_otp_wa.txt"
LOG_FILE_TG      = "log_otp_telegram.txt"
PAKAI_API        = True
PAKAI_BLINK      = True
PAKAI_LOGO_BESAR = True
PAKAI_WARNA      = True
# =====================================

# ====== DETEKSI LEBAR LAYAR ======
def get_lebar():
    try:
        return shutil.get_terminal_size().columns
    except Exception:
        return 40

LEBAR = get_lebar()

# ====== WARNA ANSI ======
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

# ====== HARI & BULAN ======
HARI_ID = {
    0: "SENIN", 1: "SELASA", 2: "RABU",
    3: "KAMIS", 4: "JUMAT", 5: "SABTU", 6: "MINGGU"
}
BULAN_ID = {
    1: "JANUARI", 2: "FEBRUARI", 3: "MARET",
    4: "APRIL", 5: "MEI", 6: "JUNI",
    7: "JULI", 8: "AGUSTUS", 9: "SEPTEMBER",
    10: "OKTOBER", 11: "NOVEMBER", 12: "DESEMBER"
}

# ====== API ======
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

# ====== LOGO ======
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

# ====== LIVE CLOCK ======
_clock_lock = threading.Lock()

def ambil_waktu_live():
    now = datetime.datetime.now()
    return (
        HARI_ID[now.weekday()],
        now.day,
        BULAN_ID[now.month],
        now.year,
        now.strftime("%H:%M:%S")
    )

def format_clock():
    hari, tgl, bulan, tahun, jam = ambil_waktu_live()
    return (
        f"{C.BG_BLUE}{C.WHITE} 📅 {hari}, {tgl:02d} {bulan} {tahun} "
        f"{C.RESET} {C.BG_RED}{C.WHITE} ⏰ {jam} WIB {C.RESET}"
    )

def print_live_clock():
    print("  " + format_clock())

def live_clock_loop(stop_event):
    while not stop_event.is_set():
        with _clock_lock:
            teks = "  " + format_clock()
            sys.stdout.write("\033[s\033[2K\r" + teks + "\033[u")
            sys.stdout.flush()
        time.sleep(1)

# ====== UTIL ======
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
    print(C.MAGENTA + "  ║" + C.WHITE + "           ⚠  Tidak kirim ke WA/Telegram asli         " + C.MAGENTA + "║")
    print(C.MAGENTA + "  ╚══════════════════════════════════════════════════════╝" + C.RESET)
    print_live_clock()
    print(C.ORANGE + "  " + "─"*min(LEBAR-4, 56) + C.RESET)

# ====== GENERATOR OTP ======
def generate_otp():
    """Generate kode OTP 6 digit (random/palsu)"""
    return str(random.randint(100000, 999999))

# ====== LOG ======
def tulis_log(file_log, platform, nomor, otp, status="TERCATAT"):
    waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    baris = f"[{waktu}] [{status}] [{platform}] -> {nomor} : KODE OTP = {otp}"
    with open(file_log, "a", encoding="utf-8") as f:
        f.write(baris + "\n")
    return baris

def validasi_nomor(nomor):
    n = nomor.replace("+","").replace("-","").replace(" ","")
    return n.isdigit() and 10 <= len(n) <= 15

# ====== SPAM OTP (WA / TELEGRAM) ======
def spam_otp(platform, file_log, warna_platform):
    print()
    print(warna_platform + "  ╔══════════════════════════════════════════════╗")
    print(warna_platform + f"  ║        📨 SPAM OTP - {platform.upper():<20}    ║")
    print(warna_platform + "  ╚══════════════════════════════════════════════╝" + C.RESET)
    print()

    # ==== INPUT NOMOR TARGET ====
    nomor = input(f"  {C.CYAN}Nomor target [{NOMOR_DEFAULT}] > {C.RESET}").strip()
    if not nomor:
        nomor = NOMOR_DEFAULT
    if not validasi_nomor(nomor):
        print(f"\n{C.RED}[!] Nomor tidak valid.{C.RESET}")
        input("  Enter...")
        return

    # ==== INPUT JUMLAH & DELAY ====
    try:
        jumlah = int(input(f"  {C.CYAN}Jumlah OTP  > {C.RESET}"))
        delay  = float(input(f"  {C.CYAN}Delay(s)    > {C.RESET}"))
        if jumlah <= 0 or delay < 0:
            raise ValueError
    except ValueError:
        print(f"\n{C.RED}[!] Angka tidak valid.{C.RESET}")
        input("  Enter...")
        return

    # ==== INFO ====
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
                log = tulis_log(file_log, platform, nomor, otp, "GAGAL")
                print(f"{C.RED}[{i}/{jumlah}] {log}{C.RESET}")
                gagal += 1
            else:
                log = tulis_log(file_log, platform, nomor, otp, "TERCATAT")
                print(f"{C.GREEN}[{i}/{jumlah}] {log}{C.RESET}")
                sukses += 1
            time.sleep(delay)
        except KeyboardInterrupt:
            print(f"\n{C.RED}[!] Dihentikan (Ctrl+C){C.RESET}")
            break
        except Exception as e:
            print(f"{C.RED}[!] Error: {e}{C.RESET}")
            gagal += 1

    # ==== RINGKASAN ====
    print("\n" + C.ORANGE + "="*min(LEBAR-4, 58) + C.RESET)
    print(C.CYAN + f"           [ RINGKASAN SPAM OTP {platform.upper()} ]" + C.RESET)
    print(C.ORANGE + "="*min(LEBAR-4, 58) + C.RESET)
    print(f"  Platform  : {C.WHITE}{platform.upper()}{C.RESET}")
    print(f"  Target    : {C.WHITE}{nomor}{C.RESET}")
    print(f"  Sukses    : {C.GREEN}{sukses}{C.RESET}")
    print(f"  Gagal     : {C.RED}{gagal}{C.RESET}")
    print(f"  Log file  : {C.YELLOW}{file_log}{C.RESET}")
    print(C.ORANGE + "="*min(LEBAR-4, 58) + C.RESET)
    print(f"{C.YELLOW}[i] OTP di atas adalah random/palsu.")
    print(f"    Tidak ada yang benar-benar terkirim.{C.RESET}\n")

# ====== LIHAT & HAPUS LOG ======
def lihat_log():
    print()
    print(f"  {C.CYAN}[1]{C.RESET} Log WA")
    print(f"  {C.CYAN}[2]{C.RESET} Log Telegram")
    print(f"  {C.CYAN}[0]{C.RESET} Kembali")
    pilih = input(f"\n  {C.CYAN}Pilih > {C.RESET}").strip()

    if pilih == "1":
        file_log = LOG_FILE_WA
    elif pilih == "2":
        file_log = LOG_FILE_TG
    else:
        return

    if not os.path.exists(file_log):
        print(f"\n{C.RED}[!] Belum ada log di {file_log}.{C.RESET}")
        return
    print(f"\n{C.CYAN}=== {file_log} ==={C.RESET}")
    with open(file_log, "r", encoding="utf-8") as f:
        print(f.read())

def hapus_log():
    print()
    print(f"  {C.CYAN}[1]{C.RESET} Hapus Log WA")
    print(f"  {C.CYAN}[2]{C.RESET} Hapus Log Telegram")
    print(f"  {C.CYAN}[3]{C.RESET} Hapus Semua Log")
    print(f"  {C.CYAN}[0]{C.RESET} Kembali")
    pilih = input(f"\n  {C.CYAN}Pilih > {C.RESET}").strip()

    target = []
    if pilih == "1":
        target = [LOG_FILE_WA]
    elif pilih == "2":
        target = [LOG_FILE_TG]
    elif pilih == "3":
        target = [LOG_FILE_WA, LOG_FILE_TG]
    else:
        return

    for f in target:
        if os.path.exists(f):
            os.remove(f)
            print(f"{C.GREEN}[✓] {f} dihapus.{C.RESET}")
        else:
            print(f"{C.RED}[!] {f} tidak ada.{C.RESET}")

# ====== MENU ======
def menu():
    while True:
        print_banner()
        print(f"  Nomor default : {C.YELLOW}{NOMOR_DEFAULT}{C.RESET}\n")
        print(f"  {C.GREEN}[1]{C.RESET} {C.WHITE}SPAM OTP WA{C.RESET}")
        print(f"  {C.GREEN}[2]{C.RESET} {C.WHITE}SPAM OTP TELEGRAM{C.RESET}")
        print(f"  {C.GREEN}[3]{C.RESET} Lihat Log")
        print(f"  {C.GREEN}[4]{C.RESET} Hapus Log")
        print(f"  {C.GREEN}[5]{C.RESET} Info / Disclaimer")
        print(f"  {C.GREEN}[6]{C.RESET} Keluar")
        pilih = input(f"\n  {C.CYAN}Pilih > {C.RESET}").strip()

        if pilih == "1":
            print_banner()
            spam_otp("WhatsApp", LOG_FILE_WA, C.GREEN)
            input("\n  Enter untuk kembali...")

        elif pilih == "2":
            print_banner()
            spam_otp("Telegram", LOG_FILE_TG, C.BLUE)
            input("\n  Enter untuk kembali...")

        elif pilih == "3":
            lihat_log()
            input("\n  Enter untuk kembali...")

        elif pilih == "4":
            hapus_log()
            input("\n  Enter untuk kembali...")

        elif pilih == "5":
            print_banner()
            print(C.YELLOW)
            print("  INFO / DISCLAIMER:")
            print("  -------------------------------------------------")
            print("  • Script ini adalah SIMULASI untuk EDUKASI.")
            print("  • Hanya menulis ke file log lokal.")
            print("  • TIDAK terhubung ke WhatsApp / Telegram.")
            print("  • Kode OTP yang muncul adalah RANDOM/PALSU.")
            print("  • Tidak ada pesan yang benar-benar terkirim.")
            print("  • Hanya untuk belajar Python & logika loop.")
            print("  • Spam OTP ke orang lain = pelanggaran UU ITE.")
            print("  • Author: Azmi - 2024")
            print(C.RESET)
            input("  Enter untuk kembali...")

        elif pilih == "6":
            print(f"\n{C.GREEN}[✓] Bye! - Azmi{C.RESET}\n")
            sys.exit(0)
        else:
            print(f"\n{C.RED}[!] Pilihan tidak valid.{C.RESET}")
            time.sleep(1)

# ====== ENTRY POINT ======
if __name__ == "__main__":
    stop_event = threading.Event()
    clock_thread = threading.Thread(target=live_clock_loop, args=(stop_event,), daemon=True)
    clock_thread.start()
    try:
        menu()
    except KeyboardInterrupt:
        pass
    finally:
        stop_event.set()
        print(f"\n\n{C.GREEN}[✓] Dihentikan. - Azmi{C.RESET}\n")
