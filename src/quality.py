from src.logger import logger

def validate_weather(data):
    checks = [
        validate_city(data),
        validate_temperature(data),
        validate_coordinates(data),
        validate_observation_time(data)
    ]
    if all(checks):
        logger.info(f"Data quality passed for {data['city']}")
        return True

    logger.error(f"Data quality failed for {data['city']}")
    return False

def validate_city(data):
    return (
        data.get("city") is not None
        and len(data["city"]) > 0
    )

def validate_temperature(data):
    temperature = data.get("temperature")
    return (
        temperature is not None
        and -50 <= temperature <= 60
    )

def validate_coordinates(data):
    lat = data.get("latitude")
    lon = data.get("longitude")
    return (
        -90 <= lat <= 90
        and -180 <= lon <= 180
    )

def validate_observation_time(data):
    return (
        data.get("observation_time")
        is not None
    )