@echo off
rem ============================================================
rem ForgeMotion CLI - launcher Windows
rem Dobel-klik file ini atau jalankan dari cmd: run.bat
rem ============================================================
cd /d "%~dp0"

where python >nul 2>nul
if %errorlevel%==0 (
    python main.py
) else (
    where py >nul 2>nul
    if %errorlevel%==0 (
        py main.py
    ) else (
        echo Python belum terpasang. Unduh di https://www.python.org/downloads/
        echo Pastikan mencentang "Add Python to PATH" saat instalasi.
    )
)
pause
