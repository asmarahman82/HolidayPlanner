# test_huggingface.py
import json
import logging
from tools.huggingface_tool import HuggingFaceTool

logging.basicConfig(level=logging.INFO)

def main():
    print("🤖 Hugging Face Summarization Test\n")
    
    # Initialize the HuggingFaceTool with your API key and endpoint
    hf_tool = HuggingFaceTool()
    
    while True:
        prompt = input("Enter text to summarize (or type 'exit' to quit): ").strip()
        if prompt.lower() == "exit":
            print("Exiting test...")
            break
        
        # Call the summarize method
        summary = hf_tool.summarize(prompt)
        
        print("\n=== Summary Result ===")
        print(summary)
        print("-" * 50)

if __name__ == "__main__":
    main()

