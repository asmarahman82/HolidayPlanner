# agents/itinerary_agent.py
import logging
from tools.groq_tool import GroqTool
from config.constants import MAX_ITINERARY_DAYS

class ItineraryAgent:
    def __init__(self):
        self.groq = GroqTool()

    def run(self, data: dict):
        logging.info("ItineraryAgent: generating itinerary")
        city = data.get("city")
        duration = min(int(data.get("duration", 3)), MAX_ITINERARY_DAYS)
        preferences = ", ".join(data.get("preferences", []))
        weather_desc = data.get("weather", {}).get("description", "pleasant weather")
        places = data.get("destination_info", {}).get("places", {})

        # Compose a compact prompt for Groq
        prompt = (
            f"Create a {duration}-day trip plan for {city}. "
            f"Traveler likes: {preferences}. "
            f"Weather: {weather_desc}. "
            f"Use these sample places: {places}. "
            f"Return a short JSON with keys: day, main_activity, note."
        )

        itinerary_text = self.groq.generate_text(prompt)
        data["itinerary_text"] = itinerary_text
        logging.info("ItineraryAgent: generated itinerary text")
        return data
