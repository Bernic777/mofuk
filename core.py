#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Mofuk (Moi) — To Vanish / Disappear / Be No Longer Visible
----------------------------------------------------------
Origin & Inspiration:
Inspired by the Moi Tribe of West Papua, Indonesia — an indigenous community 
continuing their steadfast struggle against forest exploitation.

The Philosophy:
The name represents the principle of vanishing without a trace.
- Minimal Exposure: Preferring substance over visibility.
- Low Digital Footprint: Existing quietly in a noisy world.
- Respect for Sustainability: Leaving the earth exactly as we found it.

Script Function:
A meditatively designed Tor Identity Rotation tool. It secures your digital 
footprint by automating IP rotation while reminding us of our ecological footprint.
"""

import sys
import os
import time
import shutil
import subprocess
import signal
import random

# --- System Configuration ---
PROXY_HOST = "127.0.0.1"
PROXY_PORT = 9050
TARGET_URL = "https://api.ipify.org"
CMD_RELOAD = "service tor reload"
CMD_START = "service tor start"

# --- Runtime Data ---
LOG_HISTORY = [] # Stores the IP rotation logs

# --- Mofuk Philosophy Quotes (Complete Collection) ---
QUOTES = [
    {"en": "We were not born evil; we practiced it daily.", "id": "Kita tidak terlahir jahat; kita melatihnya setiap hari. Selamatkan pohon!"},
    {"en": "Humanity didn’t conquer nature—nature tolerated us.", "id": "Manusia tidak menaklukkan alam—alam hanya menoleransi kita. Selamatkan pohon!"},
    {"en": "We mistook consumption for purpose.", "id": "Kita mengira konsumsi adalah tujuan hidup. Selamatkan pohon!"},
    {"en": "The planet was stable until we called it progress.", "id": "Planet ini stabil sampai kita menyebutnya kemajuan. Selamatkan pohon!"},
    {"en": "We cut roots, then asked why everything fell.", "id": "Kita memotong akar, lalu bertanya kenapa semuanya roboh. Selamatkan pohon!"},
    {"en": "Intelligence without restraint is just efficient destruction.", "id": "Kecerdasan tanpa kendali hanyalah kehancuran yang efisien. Selamatkan pohon!"},
    {"en": "We didn’t lose harmony; we traded it.", "id": "Kita tidak kehilangan harmoni; kita menukarnya. Selamatkan pohon!"},
    {"en": "Earth was never fragile. Our ethics were.", "id": "Bumi tidak pernah rapuh. Etika kitalah yang rapuh. Selamatkan pohon!"},
    {"en": "We called it survival of the fittest—then eliminated life itself.", "id": "Kita menyebutnya seleksi alam—lalu melenyapkan kehidupan itu sendiri. Selamatkan pohon!"},
    {"en": "A species that cannot limit itself signs its own extinction.", "id": "Spesies yang tak bisa membatasi diri menandatangani kepunahannya sendiri. Selamatkan pohon!"},
    {"en": "We turned forests into numbers and wondered why they stopped breathing.", "id": "Kita mengubah hutan menjadi angka dan heran mengapa ia berhenti bernapas. Selamatkan pohon!"},
    {"en": "Morality failed quietly, long before nature screamed.", "id": "Moralitas runtuh diam-diam, jauh sebelum alam berteriak. Selamatkan pohon!"},
    {"en": "We treated tomorrow as disposable.", "id": "Kita memperlakukan hari esok seperti barang sekali pakai. Selamatkan pohon!"},
    {"en": "Civilization grew taller as its foundations rotted.", "id": "Peradaban tumbuh tinggi sementara fondasinya membusuk. Selamatkan pohon!"},
    {"en": "We replaced reverence with ownership.", "id": "Kita mengganti rasa hormat dengan kepemilikan. Selamatkan pohon!"},
    {"en": "A planet can survive without humans. The opposite was the illusion.", "id": "Planet bisa bertahan tanpa manusia. Kebalikannya hanyalah ilusi. Selamatkan pohon!"},
    {"en": "We didn’t misunderstand nature—we ignored it.", "id": "Kita tidak salah paham pada alam—kita mengabaikannya. Selamatkan pohon!"},
    {"en": "Growth without wisdom is decay in disguise.", "id": "Pertumbuhan tanpa kebijaksanaan adalah pembusukan yang menyamar. Selamatkan pohon!"},
    {"en": "We worshipped speed and forgot direction.", "id": "Kita menyembah kecepatan dan melupakan arah. Selamatkan pohon!"},
    {"en": "We wanted dominance, not balance.", "id": "Kita menginginkan dominasi, bukan keseimbangan. Selamatkan pohon!"},
    {"en": "Nature kept accounts. We ignored the debt.", "id": "Alam mencatat segalanya. Kita mengabaikan hutangnya. Selamatkan pohon!"},
    {"en": "We learned how to extract, not how to stop.", "id": "Kita belajar cara mengambil, bukan cara berhenti. Selamatkan pohon!"},
    {"en": "Human pride was louder than planetary limits.", "id": "Kesombongan manusia lebih keras dari batas planet. Selamatkan pohon!"},
    {"en": "We measured success by damage we could afford.", "id": "Kita mengukur sukses dari kerusakan yang sanggup kita bayar. Selamatkan pohon!"},
    {"en": "Extinction is not a punishment; it’s a consequence.", "id": "Kepunahan bukan hukuman; ia konsekuensi. Selamatkan pohon!"},
    {"en": "We thought we were outside nature. That was the error.", "id": "Kita mengira berada di luar alam. Itulah kesalahannya. Selamatkan pohon!"},
    {"en": "Forests died quietly while markets celebrated.", "id": "Hutan mati dalam diam sementara pasar berpesta. Selamatkan pohon!"},
    {"en": "We mastered tools but failed character.", "id": "Kita menguasai alat, tapi gagal membangun karakter. Selamatkan pohon!"},
    {"en": "A species that eats its habitat calls it destiny.", "id": "Spesies yang memakan habitatnya sendiri menyebutnya takdir. Selamatkan pohon!"},
    {"en": "The end won’t be sudden—it will be deserved.", "id": "Akhirnya tidak mendadak—ia pantas terjadi. Selamatkan pohon!"},
    {"en": "We optimized profit, not permanence.", "id": "Kita mengoptimalkan laba, bukan keberlanjutan. Selamatkan pohon!"},
    {"en": "Nature doesn’t negotiate with denial.", "id": "Alam tidak bernegosiasi dengan penyangkalan. Selamatkan pohon!"},
    {"en": "We burned libraries written in leaves.", "id": "Kita membakar perpustakaan yang ditulis oleh daun. Selamatkan pohon!"},
    {"en": "Humanity became efficient at its own erasure.", "id": "Manusia menjadi efisien dalam menghapus dirinya sendiri. Selamatkan pohon!"},
    {"en": "We asked how much we could take, not how long we could last.", "id": "Kita bertanya seberapa banyak bisa diambil, bukan seberapa lama bisa bertahan. Selamatkan pohon!"},
    {"en": "The future was sacrificed for quarterly comfort.", "id": "Masa depan dikorbankan demi kenyamanan sesaat. Selamatkan pohon!"},
    {"en": "We called warning signs opinions.", "id": "Kita menyebut tanda peringatan sebagai opini. Selamatkan pohon!"},
    {"en": "A dying planet reflects a dying conscience.", "id": "Planet yang sekarat mencerminkan nurani yang sekarat. Selamatkan pohon!"},
    {"en": "We believed technology would forgive us.", "id": "Kita percaya teknologi akan memaafkan kita. Selamatkan pohon!"},
    {"en": "Save trees—not to save Earth, but to postpone human silence.", "id": "Selamatkan pohon—bukan untuk menyelamatkan Bumi, tapi untuk menunda keheningan manusia. Selamatkan pohon!"}
]

class TermUI:
    """Handles terminal visual output."""
    R = '\033[91m' # Red
    G = '\033[92m' # Green
    C = '\033[96m' # Cyan
    Y = '\033[93m' # Yellow
    W = '\033[0m'  # White/Reset
    B = '\033[1m'  # Bold
    DIM = '\033[2m' # Dim
    ITL = '\033[3m' # Italic
    
    # ANSI Codes for Robust Control
    HIDE_CURSOR = '\033[?25l'
    SHOW_CURSOR = '\033[?25h'
    HOME = '\033[H' # Move cursor to top-left (0,0)
    CLR_LINE = '\033[K' # Clear line from cursor to right end

    @staticmethod
    def banner_print():
        """Returns the banner string lines."""
        return f"""{TermUI.C}{TermUI.B}
    __  ___      ____      __
   /  |/  /___  / __/_  __/ /__
  / /|_/ / __ \/ /_/ / / / //_/
 / /  / / /_/ / __/ /_/ / ,<   
