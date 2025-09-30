#!/bin/bash
# Quick start script for Radiopaedia Pediatric Radiology

echo "=================================================="
echo "  Radiología Pediátrica - Quick Start"
echo "=================================================="
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python -m venv venv
    echo "✓ Virtual environment created"
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Check if dependencies are installed
if ! python -c "import flask" 2>/dev/null; then
    echo "📥 Installing dependencies..."
    pip install -r requirements.txt
    echo "✓ Dependencies installed"
else
    echo "✓ Dependencies already installed"
fi

echo ""
echo "Choose an option:"
echo "  1) Run the scraper (extract cases from Radiopaedia)"
echo "  2) Start the web application (view cases)"
echo "  3) Exit"
echo ""
read -p "Enter your choice (1-3): " choice

case $choice in
    1)
        echo ""
        read -p "Enter playlist URL (or press Enter for default): " url
        if [ -z "$url" ]; then
            python scraper.py
        else
            python scraper.py "$url"
        fi
        ;;
    2)
        echo ""
        echo "Starting web application..."
        echo "Open your browser at: http://localhost:5000"
        echo ""
        python webapp.py
        ;;
    3)
        echo "Goodbye!"
        exit 0
        ;;
    *)
        echo "Invalid choice. Exiting."
        exit 1
        ;;
esac
