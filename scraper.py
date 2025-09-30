#!/usr/bin/env python3
"""
Radiopaedia Playlist Scraper
Scrapes cases from a Radiopaedia playlist for creating a pediatric radiology website
"""

import requests
from bs4 import BeautifulSoup
import json
import os
import time
from typing import List, Dict
import sys


class RadiopaediaScraper:
    """Scraper for Radiopaedia playlists"""
    
    def __init__(self, playlist_url: str):
        """
        Initialize the scraper
        
        Args:
            playlist_url: URL of the Radiopaedia playlist
        """
        self.playlist_url = playlist_url
        self.base_url = "https://radiopaedia.org"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
    def get_playlist_cases(self) -> List[str]:
        """
        Extract case URLs from the playlist
        
        Returns:
            List of case URLs
        """
        print(f"Fetching playlist: {self.playlist_url}")
        try:
            response = self.session.get(self.playlist_url)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            case_links = []
            
            # Find all case links in the playlist
            for link in soup.find_all('a', href=True):
                href = link['href']
                if '/cases/' in href and href not in case_links:
                    full_url = href if href.startswith('http') else f"{self.base_url}{href}"
                    case_links.append(full_url)
            
            print(f"Found {len(case_links)} cases in playlist")
            return case_links
            
        except requests.RequestException as e:
            print(f"Error fetching playlist: {e}")
            return []
    
    def scrape_case(self, case_url: str) -> Dict:
        """
        Scrape a single case
        
        Args:
            case_url: URL of the case
            
        Returns:
            Dictionary with case information
        """
        print(f"Scraping case: {case_url}")
        
        try:
            response = self.session.get(case_url)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract case information
            case_data = {
                'url': case_url,
                'title': '',
                'patient_data': {},
                'study': '',
                'findings': '',
                'diagnosis': '',
                'discussion': '',
                'images': []
            }
            
            # Extract title
            title_elem = soup.find('h1')
            if title_elem:
                case_data['title'] = title_elem.get_text(strip=True)
            
            # Extract patient data
            patient_section = soup.find('div', class_='case-section data-section')
            if patient_section:
                for item in patient_section.find_all('div', class_='data-item'):
                    label_elem = item.find('span', class_='data-item-label')
                    value_elem = item.find('span', class_='data-item-value')
                    if label_elem and value_elem:
                        label = label_elem.get_text(strip=True).rstrip(':')
                        value = value_elem.get_text(strip=True)
                        case_data['patient_data'][label] = value
            
            # Extract study information
            study_section = soup.find('div', {'data-section': 'study'})
            if study_section:
                case_data['study'] = study_section.get_text(strip=True)
            
            # Extract findings
            findings_section = soup.find('div', {'data-section': 'findings'})
            if findings_section:
                case_data['findings'] = findings_section.get_text(strip=True)
            
            # Extract diagnosis
            diagnosis_section = soup.find('div', {'data-section': 'diagnosis'})
            if diagnosis_section:
                case_data['diagnosis'] = diagnosis_section.get_text(strip=True)
            
            # Extract discussion
            discussion_section = soup.find('div', {'data-section': 'discussion'})
            if discussion_section:
                case_data['discussion'] = discussion_section.get_text(strip=True)
            
            # Extract image URLs
            for img in soup.find_all('img', class_='case-study-image'):
                if img.get('src'):
                    case_data['images'].append(img['src'])
            
            return case_data
            
        except requests.RequestException as e:
            print(f"Error scraping case {case_url}: {e}")
            return {}
    
    def scrape_playlist(self, output_file: str = 'cases.json', delay: float = 1.0):
        """
        Scrape all cases from the playlist
        
        Args:
            output_file: Path to save the scraped data
            delay: Delay between requests in seconds (be respectful!)
        """
        case_urls = self.get_playlist_cases()
        
        if not case_urls:
            print("No cases found in playlist")
            return
        
        all_cases = []
        
        for i, case_url in enumerate(case_urls, 1):
            print(f"\nScraping case {i}/{len(case_urls)}")
            case_data = self.scrape_case(case_url)
            
            if case_data:
                all_cases.append(case_data)
            
            # Be respectful - add delay between requests
            if i < len(case_urls):
                time.sleep(delay)
        
        # Save to JSON file
        os.makedirs('data', exist_ok=True)
        output_path = os.path.join('data', output_file)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(all_cases, f, indent=2, ensure_ascii=False)
        
        print(f"\n✓ Scraped {len(all_cases)} cases successfully")
        print(f"✓ Data saved to {output_path}")


def main():
    """Main function"""
    # Default playlist URL
    playlist_url = "https://radiopaedia.org/playlists/85715"
    
    # Allow custom playlist URL from command line
    if len(sys.argv) > 1:
        playlist_url = sys.argv[1]
    
    print("=" * 60)
    print("Radiopaedia Playlist Scraper")
    print("=" * 60)
    print(f"\nPlaylist URL: {playlist_url}")
    print("\nNote: Please be respectful of Radiopaedia's servers.")
    print("This scraper includes delays between requests.\n")
    
    scraper = RadiopaediaScraper(playlist_url)
    scraper.scrape_playlist()


if __name__ == '__main__':
    main()
