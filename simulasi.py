#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===========================================
 SIMULASI SPAM WA - EDUKASI ONLY
 Author  : Azmi
 Version : 3.0.0
 Year    : 2024
-------------------------------------------
 - HANYA menulis ke file log lokal
 - TIDAK terhubung ke WhatsApp / internet
 - Target default: 0888888888888
 - Fitur baru: Live tanggal, bulan, tahun, jam
===========================================
"""

import os
import sys
import time
import random
import datetime
import threading

# ====== KONFIGURASI ======
NOMOR_DEFAULT = "0888888888888"
LOG_FILE      = "log_simulasi.txt"

# ====== WARNA ANSI ======
class C:
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
    BLINK   = "\033[5m"
    BG_RED  = "\033[1;41m"
    BG_BLUE = "\033[1;44m"

# ====== HARI & BULAN INDONESIA ======
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

# ====== EFEK GARIS API BESAR ======
FIRE_LINES = [
    "  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ",
    "  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ",
    "  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ",
    "  █████████████████████████████████████████████████████████████████████  ",
    "  █████████████████████████████████████████████████████████████████████  ",
    "  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ",
    "  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ",
    "  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ",
]
FIRE_COLORS = [C.YELLOW, C.ORANGE, C.RED, C.RED, C.RED, C.ORANGE, C.YELLOW, C.YELLOW]

# ====== LOGO ASCII ======
LOGO_SPAM = r"""
  ███████╗██████╗  █████╗ ███╗   ███╗    ██╗    ██╗ █████╗ 
  ██╔════╝██╔══██╗██╔══██╗████╗ ████║    ██║    ██║██╔══██╗
  ███████╗██████╔╝███████║██╔████╔██║    ██║ █╗ ██║███████║
  ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║    ██║███╗██║██╔══██║
  ███████║██║     ██║  ██║██║ ╚═╝ ██║    ╚███╔███╔╝██║  ██║
  ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝     ╚══╝╚══╝ ╚═╝  ╚═╝
"""

LOGO_SIMULASI = r"""
   ███████╗██╗███╗   ███╗██╗   ██╗██╗      █████╗ ███████╗██╗
   ██╔════╝██║████╗ ████║██║   ██║██║     ██╔══██╗██╔════╝██║
   ███████╗██║██╔████╔██║██║   ██║██║     ███████║███████╗██║
   ╚════██║██║██║╚██╔╝██║██║   ██║██║     ██╔══██║╚════██║██║
   ███████║██║██║ ╚═╝ ██║╚██████╔╝███████╗██║  ██║███████║██║
   ╚══════╝╚═╝╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝
