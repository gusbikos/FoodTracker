
"""
Keeps all your configuration (API keys, URLs, tokens) in one place.
Purpose:
Central configuration file.

Responsibilities:
- Load environment variables from .env
- Store API keys
- Store database URLs
- Store environment settings (dev / prod)

Examples of things stored here:
- Nutrition API key
- Database connection string
- Secret keys
“All sensitive or environment-based settings live here.”
"""
import os
from dotenv import load_dotenv

load_dotenv()

FOOD_FACTS_API_KEY = os.getenv("FOOD_FACTS_API_KEY")