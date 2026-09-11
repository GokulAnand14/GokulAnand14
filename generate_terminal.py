import os
import gifos

os.environ["GIFOS_GENERAL_COLOR_SCHEME"] = "catppuccin-mocha"

def main():
    t = gifos.Terminal(
        width=680,
        height=320,
        xpad=15,
        ypad=15,
        font_size=16,
        line_spacing=4
    )
    t.set_fps(15)

    # Boot / Login sequence
    t.toggle_show_cursor(False)
    t.gen_text("\x1b[94mGAllium OS v2.4 (x86_64 tty1)\x1b[0m", 1, count=3)
    t.gen_text("login: ", 3, count=2)
    t.toggle_show_cursor(True)
    t.gen_typing_text("gokul", 3, contin=True, speed=1)
    
    t.toggle_show_cursor(False)
    t.gen_text("password: ", 4, count=2)
    t.toggle_show_cursor(True)
    t.gen_typing_text("********", 4, contin=True, speed=1)
    
    t.toggle_show_cursor(False)
    t.gen_text("\x1b[90mLast login: Fri Sep 11 2026 on tty1\x1b[0m", 6, count=3)

    # Clear screen simulation
    t.gen_text("\x1b[92mgokul@dev\x1b[0m:\x1b[94m~\x1b[0m$ ", 8)
    t.toggle_show_cursor(True)
    t.gen_typing_text("clear", 8, contin=True, speed=1)
    t.clone_frame(2)

    # Fastfetch execution
    t.clear_frame()
    t.toggle_show_cursor(False)
    t.gen_text("\x1b[92mgokul@dev\x1b[0m:\x1b[94m~\x1b[0m$ ", 1)
    t.toggle_show_cursor(True)
    t.gen_typing_text("fastfetch", 1, contin=True, speed=1)
    t.clone_frame(2)

    # Specs table with color accents
    t.toggle_show_cursor(False)
    lines = [
        "  \x1b[94m_____\x1b[0m     \x1b[95muser:\x1b[0m     Gokul Anand R [GAllium] (17)",
        " \x1b[94m/ ____|\x1b[0m    \x1b[95muptime:\x1b[0m   17 Years",
        "\x1b[94m| |  __\x1b[0m     \x1b[95mbuilding:\x1b[0m excalideck (Native Excalidraw + Obsidian)",
        "\x1b[94m| | |_ |\x1b[0m    \x1b[95mstack:\x1b[0m    Rust, Tauri, TypeScript, Next.js, Linux",
        " \x1b[94m\\_____|\x1b[0m    \x1b[95mperk:\x1b[0m     not bad at multiple skills",
        "            \x1b[95mcontact:\x1b[0m  linkedin.com/in/gokul-anand",
    ]
    for idx, l in enumerate(lines):
        t.gen_text(l, 3 + idx, count=1)

    t.clone_frame(3)
    
    # Run cargo build
    t.gen_text("\x1b[92mgokul@dev\x1b[0m:\x1b[94m~\x1b[0m$ ", 10)
    t.toggle_show_cursor(True)
    t.gen_typing_text("cargo build --release", 10, contin=True, speed=1)
    t.clone_frame(2)
    
    t.toggle_show_cursor(False)
    t.gen_text("   \x1b[92mCompiling\x1b[0m excalideck-core v0.1.0 (release)", 11, count=1)
    t.gen_text("    \x1b[92mFinished\x1b[0m release [optimized] target(s) in 1.42s", 12, count=1)

    t.gen_text("\x1b[92mgokul@dev\x1b[0m:\x1b[94m~\x1b[0m$ ", 14)
    t.toggle_show_cursor(True)
    t.gen_typing_text("# ready to ship. thanks for stopping by! _", 14, contin=True, speed=1)
    
    # Freeze final frame so it remains visible permanently
    t.clone_frame(10)

    # Render non-repeating GIF (-loop -1)
    os.system(
        'ffmpeg -hide_banner -loglevel error -y -r 15 -i "frames/frame_%d.png" -filter_complex "[0:v] split [a][b];[a] palettegen [p];[b][p] paletteuse" -loop -1 terminal.gif'
    )
    print("Non-repeating terminal GIF generated successfully!")

if __name__ == "__main__":
    main()
