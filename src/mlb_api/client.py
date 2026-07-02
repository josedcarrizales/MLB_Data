import requests
from mlb_api.config import API_KEY

HEADERS = {"accept": "application/json", "x-api-key": API_KEY}

def get_json(url: str, timeout: int = 5) -> dict | None:
    """Make a GET request to a Sportradar endpoint and return parsed JSON."""
    try:
        response = requests.get(url, headers=HEADERS, timeout=timeout)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.Timeout as err:
        print(f"Timeout Error: {err}")
    except requests.exceptions.ConnectionError as err:
        print(f"Connection Error: {err}")
    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error: {err}")
        print(f"Server response body: {response.text}")
    except requests.exceptions.RequestException as err:
        print(f"General Requests Error: {err}")
    except ValueError:
        print("Error: Response was not valid JSON.")

    return None