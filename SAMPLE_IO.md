# Sample Input & Output

## Sample CLI Input (interactive prompts)
- Destination: Jeddah
- Budget (USD): 1500
- Duration (days): 4
- Preferences: parks, libraries, hotels

## Sample Output JSON (outputs/final_plan.json)
{
  "destination": "Jeddah",
  "summary": "A 4-day personalized trip focusing on parks, libraries and central hotels.",
  "weather": {
    "description": "sunny",
    "temp": 33,
    "humidity": 40
  },
  "places": {
    "museums": [],
    "food": ["Al Baik", "Baker & Spice"],
    "culture": ["Al-Balad"]
  },
  "itinerary": {
    "Day 1": "Arrival, Corniche stroll and dinner at Baker & Spice.",
    "Day 2": "King Abdulaziz Public Library visit and Corniche sunset.",
    "Day 3": "Local markets, waterfront activities.",
    "Day 4": "Relax, hotel amenities and departure."
  },
  "budget": {
    "estimate": 1420,
    "flagged": false
  },
  "notes": "Plan fits within budget and weather is favorable for outdoor activities."
}
