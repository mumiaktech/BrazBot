#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies using pipenv
pipenv install --deploy --ignore-pipfile

# Start your Python application
pipenv run python brazbot.py
