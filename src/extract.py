import requests
from logger import logger

def get_weather(latitude, longitude):

    try:
        url = (
            "https://api.open-meteo.com/v1/forecast"
            f"?latitude={latitude}"
            f"&longitude={longitude}"
            "&current=temperature_2m,wind_speed_10m,weather_code"
        )

        logger.info(f"Requesting weather data: {latitude}, {longitude}")
        response = requests.get(url,timeout=10)
        response.raise_for_status()
        return response.json()
    
    except Exception as e:
        logger.error(f"API request failed: {e}")
        return None