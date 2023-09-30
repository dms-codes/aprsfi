# APRS Location Data Fetcher

This Python script allows you to fetch and display the location data of an APRS (Automatic Packet Reporting System) station using the [APRS.fi](https://aprs.fi/) API. It retrieves information such as callsign, latitude, longitude, comment, path, and timestamps.

## Prerequisites

Before you begin, make sure you have the following:

- Python installed on your system.
- An APRS.fi API key. You can obtain it by signing up on the [APRS.fi API page](https://aprs.fi/page/api).

## Usage

1. Clone this repository or download the script.

2. Open the script and replace `'yourAPIkey'` with your actual APRS.fi API key.

3. Modify the `callsign` and `loc` variables to specify the callsign of the APRS station and the location (grid square) you want to query.

4. Run the script using the following command:

   ```bash
   python aprs_location_fetcher.py
   ```

The script will make an API request to APRS.fi and display the following information:

- **Name**: The station's name.
- **Lat/Long**: Latitude and longitude coordinates.
- **Comment**: A comment associated with the station.
- **Path**: The path the packet took.
- **Start Time**: The timestamp when the data was first received.
- **End Time**: The timestamp when the data was last received.

## Example

Here's an example of what the script's output might look like:

```plaintext
Name : John's Station
Lat/Long : 47.12345,-122.54321
Comment : Testing APRS
Path : WIDE1-1,WIDE2-2
Start Time : 2023-09-30 14:30:00
End Time : 2023-09-30 14:45:00
```

## Note

- Make sure to keep your API key secure and do not share it publicly.
- The script assumes you have internet access to make API requests.

Feel free to explore and customize the script according to your needs.
