import json
import logging
from tools.groq_tool import GroqTool
from tools.weather_tool import get_weather  # ✅ import live weather function
from config.settings import DEFAULT_CITY, DEFAULT_BUDGET, DEFAULT_DURATION, DEFAULT_PREFERENCES

logging.basicConfig(level=logging.INFO)

def get_user_input(prompt, default):
    user_input = input(f"{prompt} (default: {default}): ").strip()
    return user_input if user_input else default

def main():
    print("✈️ Welcome to HolidayPlanner! Let's plan your trip)")

    city = get_user_input("Destination city", DEFAULT_CITY)
    budget = get_user_input("Budget in USD", DEFAULT_BUDGET)
    duration = get_user_input("Duration in days", DEFAULT_DURATION)
    preferences = get_user_input(
        "Preferences, comma-separated", ",".join(DEFAULT_PREFERENCES)
    ).split(",")

    # Initialize GroqTool with supported model
    groq = GroqTool()

    # ✅ Fetch live weather
    weather_data = get_weather(city)

    # Create a prompt for the itinerary
    prompt = (
        f"Create a {duration}-day itinerary for {city} including "
        f"{', '.join(preferences)}. Provide times, activities, and tips."
    )

    itinerary = groq.generate_text(prompt)

    holiday_plan = {
        "destination": city,
        "summary": f"A personalized trip plan for {city} including {', '.join(preferences)}.",
        "weather": weather_data,  # ✅ live weather data injected here
        "places": {
            "museums": [],
            "food": [],
            "culture": []
        },
        "itinerary": itinerary,
        "budget": {
            "estimate": budget,
            "flagged": False
        }
    }

    print("\n=== Final Holiday Plan ===")
    print(json.dumps(holiday_plan, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
