import requests
import pandas as pd

import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.environ["SPORTRADAR_API_KEY"]
url = "https://api.sportradar.com/mlb/trial/v8/en/league/awards/list.json"

headers = {
    "accept": "application/json",
    "x-api-key": API_KEY
    }

import requests

try:
    # Make API call
    response = requests.get(url, headers=headers,timeout=5)
    
    # Raise error faster when it is 4xx or 5xx
    response.raise_for_status()
    
    # Successful response
    data = response.json()
    print("Success:", response.status_code)

# Catch timeout
except requests.exceptions.Timeout as err_timeout:
    print(f"Timeout Error: {err_timeout}")

# Catch connection error
except requests.exceptions.ConnectionError as err_conn:
    print(f"Connection Error: {err_conn}")

# Catch HTTP error
except requests.exceptions.HTTPError as err_http:
    print(f"HTTP Error: {err_http}")
    print(f"Server response body: {response.text}")

# Catch general error not fitting the above requirements
except requests.exceptions.RequestException as err_generic:
    print(f"General Requests Error: {err_generic}")
    
# Catch bad JSON response
except ValueError:
    print("Error: Response was not valid JSON.")

# Extract the first object and wrap it in a list to form a row
if data:
    # Optional: look at the shape before you commit to a parsing plan
    def explore(obj, prefix=""):
        if isinstance(obj, dict):
            for k, v in obj.items():
                print(f"{prefix}{k}: {type(v).__name__}")
                explore(v, prefix + "  ")
        elif isinstance(obj, list) and obj:
            print(f"{prefix}[list of {len(obj)}]")
            explore(obj[0], prefix + "  ")

    explore(data)

    awards_df = pd.json_normalize(data.get("awards", []))
    print(awards_df)