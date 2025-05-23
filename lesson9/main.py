import json
import os
import requests
from datetime import datetime, timedelta
import time

class WeatherForecast:
    def __init__(self, filename='weather_cache.json'):
        self.filename = filename
        self._data = {}
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                try:
                    self._data = json.load(f)
                except json.JSONDecodeError:
                    self._data = {}

    def __setitem__(self, key, weather):
        self._data[key] = weather
        self._save()

    def __getitem__(self, key):
        return self._data.get(key, None)

    def __iter__(self):
        return iter(self._data)

    def items(self):
        for key, weather in self._data.items():
            yield (key, weather)

    def _save(self):
        with open(self.filename, 'w') as f:
            json.dump(self._data, f, indent=2)


def get_next_day():
    return (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')


def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def get_lat_lon(city_name):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": city_name,
        "format": "jsonv2",
        "addressdetails": 1,
        "limit": 1
    }
    headers = {
        "User-Agent": "weather-app-example"
    }
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        if not data:
            print("Location not found.")
            return None, None
        lat = float(data[0]["lat"])
        lon = float(data[0]["lon"])
        return lat, lon
    except requests.HTTPError as e:
        if response.status_code == 403:
            print("Access forbidden by the geolocation service (HTTP 403). Try again later or check your network.")
        else:
            print(f"HTTP error: {e}")
        return None, None
    except Exception as e:
        print(f"Error fetching location: {e}")
        return None, None


def fetch_precipitation(latitude, longitude, date):
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}"
        f"&daily=precipitation_sum&timezone=Europe%2FLondon"
        f"&start_date={date}&end_date={date}"
    )
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        daily = data.get('daily', {})
        precipitation_list = daily.get('precipitation_sum', [])
        if precipitation_list:
            return precipitation_list[0]
        else:
            return None
    except requests.RequestException as e:
        print(f"API request error: {e}")
        return None


def main():
    weather_forecast = WeatherForecast()

    city_name = input("Enter city name: ").strip()
    if not city_name:
        print("City name cannot be empty.")
        return

    lat, lon = get_lat_lon(city_name)
    if lat is None or lon is None:
        return  # Could not get location

    user_date = input("Enter date to check weather (YYYY-mm-dd) or press Enter for tomorrow: ").strip()
    if not user_date:
        user_date = get_next_day()

    if not is_valid_date(user_date):
        print("Invalid date format. Please enter date as YYYY-mm-dd.")
        return

    key = f"{user_date}_{city_name.lower()}"
    precipitation = weather_forecast[key]

    if precipitation is None:
        print("Fetching data from API...")
        precipitation = fetch_precipitation(lat, lon, user_date)
        if precipitation is not None:
            weather_forecast[key] = precipitation
        else:
            print("Could not retrieve weather data.")
            precipitation = -1

    if precipitation is None or precipitation < 0:
        print("I don't know")
    elif precipitation > 0.0:
        print(f"It will rain. Precipitation: {precipitation} mm")
    else:
        print("It will not rain.")


if __name__ == "__main__":
    main()