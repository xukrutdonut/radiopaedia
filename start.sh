#!/bin/bash
# Quick start script for Radiopaedia Viewer

echo "=========================================="
echo "Radiopaedia Viewer - Quick Start"
echo "=========================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    exit 1
fi

# Check if dependencies are installed
if ! python3 -c "import requests" 2>/dev/null; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
    echo ""
fi

# Check if data exists
if [ ! -f "data/playlist_data.json" ]; then
    echo "No scraped data found."
    echo "The viewer will use sample data."
    echo ""
    echo "To scrape real data, run:"
    echo "  python3 scraper.py 85715"
    echo ""
fi

# Start the server
echo "Starting web server..."
echo ""
python3 server.py 8000
