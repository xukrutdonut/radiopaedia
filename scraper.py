#!/usr/bin/env python3
"""
Radiopaedia Playlist Scraper
Scrapes case information from a radiopaedia.org playlist
"""

import requests
from bs4 import BeautifulSoup
import json
import os
import time


class RadiopaediaScraper:
    """Scraper for radiopaedia.org playlists"""
    
    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.base_url = "https://radiopaedia.org"
        self.playlist_url = f"{self.base_url}/playlists/{playlist_id}"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def scrape_playlist(self):
        """Scrape the playlist page and extract case information"""
        print(f"Scraping playlist: {self.playlist_url}")
        
        try:
            response = self.session.get(self.playlist_url)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Error fetching playlist: {e}")
            return None
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract playlist information
        playlist_data = {
            'id': self.playlist_id,
            'url': self.playlist_url,
            'title': self._extract_title(soup),
            'description': self._extract_description(soup),
            'cases': self._extract_cases(soup)
        }
        
        return playlist_data
    
    def _extract_title(self, soup):
        """Extract playlist title"""
        title_elem = soup.find('h1') or soup.find('title')
        if title_elem:
            return title_elem.get_text(strip=True)
        return f"Playlist {self.playlist_id}"
    
    def _extract_description(self, soup):
        """Extract playlist description"""
        desc_elem = soup.find('div', class_='description') or soup.find('p')
        if desc_elem:
            return desc_elem.get_text(strip=True)
        return ""
    
    def _extract_cases(self, soup):
        """Extract case information from the playlist"""
        cases = []
        
        # Look for case links (common patterns in radiopaedia)
        case_links = soup.find_all('a', href=lambda x: x and '/cases/' in x)
        
        seen_cases = set()
        for link in case_links:
            case_url = link.get('href', '')
            if not case_url.startswith('http'):
                case_url = self.base_url + case_url
            
            # Extract case ID from URL
            if '/cases/' in case_url:
                case_id = case_url.split('/cases/')[-1].split('?')[0].split('#')[0]
                
                # Avoid duplicates
                if case_id in seen_cases:
                    continue
                seen_cases.add(case_id)
                
                case_info = {
                    'id': case_id,
                    'url': case_url,
                    'title': link.get_text(strip=True) or f"Case {case_id}",
                }
                
                cases.append(case_info)
        
        return cases
    
    def scrape_case_details(self, case_url):
        """Scrape detailed information from a specific case"""
        print(f"Scraping case: {case_url}")
        
        try:
            response = self.session.get(case_url)
            response.raise_for_status()
            time.sleep(1)  # Be respectful with rate limiting
        except requests.RequestException as e:
            print(f"Error fetching case: {e}")
            return None
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        case_data = {
            'url': case_url,
            'title': self._extract_case_title(soup),
            'presentation': self._extract_case_presentation(soup),
            'diagnosis': self._extract_case_diagnosis(soup),
            'images': self._extract_case_images(soup)
        }
        
        return case_data
    
    def _extract_case_title(self, soup):
        """Extract case title"""
        title_elem = soup.find('h1')
        if title_elem:
            return title_elem.get_text(strip=True)
        return "Untitled Case"
    
    def _extract_case_presentation(self, soup):
        """Extract case presentation/description"""
        presentation = soup.find('div', class_='case-section')
        if presentation:
            return presentation.get_text(strip=True)
        return ""
    
    def _extract_case_diagnosis(self, soup):
        """Extract case diagnosis"""
        diagnosis = soup.find('div', class_='diagnosis')
        if diagnosis:
            return diagnosis.get_text(strip=True)
        return ""
    
    def _extract_case_images(self, soup):
        """Extract image URLs from the case"""
        images = []
        
        # Look for image elements
        img_elements = soup.find_all('img', src=True)
        
        for img in img_elements:
            src = img.get('src', '')
            if src and ('cdn' in src or 'images' in src):
                if not src.startswith('http'):
                    src = self.base_url + src
                
                images.append({
                    'url': src,
                    'alt': img.get('alt', ''),
                    'title': img.get('title', '')
                })
        
        return images
    
    def save_data(self, data, filename='data/playlist_data.json'):
        """Save scraped data to JSON file"""
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"Data saved to {filename}")


def main():
    """Main function to run the scraper"""
    import sys
    
    # Get playlist ID from command line or use default
    playlist_id = sys.argv[1] if len(sys.argv) > 1 else "85715"
    
    scraper = RadiopaediaScraper(playlist_id)
    
    # Scrape the playlist
    playlist_data = scraper.scrape_playlist()
    
    if playlist_data:
        print(f"\nFound {len(playlist_data['cases'])} cases in playlist")
        
        # Optionally scrape individual cases
        if len(sys.argv) > 2 and sys.argv[2] == '--full':
            print("\nScraping individual cases...")
            for i, case in enumerate(playlist_data['cases'], 1):
                print(f"[{i}/{len(playlist_data['cases'])}] ", end='')
                case_details = scraper.scrape_case_details(case['url'])
                if case_details:
                    case.update(case_details)
        
        # Save the data
        scraper.save_data(playlist_data)
        print("\nScraping completed successfully!")
    else:
        print("Failed to scrape playlist")
        sys.exit(1)


if __name__ == '__main__':
    main()
