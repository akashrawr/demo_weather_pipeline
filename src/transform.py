def transform_weather(data, city):
    """
    Transform raw weather JSON into a clean dictionary.
    """
    current = data["current"]
    return {
        "city": city,
        "latitude": data["latitude"],
        "longitude": data["longitude"],
        "temperature": current["temperature_2m"],
        "wind_speed": current["wind_speed_10m"],
        "weather_code": current["weather_code"],
        "observation_time": current["time"],
    }