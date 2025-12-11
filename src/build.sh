#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install --upgrade pip
pip install -r src/requirements.txt

# Run database migrations (optional - uncomment if you want auto-migrations on deploy)
# cd src
# alembic upgrade head

