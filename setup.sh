#!/bin/bash

# Setup script for the Data Model Project
# This script installs all necessary dependencies for the project

echo "=========================================="
echo "Setting up Data Model Project"
echo "=========================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

echo "Python 3 found: $(python3 --version)"

# Upgrade pip
echo ""
echo "Upgrading pip..."
python3 -m pip install --upgrade pip

# Install required Python packages
echo ""
echo "Installing Python dependencies..."
pip install pandas numpy matplotlib jupyter jupyterlab

# Verify installations
echo ""
echo "=========================================="
echo "Verifying installations..."
echo "=========================================="

python3 -c "import pandas; print('✓ pandas:', pandas.__version__)"
python3 -c "import numpy; print('✓ numpy:', numpy.__version__)"
python3 -c "import matplotlib; print('✓ matplotlib:', matplotlib.__version__)"
python3 -c "import jupyter; print('✓ jupyter installed')"
python3 -c "import jupyterlab; print('✓ jupyterlab installed')"

echo ""
echo "=========================================="
echo "Setup Complete!"
echo "=========================================="
echo ""
echo "To start working with notebooks, run:"
echo "  jupyter lab --port 8888"
echo ""
echo "Or:"
echo "  jupyter notebook"
echo ""
