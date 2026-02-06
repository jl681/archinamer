#!/bin/bash

# 1. Colors for better visibility
GREEN='\033[0;32m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🏗️  Starting Archinamer Setup...${NC}"

# 2. Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Error: Python 3 is not installed.${NC}"
    echo "Please install Python 3 before running this setup."
    exit 1
fi

# Optional: Verify minimum version (e.g., 3.8+)
PY_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
echo -e "Found Python $PY_VERSION"

# 3. Create Virtual Environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo -e "Creating virtual environment..."
    python3 -m venv .venv
fi

# 4. Activate the environment
source .venv/bin/activate

# 5. Upgrade pip and install in Editable Mode
echo -e "Installing dependencies and registering 'archinamer' command..."
pip install --upgrade pip
pip install -e .

# 6. Check for .env file
if [ ! -f ".env" ]; then
    echo -e "${BLUE}⚠️  No .env file found. Creating a template...${NC}"
    echo "DASHSCOPE_API_KEY=your_api_key_here" > .env
    echo "Please edit the .env file with your actual QWEN api key."
fi

echo -e "${GREEN}✅ Setup Complete!${NC}"
echo -e "To start using the tool, run: ${BLUE}source .venv/bin/activate${NC}"
echo -e "Then just type: ${BLUE}archinamer \"your project idea\"${NC}"