/_/  /_/\____/_/  \__,_/_/|_|  
        {TermUI.W}:: Tor Identity Rotation Engine v0.3 ::
   {TermUI.C}"Mofuk (Moi) means To Vanish / Disappear / Be No Longer Visible"
   
"Moi is a tribe in West Papua, Indonesia. who are struggling with forest exploitation. Save the trees.!"{TermUI.W}
        """

    @staticmethod
    def status(msg, type="info"):
        """Adds a message to the LOG_HISTORY instead of printing directly."""
        timestamp = time.strftime("%H:%M:%S")
        if type == "info":
            prefix = f"{TermUI.C}[*]{TermUI.W}"
        elif type == "success":
            prefix = f"{TermUI.G}[+]{TermUI.W}"
        elif type == "error":
            prefix = f"{TermUI.R}[!]{TermUI.W}"
        elif type == "warn":
            prefix = f"{TermUI.Y}[?]{TermUI.W}"
        else:
            prefix = f"[{type}]"
            
        formatted_msg = f"{TermUI.DIM}{timestamp}{TermUI.W} {prefix} {msg}"
        LOG_HISTORY.append(formatted_msg)
        # Keep history manageable (last 10 lines)
        if len(LOG_HISTORY) > 10:
            LOG_HISTORY.pop(0)

    @staticmethod
    def render_frame(current_quote_idx, start_time, total_duration):
        """
        Redraws the ENTIRE screen from top to bottom.
        This eliminates "cursor jump" artifacts and ensures a stable layout.
        """
        now = time.time()
        elapsed_total = now - start_time
        remaining = int(total_duration - elapsed_total)
        if remaining < 0: remaining = 0

        # 1. Reset Cursor to Home (0,0) - No screen clearing, just overwrite
        buffer = f"{TermUI.HOME}"
        
        # 2. Build Banner
        # Split banner into lines to ensure CLR_LINE is applied
        banner_lines = TermUI.banner_print().strip('\n').split('\n')
        for line in banner_lines:
            buffer += f"{line}{TermUI.CLR_LINE}\n"
        
        # 3. Build Quotes Section
        buffer += f"{TermUI.DIM}--- PHILOSOPHY ---{TermUI.W}{TermUI.CLR_LINE}\n"
        
        # Quote Logic (Standard: 7 seconds per quote)
        quote_duration = 7.0
        cycle_count = int(elapsed_total // quote_duration)
        actual_idx = (current_quote_idx + cycle_count) % len(QUOTES)
        q = QUOTES[actual_idx]
        
        # Typing Effect
        quote_start_time = start_time + (cycle_count * quote_duration)
        elapsed_quote = now - quote_start_time
        # Speed adapts to ensure readability within 7s
        typing_speed = 35 if total_duration > 2 else 100 
        char_limit = int(elapsed_quote * typing_speed)
        
        txt_en = q['en'][:char_limit]
        txt_id = q['id'][:char_limit]
        cursor = "█" if int(now * 2) % 2 == 0 else " "

        cursor_en = cursor if len(txt_en) < len(q['en']) else ""
        buffer += f" {TermUI.C}EN:{TermUI.W} {txt_en}{TermUI.C}{cursor_en}{TermUI.W}{TermUI.CLR_LINE}\n"
        
        cursor_id = cursor if len(txt_id) < len(q['id']) else ""
        buffer += f" {TermUI.G}ID:{TermUI.W} {TermUI.ITL}{txt_id}{TermUI.W}{TermUI.G}{cursor_id}{TermUI.W}{TermUI.CLR_LINE}\n"
        
        # Spacer
        buffer += f"{TermUI.CLR_LINE}\n"

        # 4. Build Logs Section
        buffer += f"{TermUI.DIM}--- SYSTEM LOGS ---{TermUI.W}{TermUI.CLR_LINE}\n"
        lines_printed = 0
        for log in LOG_HISTORY:
            buffer += f"{log}{TermUI.CLR_LINE}\n"
            lines_printed += 1
        
        # Fill empty log space to maintain fixed height
        while lines_printed < 10:
            buffer += f"{TermUI.DIM}~{TermUI.W}{TermUI.CLR_LINE}\n"
            lines_printed += 1

        # 5. Build Status Bar
        spinner = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"[int(now * 10) % 10]
        buffer += f"{TermUI.DIM}[{TermUI.W}{TermUI.C}{spinner}{TermUI.W}{TermUI.DIM}] Waiting... {TermUI.W}{remaining}s {TermUI.DIM}|{TermUI.W} Vanish Protocol Active{TermUI.CLR_LINE}"

        # 6. Flush Buffer to Screen
        sys.stdout.write(buffer)
        sys.stdout.flush()

    @staticmethod
    def meditate(duration):
        """
        Main Loop Driver during wait time.
        """
        # Hide Cursor for visual cleanliness
        sys.stdout.write(TermUI.HIDE_CURSOR)
        
        end_time = time.time() + duration
        start_time = time.time()
        current_idx = random.randint(0, len(QUOTES) - 1)

        while time.time() < end_time:
            TermUI.render_frame(current_idx, start_time, duration)
            time.sleep(0.05) 
        
        # Final render
        TermUI.render_frame(current_idx, start_time, duration)
        
        # Restore Cursor
        sys.stdout.write(TermUI.SHOW_CURSOR)
        print("") # Move down one line to prevent overwrite by next print

def assert_sudo():
    if os.geteuid() != 0:
        print("Root privileges required.")
        sys.exit(1)

def resolve_modules():
    try:
        import requests
    except ImportError:
        # Since this is now a package core file, we assume pip install handled deps,
        # but we can check just in case or warn.
        print("Installing requests...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "requests[socks]"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except:
            sys.exit(1)
    
    if shutil.which('tor') is None:
        print("Installing tor...")
        os.system("apt-get update -qq && apt-get install tor -y -qq > /dev/null")

def daemon_ignite():
    try:
        with open(os.devnull, 'w') as devnull:
            subprocess.call(CMD_START.split(), stdout=devnull, stderr=devnull)
    except:
        pass

def fetch_identity():
    import requests
    session = requests.session()
    session.proxies = {
        'http':  f'socks5://{PROXY_HOST}:{PROXY_PORT}',
        'https': f'socks5://{PROXY_HOST}:{PROXY_PORT}'
    }
    try:
        r = session.get(TARGET_URL, timeout=8)
        return r.text.strip()
    except:
        return "Unknown/Offline"

def rotate_circuit():
    try:
        os.system(f"{CMD_RELOAD} > /dev/null 2>&1")
        return True
    except:
        return False

def terminate(sig, frame):
    # Restore cursor on exit
    sys.stdout.write('\033[?25h')
    print("\n\nExiting...")
    sys.exit(0)

def main_sequence():
    assert_sudo()
    resolve_modules()
    
    # Daemon check usually done before execution
    daemon_ignite()
    
    # Hide cursor initially
    sys.stdout.write(TermUI.HIDE_CURSOR)
    
    TermUI.status("Initializing Mofuk Protocol...", "info")
    
    current_id = fetch_identity()
    TermUI.status(f"Initial IP: {TermUI.B}{current_id}{TermUI.W}", "success")

    # Clear screen initially for clean start
    os.system('cls' if os.name == 'nt' else 'clear')
    
    try:
        # Show cursor for input
        sys.stdout.write(TermUI.SHOW_CURSOR)
        print(TermUI.banner_print()) # Print banner once for context
        # Default changed to 7s as requested in previous logic
        interval_input = input(f"{TermUI.C}[?]{TermUI.W} Silence Duration (sec) [7]: ") or "7"
        interval = int(interval_input)
        
        cycles_input = input(f"{TermUI.C}[?]{TermUI.W} Total Shifts (0=Infinite): ") or "0"
        cycles = int(cycles_input)
        
        sys.stdout.write(TermUI.HIDE_CURSOR)
    except ValueError:
        interval, cycles = 7, 0
    
    TermUI.status("VANISH PROTOCOL ENGAGED", "warn")
    
    count = 0
    while True:
        try:
            if cycles > 0 and count >= cycles:
                TermUI.status("Cycle limit reached.", "success")
                # Final clean render
                os.system('cls' if os.name == 'nt' else 'clear')
                print(TermUI.banner_print())
                for log in LOG_HISTORY[-10:]: print(log)
                print(f"{TermUI.G}[+] Mission Complete.{TermUI.W}")
                break
                
            # Execute meditative wait (Full Redraw Architecture)
            TermUI.meditate(interval)
            
            rotate_circuit()
            
            new_id = fetch_identity()
            count += 1
            
            TermUI.status(f"Cycle {count} >> New Identity: {TermUI.B}{new_id}{TermUI.W}", "success")
            
        except KeyboardInterrupt:
            terminate(None, None)
        except Exception as e:
            TermUI.status(f"Runtime error: {e}", "error")

if __name__ == "__main__":
    signal.signal(signal.SIGINT, terminate)
    main_sequence()
