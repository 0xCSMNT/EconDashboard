import os
from dotenv import load_dotenv
import requests
import json
import time

# Load environment variables from .env file
load_dotenv()

# API key and base URL
api_key = os.getenv("FRED_API_KEY")
base_url = "https://api.stlouisfed.org/fred/series/observations"

# Define the list of data sources
data_sources = [
    {'name': 'GDP', 'code': 'GDP', 'frequency': 'Quarterly'},
    {'name': 'Federal Total Debt', 'code': 'GFDEBTN', 'frequency': 'Quarterly'},
    {'name': 'Federal Debt to GDP', 'code': 'GFDEGDQ188S', 'frequency': 'Quarterly'},
    {'name': 'Household Debt to GDP', 'code': 'HDTGPDUSQ163N', 'frequency': 'Quarterly'},
    {'name': 'Unemployment', 'code': 'UNRATE', 'frequency': 'Monthly'},
    {'name': 'CPI', 'code': 'CORESTICKM159SFRBATL', 'frequency': 'Monthly'},
    {'name': 'Industrial Production', 'code': 'INDPRO', 'frequency': 'Monthly'},
    {'name': 'Housing Starts', 'code': 'HOUST', 'frequency': 'Monthly'},
    {'name': 'Money Supply (M2)', 'code': 'M2SL', 'frequency': 'Monthly'},
    {'name': 'Fed Funds Rate', 'code': 'DFF', 'frequency': 'Daily'},
    {'name': 'SP500', 'code': 'SP500', 'frequency': 'Daily'},
    {'name': 'NASDAQ 100', 'code': 'NASDAQ100', 'frequency': 'Daily'}
]

# Filter out unwanted keys from the observations
def filter_observation(obs):
    return {
        'x': obs['date'],
        'y': obs['value']
    }

# ... [rest of the imports and setup]
def fetch_data_and_write_to_file():
    fred_data = {}
    count = 0

    for source in data_sources:
        params = {
            "api_key": api_key,
            "file_type": "json",
            "series_id": source['code'],
            "observation_start": "1970-01-01",
            "sort_order": "desc"
        }
        
        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            
            print(f"Successfully fetched data for {source['name']} ({source['code']})")
            data = response.json()
            
            # Filter out unwanted keys
            filtered_observations = [filter_observation(obs) for obs in data['observations']]

            fred_data[source['code']] = filtered_observations
            count += len(filtered_observations)
            
            fred_data[source['code']] = filtered_observations

        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch data for {source['name']} ({source['code']})")
            print(f"Exception: {e}")

        time.sleep(0.25)  # To avoid hitting rate limit; adjust as needed

    print(f"Total data points fetched: {count}")

    with open("fred_data.json", "w") as f:
        json.dump(fred_data, f, indent=4)

if __name__ == "__main__":
    fetch_data_and_write_to_file()
