import pandas as pd
from mlb_api.client import get_json
from mlb_api.config import BASE_URL

def fetch_awards() -> pd.DataFrame:
    """Fetch the league awards list and return it as a flat DataFrame."""
    url = f"{BASE_URL}/league/awards/list.json"
    data = get_json(url)

    if data is None:
        return pd.DataFrame()  # empty DataFrame instead of crashing downstream code

    return pd.json_normalize(data.get("awards", []))