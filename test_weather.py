# test_weather.py
import json
from tools.weather_tool import get_weather

def main():
    print("🌦️ Testing Live Weather Fetch...\n")

    # Ask user for a city
    city = input("Enter a city name to check weather (e.g. Jeddah): ").strip() or "Jeddah"

    # Call the weather function
    data = get_weather(city)

    # Display results nicely
    print("\n=== Live Weather Data ===")
    print(json.dumps(data, indent=2, ensure_ascii=False))

    # Quick feedback
    if "error" in data:
        print("\n⚠️ Something went wrong. Please check:")
        print("1️⃣ Your OPENWEATHER_API_KEY in .env or config.settings")
        print("2️⃣ Internet connection")
        print("3️⃣ Correct city name")
    else:
        print("\n✅ Weather data fetched successfully!")

if __name__ == "__main__":
    main()
