#!/bin/bash
set -ex  # Print each command and stop on error

echo "Python Version:"
python --version

echo "Pip Version:"
pip --version

echo "Installing Dependencies:"
pip install -r requirements.txt
echo "Dependencies Installed Successfully"

echo "Environment Info:"
env | sort

echo "Build Completed Successfully"
exit 0
