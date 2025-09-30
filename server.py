#!/usr/bin/env python3
"""
Simple HTTP server for the Radiopaedia viewer
"""

import http.server
import socketserver
import os
import sys
import json
import shutil

PORT = 8000


class RadiopaediaHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler to serve from the web directory"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory='web', **kwargs)
    
    def end_headers(self):
        # Add CORS headers for local development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()


def ensure_data_directory():
    """Ensure the data directory exists in the web folder"""
    web_data_dir = os.path.join('web', 'data')
    os.makedirs(web_data_dir, exist_ok=True)
    
    # Copy scraped data to web directory if it exists
    scraped_data = os.path.join('data', 'playlist_data.json')
    web_data_file = os.path.join(web_data_dir, 'playlist_data.json')
    
    if os.path.exists(scraped_data):
        shutil.copy(scraped_data, web_data_file)
        print(f"Copied scraped data to {web_data_file}")
    else:
        print("No scraped data found. The viewer will use sample data.")
        print("Run 'python scraper.py' first to scrape real data.")


def main():
    """Start the web server"""
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Ensure data is available
    ensure_data_directory()
    
    # Parse port from command line if provided
    port = int(sys.argv[1]) if len(sys.argv) > 1 else PORT
    
    with socketserver.TCPServer(("", port), RadiopaediaHandler) as httpd:
        print(f"\n{'='*60}")
        print(f"Radiopaedia Viewer Server")
        print(f"{'='*60}")
        print(f"\nServer running at: http://localhost:{port}")
        print(f"\nPress Ctrl+C to stop the server\n")
        print(f"{'='*60}\n")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\nShutting down server...")
            httpd.shutdown()


if __name__ == '__main__':
    main()
