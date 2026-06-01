import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Configure Gemini with your API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# List all available models and their supported methods
models = genai.list_models()

# Print model names and their capabilities
for model in models:
    print(f"Model: {model.name}")
    print(f"Supported Generation Methods: {model.supported_generation_methods}\n")
