from datetime import datetime
from src.database import get_session
from src.models import Weather, Location
from src.logger import logger

def load_weather(weather_data):
    session = None
    try:
        session = get_session()
        location = (
            session.query(Location)
            .filter_by(
                city=weather_data["city"]
            )
            .first()
        )

        if not location:
            location = Location(
                city=weather_data["city"],
                latitude=weather_data["latitude"],
                longitude=weather_data["longitude"]
            )
            session.add(location)
            session.flush()

        weather = Weather(
            location_id=location.id,
            temperature=weather_data["temperature"],
            wind_speed=weather_data["wind_speed"],
            weather_code=weather_data["weather_code"],
            observation_time=datetime.fromisoformat(
                weather_data["observation_time"]
            )
        )
        session.add(weather)
        session.commit()
        logger.info(f"Inserted weather for {location.city}")

    except Exception:
        logger.exception("Failed loading weather data")
        if session:
            session.rollback()
    finally:
        if session:
            session.close()