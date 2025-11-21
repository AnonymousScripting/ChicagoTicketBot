@echo off
cd /d "%~dp0"
echo --- SETTING UP CHICAGO TICKET BOT ---

:: 1. Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not in your PATH.
    echo Please install it from https://www.python.org/downloads/
    echo IMPORTANT: Check the box "Add Python to PATH" during installation.
    pause
    exit
)

:: 2. Create Virtual Environment if missing
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

:: 3. Activate venv (Windows uses Scripts\activate)
call venv\Scripts\activate

:: 4. Install Dependencies
echo Installing libraries...
pip install -r requirements.txt

:: 5. Install Browsers
echo Checking browser engine...
playwright install chromium

:: 6. Run the Bot
echo --- STARTING BOT ---
python chicagoticketbot.py

echo --- DONE ---
pause