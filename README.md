# Top 10 Restaurants Scraper

## 🔍 Description
The user to enter a city name and retrieves the top 10 restaurants in that city using SerpAPI (Google Search API). It extracts relevant information such as description and link and saves it to a JSON file.

## ✅ Features
- Takes a city name as input
- Fetches top 10 restaurants via Google search
- Stores data in `restaurants.json` using JSON format

## ⚙️ Dependencies
- Python 3.x
- `requests`

## 🔐 API Key Setup
1. Sign up at [serpapi.com](https://serpapi.com/)
2. Copy your API Key
3. Replace `YOUR_SERPAPI_KEY` in `main.py` with your key

## 🧠 Challenges
- Google doesn't allow scraping directly, hence used SerpAPI.
- Free API tier is limited to 100 searches/month.