"""

# ====== LIVE CLOCK ======
_running_clock = False

def ambil_waktu_live():
    """Ambil string waktu live lengkap"""
    now = datetime.datetime.now()
    hari   = HARI_ID[now.weekday()]
    tgl    = now.day
    bulan  = BULAN_ID[now.month]
    tahun  = now.year
    jam    = now.strftime("%H:%M:%S")
    return hari, tgl, bulan, tahun, jam

def print_live_clock():
    """Cetak live clock sekali (satu baris)"""
    hari, tgl, bulan, tahun, jam = ambil_waktu_live()
    print(
        f"  {C.BG_BLUE}{C.WHITE} 📅 {hari}, {tgl:02d} {bulan} {tahun} "
        f"{C.RESET} {C.BG_RED}{C.WHITE} ⏰ {jam} WIB {C.RESET}"
    )

def live_clock_loop(stop_event):
    """Loop update jam tiap detik (di background thread)"""
    # Simpan posisi baris ini supaya bisa ditimpa terus
    while not stop_event.is_set():
        hari, tgl, bulan, tahun, jam = ambil_waktu_live()
        # \033[2K = hapus 1 baris penuh, \r = kembali ke awal baris
        sys.stdout.write(
            f"\r  {C.BG_BLUE}{C.WHITE} 📅 {hari}, {tgl:02d} {bulan} {tahun} "
            f"{C.RESET} {C.BG_RED}{C.WHITE} ⏰ {jam} WIB {C.RESET}   "
        )
        sys.stdout.flush()
        time.sleep(1)

# ====== UTIL ======
def clear():
    os.system("clear" if os.name == "posix" else "cls")

def print_fire():
    for baris, warna in zip(FIRE_LINES, FIRE_COLORS):
        print(warna + baris + C.RESET)

def print_logo():
    print(C.YELLOW + LOGO_SPAM + C.RESET)
    print(C.RED + C.BLINK + "            ═══════ [ SIMULASI - EDUKASI ONLY ] ═══════" + C.RESET)
    print(C.CYAN + LOGO_SIMULASI + C.RESET)

def print_banner():
    clear()
    print_fire()
    print_logo()
    print(C.MAGENTA + "  ╔══════════════════════════════════════════════════════╗")
    print(C.MAGENTA + "  ║" + C.WHITE + "           🔥 Created by : " + C.YELLOW + "AZMI" + C.WHITE + " 🔥                  " + C.MAGENTA + "║")
    print(C.MAGENTA + "  ║" + C.WHITE + "           ⚠  Tidak kirim ke WhatsApp asli            " + C.MAGENTA + "║")
    print(C.MAGENTA + "  ╚══════════════════════════════════════════════════════╝" + C.RESET)
    # ==== LIVE CLOCK ====
    print_live_clock()
    print(C.ORANGE + "  " + "─"*56 + C.RESET)

# ====== LOG & SIMULASI ======
def tulis_log(nomor, pesan, status="TERCATAT"):
    now = datetime.datetime.now()
    waktu = now.strftime("%Y-%m-%d %H:%M:%S")
    baris = f"[{waktu}] [{status}] -> {nomor} : {pesan}"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(baris + "\n")
    return baris

def validasi_nomor(nomor):
    n = nomor.replace("+","").replace("-","").replace(" ","")
    return n.isdigit() and 10 <= len(n) <= 15

def mulai_simulasi(nomor, pesan, jumlah, delay):
    print(f"\n{C.CYAN}[i] Target  : {C.WHITE}{nomor}{C.RESET}")
    print(f"{C.CYAN}[i] Pesan   : {C.WHITE}{pesan}{C.RESET}")
    print(f"{C.CYAN}[i] Jumlah  : {C.WHITE}{jumlah}{C.RESET}")
    print(f"{C.CYAN}[i] Delay   : {C.WHITE}{delay}s{C.RESET}")
    print(f"{C.RED}[i] MODE    : {C.YELLOW}SIMULASI LOKAL (tidak kirim ke WA){C.RESET}\n")
    time.sleep(1)

    sukses, gagal = 0, 0
    for i in range(1, jumlah + 1):
        try:
            if random.random() < 0.05:
                log = tulis_log(nomor, pesan, "GAGAL")
                print(f"{C.RED}[{i}/{jumlah}] {log}{C.RESET}")
                gagal += 1
            else:
                log = tulis_log(nomor, pesan, "TERCATAT")
                print(f"{C.GREEN}[{i}/{jumlah}] {log}{C.RESET}")
                sukses += 1
            time.sleep(delay)
        except KeyboardInterrupt:
            print(f"\n{C.RED}[!] Dihentikan (Ctrl+C){C.RESET}")
            break
        except Exception as e:
            print(f"{C.RED}[!] Error: {e}{C.RESET}")
            gagal += 1

    print("\n" + C.ORANGE + "="*58 + C.RESET)
    print(C.CYAN + "                [ RINGKASAN SIMULASI ]" + C.RESET)
    print(C.ORANGE + "="*58 + C.RESET)
    print(f"  Target    : {C.WHITE}{nomor}{C.RESET}")
    print(f"  Sukses    : {C.GREEN}{sukses}{C.RESET}")
    print(f"  Gagal     : {C.RED}{gagal}{C.RESET}")
    print(f"  Log file  : {C.YELLOW}{LOG_FILE}{C.RESET}")
    print(C.ORANGE + "="*58 + C.RESET)
    print(f"{C.YELLOW}[i] Ini cuma simulasi lokal. Tidak ada pesan")
    print(f"    yang benar-benar terkirim ke WhatsApp.{C.RESET}\n")

def lihat_log():
    if not os.path.exists(LOG_FILE):
        print(f"\n{C.RED}[!] Belum ada log.{C.RESET}")
        return
    print(f"\n{C.CYAN}=== LOG SIMULASI ==={C.RESET}")
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        print(f.read())

def hapus_log():
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
        print(f"\n{C.GREEN}[✓] Log dihapus.{C.RESET}")
    else:
        print(f"\n{C.RED}[!] Tidak ada log.{C.RESET}")

# ====== MENU ======
def menu():
    while True:
        print_banner()
        print(f"  Nomor default : {C.YELLOW}{NOMOR_DEFAULT}{C.RESET}\n")
        print(f"  {C.GREEN}[1]{C.RESET} Mulai Simulasi")
        print(f"  {C.GREEN}[2]{C.RESET} Lihat Log")
        print(f"  {C.GREEN}[3]{C.RESET} Hapus Log")
        print(f"  {C.GREEN}[4]{C.RESET} Info / Disclaimer")
        print(f"  {C.GREEN}[5]{C.RESET} Keluar")
        pilih = input(f"\n  {C.CYAN}Pilih > {C.RESET}").strip()

        if pilih == "1":
            print_banner()
            nomor = input(f"  Nomor target [{NOMOR_DEFAULT}] > ").strip()
            if not nomor:
                nomor = NOMOR_DEFAULT
            if not validasi_nomor(nomor):
                print(f"\n{C.RED}[!] Nomor tidak valid.{C.RESET}")
                input("  Enter...")
                continue
            pesan = input("  Pesan > ").strip()
            if not pesan:
                print(f"\n{C.RED}[!] Pesan kosong.{C.RESET}")
                input("  Enter...")
                continue
            try:
                jumlah = int(input("  Jumlah  > "))
                delay  = float(input("  Delay(s)> "))
                if jumlah <= 0 or delay < 0:
                    raise ValueError
            except ValueError:
                print(f"\n{C.RED}[!] Angka tidak valid.{C.RESET}")
                input("  Enter...")
                continue
            mulai_simulasi(nomor, pesan, jumlah, delay)
            input("\n  Enter untuk kembali...")

        elif pilih == "2":
            lihat_log()
            input("\n  Enter untuk kembali...")

        elif pilih == "3":
            if input("  Yakin hapus? (y/n) > ").lower() == "y":
                hapus_log()
            input("  Enter untuk kembali...")

        elif pilih == "4":
            print_banner()
            print(C.YELLOW)
            print("  DISCLAIMER:")
            print("  - Script ini hanya menulis ke file log lokal.")
            print("  - TIDAK terhubung ke WhatsApp / internet.")
            print("  - Hanya untuk belajar Python & logika loop.")
            print("  - Spam WA ke orang lain = pelanggaran UU ITE.")
            print(C.RESET)
            input("  Enter untuk kembali...")

        elif pilih == "5":
            print(f"\n{C.GREEN}[✓] Bye! - Azmi{C.RESET}\n")
            sys.exit(0)
        else:
            print(f"\n{C.RED}[!] Pilihan tidak valid.{C.RESET}")
            time.sleep(1)

# ====== ENTRY POINT ======
if __name__ == "__main__":
    # Mulai live clock di background thread
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
