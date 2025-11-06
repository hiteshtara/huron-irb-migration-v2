#!/usr/bin/env bash
# ==========================================================
#  Huron IRB Migration - Virtual Environment Setup Script
# ==========================================================
#  This script creates and activates a Python virtual environment,
#  installs required packages, and validates setup.
# ----------------------------------------------------------

set -e  # Exit immediately on error

echo "---------------------------------------------"
echo "Setting up Python virtual environment (venv)..."
echo "---------------------------------------------"

# Determine Python command
if command -v python3 &>/dev/null; then
    PYTHON_CMD="python3"
else
    PYTHON_CMD="python"
fi

# 1️⃣ Create venv if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating new virtual environment..."
    $PYTHON_CMD -m venv venv
else
    echo "Virtual environment already exists. Skipping creation."
fi

# 2️⃣ Activate venv
echo "Activating virtual environment..."
source venv/bin/activate

# 3️⃣ Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# 4️⃣ Install dependencies
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

# 5️⃣ Verify installation
echo "---------------------------------------------"
echo "Verifying installed packages..."
echo "---------------------------------------------"
pip list

echo ""
echo "✅ Setup complete!"
echo "To activate your environment in future sessions, run:"
echo "source venv/bin/activate"
echo ""
