#!/usr/bin/env bash
# ============================================================
# ForgeMotion CLI — launcher Linux / Termux / Mac
# Jalankan:  chmod +x run.sh && ./run.sh
# ============================================================
cd "$(dirname "$0")" || exit 1

if command -v python3 >/dev/null 2>&1; then
    exec python3 main.py
elif command -v python >/dev/null 2>&1; then
    exec python main.py
else
    echo "Python belum terpasang."
    echo "  Termux : pkg install python"
    echo "  Linux  : sudo apt install python3"
    exit 1
fi
