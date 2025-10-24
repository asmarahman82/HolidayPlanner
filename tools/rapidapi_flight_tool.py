# tools/rapidapi_flight_tool.py
import os, requests, logging
from config.settings import RAPIDAPI_KEY

def get_flight_info(origin: str, destination: str):
    if not RAPIDAPI_KEY:
        logging.warning("No RapidAPI key set")
        return {"error": "No API key"}
    try:
        url = "https://flight-fare-search.p.rapidapi.com/v2/flights/"
        headers = {
            "X-RapidAPI-Key": RAPIDAPI_KEY,
            "X-RapidAPI-Host": "flight-fare-search.p.rapidapi.com"
        }
        params = {"from": origin, "to": destination, "currency": "USD"}
        r = requests.get(url, headers=headers, params=params, timeout=10)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        logging.error(f"rapidapi_flight_tool: error fetching flights: {e}")
        return {"error": str(e)}
