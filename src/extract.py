import requests
from tenacity import retry, stop_after_attempt, wait_fixed
from src.logger import logger

@retry(
    stop=stop_after_attempt(3),
    wait=wait_fixed(5)
)
def get_weather(latitude, longitude):
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        "&current=temperature_2m,wind_speed_10m,weather_code"
    )

    logger.info(f"Requesting weather data: {latitude}, {longitude}")
    response = requests.get(url,timeout=30)
    response.raise_for_status()
    return response.json()