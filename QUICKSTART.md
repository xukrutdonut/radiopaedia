# ⚡ Quick Start Guide

## Installation (2 minutes)

```bash
# Clone the repo
git clone https://github.com/xukrutdonut/radiopaedia.git
cd radiopaedia

# Install dependencies
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

### 1️⃣ Scrape Cases (5-10 minutes)

```bash
# Use default playlist (85715)
python scraper.py

# Or use your own playlist
python scraper.py https://radiopaedia.org/playlists/YOUR_ID
```

### 2️⃣ View Cases (instant)

```bash
python webapp.py
# Open http://localhost:5000
```

## Alternative: Use Quick Start Scripts

### Linux/Mac
```bash
./run.sh
```

### Windows
```bash
run.bat
```

## What You Get

✅ **Scraper** that extracts cases from your Radiopaedia playlist  
✅ **Web interface** to browse and study cases  
✅ **API** for programmatic access  
✅ **Offline access** to your selected cases  

## File Structure

```
radiopaedia/
├── scraper.py          # Extract cases
├── webapp.py           # Web interface
├── templates/          # HTML templates
├── data/cases.json     # Your scraped cases
└── README.md           # Full documentation
```

## Common Commands

```bash
# Start scraper with custom playlist
python scraper.py https://radiopaedia.org/playlists/85715

# Start web app on different port
# Edit webapp.py: app.run(port=8080)
python webapp.py

# Access API
curl http://localhost:5000/api/cases
```

## Need Help?

- 📖 [Full Documentation](README.md)
- 📚 [Complete Usage Guide](GUIA_USO.md)
- 🐛 [Report Issues](https://github.com/xukrutdonut/radiopaedia/issues)

## Important Notes

⚠️ **Educational use only**  
⚠️ **Credit Radiopaedia.org**  
⚠️ **Be respectful to servers** (built-in delays)  

---

Made with ❤️ for pediatric radiology education
