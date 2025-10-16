
import os
from pathlib import Path
from dotenv import load_dotenv

# Try to load .env if present (optional). If python-dotenv is not installed
# this file still works if environment variables are set externally.
try:
    load_dotenv()
except Exception:
    pass

BASE_DIR = Path(__file__).resolve().parents[2]

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
