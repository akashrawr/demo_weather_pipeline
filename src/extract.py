import requests


def get_weather(latitude, longitude):
    """
    Fetch current weather for a given latitude and longitude.
    """

    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        "&current=temperature_2m,wind_speed_10m,weather_code"
    )

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    return response.json()