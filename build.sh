#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies using requirements.txt
pip install -r requirements.txt

# Start your Python application
python brazbot.py
