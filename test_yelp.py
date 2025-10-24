# test_yelp.py
import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

YELP_API_KEY = os.getenv("YELP_API_KEY")

def search_places(location="Jeddah", term="restaurant", limit=5):
    if not YELP_API_KEY:
        return {"error": "Missing YELP_API_KEY"}

    url = "https://api.yelp.com/v3/businesses/search"
    headers = {"Authorization": f"Bearer {YELP_API_KEY}"}
    params = {"location": location, "term": term, "limit": limit}

    try:
        r = requests.get(url, headers=headers, params=params, timeout=10)
        r.raise_for_status()
        data = r.json()
        return data.get("businesses", [])
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    print("🍽️ Testing Yelp API...\n")
    location = input("Enter city (e.g. Jeddah): ").strip() or "Jeddah"
    term = input("Enter search term (e.g. parks, cafes): ").strip() or "restaurants"

    results = search_places(location, term)
    print("\n=== Yelp API Results ===")
    print(json.dumps(results[:3], indent=2, ensure_ascii=False))

