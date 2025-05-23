import requests
import datetime
import json
import os

def geocode_location(location):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": location,
        "format": "json",
        "limit": 1
    }
    headers = {
        "User-Agent": "weather-checker-script/1.0 (alerts.utkarbha@gmail.com)"
    }
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200 and response.json():
        lat = response.json()[0]["lat"]
        lon = response.json()[0]["lon"]
        return float(lat), float(lon)
    else:
        return None, None

def get_precipitation(date, latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=precipitation_sum&timezone=Europe/London&start_date={date}&end_date={date}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        try:
            return data['daily']['precipitation_sum'][0]
        except (KeyError, IndexError):
            return None
    return None

def main():
    location = input("Enter the location (e.g., city name): ")
    lat, lon = geocode_location(location)
    if lat is None:
        print("Location not found.")
        return

    date_input = input("Enter the date (YYYY-MM-DD) or press Enter for tomorrow: ")
    if not date_input:
        date = (datetime.date.today() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    else:
        try:
            date = datetime.datetime.strptime(date_input, '%Y-%m-%d').date().strftime('%Y-%m-%d')
        except ValueError:
            print("Invalid date format.")
            return

    cache_file = 'weather_cache.json'
    if os.path.exists(cache_file):
        with open(cache_file, 'r') as f:
            cache = json.load(f)
    else:
        cache = {}

    if date in cache and location in cache[date]:
        precipitation = cache[date][location]
        print(f"Cached data: {precipitation} mm of precipitation on {date} in {location}.")
        return

    precipitation = get_precipitation(date, lat, lon)
    if precipitation is None:
        print("Unable to retrieve precipitation data.")
    else:
        print(f"Forecast: {precipitation} mm of precipitation on {date} in {location}.")
        cache.setdefault(date, {})[location] = precipitation
        with open(cache_file, 'w') as f:
            json.dump(cache, f)

if __name__ == "__main__":
    main()