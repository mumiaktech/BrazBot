#!/usr/bin/env bash
# Exit on error
set -o errexit

# Activate the virtual environment (optional)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the bot
python brazbot.py
