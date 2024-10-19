import requests
from datetime import datetime
from typing import Dict

def get_aprs_data(callsign: str, apikey: str) -> Dict[str, str]:
    """
    Fetches APRS data for a given callsign from the API.

    Args:
        callsign (str): The callsign to query.
        apikey (str): The API key for authentication.

    Returns:
        Dict[str, str]: A dictionary with the fetched APRS data.
    """
    url = f'https://api.aprs.fi/api/get?name={callsign}&what=loc&apikey={apikey}&format=json'
    
    response = requests.get(url=url)
    response.raise_for_status()  # Ensure HTTP errors are raised if present
    data = response.json()['entries'][0]
    
    # Return the relevant data in a dictionary
    return {
        'name': data['name'],
        'lat': str(data['lat']),
        'long': str(data['lng']),
        'comment': data.get('comment', 'No comment'),
        'path': data['path'],
        'start_time': datetime.fromtimestamp(int(data['time'])).strftime('%Y-%m-%d %H:%M:%S'),
        'end_time': datetime.fromtimestamp(int(data['lasttime'])).strftime('%Y-%m-%d %H:%M:%S')
    }

def format_aprs_data(data: Dict[str, str]) -> str:
    """
    Formats the APRS data into a readable string.

    Args:
        data (Dict[str, str]): The APRS data to format.

    Returns:
        str: The formatted string with all data.
    """
    return (f"Name: {data['name']}\n"
            f"Lat/Long: {data['lat']}, {data['long']}\n"
            f"Comment: {data['comment']}\n"
            f"Path: {data['path']}\n"
            f"Start Time: {data['start_time']}\n"
            f"End Time: {data['end_time']}")


# Parameters
callsign = 'YC0DMS'
apikey = 'yourAPIkey'

# Get and print the formatted data
try:
    aprs_data = get_aprs_data(callsign, apikey)
    formatted_data = format_aprs_data(aprs_data)
    print(formatted_data)
except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
