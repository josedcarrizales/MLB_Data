import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("SPORTRADAR_API_KEY")
BASE_URL = "https://api.sportradar.com/mlb/trial/v8/en"

if not API_KEY:
    raise ValueError("SPORTRADAR_API_KEY not found, please check your API Key")