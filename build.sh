#!/usr/bin/env bash
# exit on error
set -o errexit

# Check Python version
echo "Python version:"
python3 --version

# Upgrade pip and build tools
pip install --upgrade pip setuptools wheel

# Install dependencies
# Use --only-binary to prefer pre-built wheels and avoid compilation
pip install --only-binary :all: -r src/requirements.txt || pip install -r src/requirements.txt

# Run database migrations (optional - uncomment if you want auto-migrations on deploy)
# cd src
# alembic upgrade head

