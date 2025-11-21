#!/bin/bash
cd "$(dirname "$0")"
echo "--- SETTING UP CHICAGO TICKET BOT ---"

# 1. Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python3 not found. Please install from python.org"
    exit
fi

# 2. Create Virtual Environment (if missing)
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# 3. Activate venv
source venv/bin/activate

# 4. Install Dependencies
echo "Installing libraries..."
pip install -r requirements.txt

# 5. Install Browsers (Safe to run every time)
echo "Checking browser engine..."
playwright install chromium

# 6. Run the Bot
echo "--- STARTING BOT ---"
python3 chicagoticketbot.py

echo "--- DONE ---"
# This keeps the terminal open so they can read the results
read -p "Press Enter to close..."