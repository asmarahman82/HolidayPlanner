# test_groq.py
import logging
from tools.groq_tool import GroqTool

logging.basicConfig(level=logging.DEBUG)

def main():
    prompt = "Create a 1-day itinerary for Jeddah including parks, libraries, and hotels."

    # Initialize GroqTool
    groq = GroqTool()
    groq.model = "openai/gpt-oss-120b"  # Set your actual model

    # Generate text
    result = groq.generate_text(prompt)

    print("=== Groq API Test Result ===")
    print(result)

if __name__ == "__main__":
    main()

