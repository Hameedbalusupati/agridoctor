import os
import requests


def get_weather_current(lat, lon):
    api_key = os.getenv("WEATHER_API_KEY", "")
    if not api_key or api_key == "demo-weather-key":
        return {"available": False, "message": "Weather API is not configured."}
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    return {
        "temperature": data.get("main", {}).get("temp", 0),
        "humidity": data.get("main", {}).get("humidity", 0),
        "rainfall": data.get("rain", {}).get("1h", 0),
        "wind_speed": data.get("wind", {}).get("speed", 0),
        "condition": data.get("weather", [{}])[0].get("main", "Unknown"),
        "location": data.get("name", "Farm"),
        "forecast": "Current conditions fetched from weather service.",
        "source": "openweathermap"
    }


def get_weather_forecast(lat, lon):
    api_key = os.getenv("WEATHER_API_KEY", "")
    if not api_key or api_key == "demo-weather-key":
        return {"available": False, "message": "Weather API is not configured.", "forecast": []}

    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    return {"available": True, "location": data.get("city", {}).get("name", "Farm"), "forecast": data.get("list", [])}
