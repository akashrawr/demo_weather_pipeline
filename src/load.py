from sqlalchemy import text
from src.database import get_session
from src.logger import logger

def load_weather(weather):
    session = None
    try:
        session = get_session()
        query = text("""
        INSERT INTO weather
        (
            city,
            latitude,
            longitude,
            temperature,
            wind_speed,
            weather_code,
            observation_time
        )

        VALUES
        (
            :city,
            :latitude,
            :longitude,
            :temperature,
            :wind_speed,
            :weather_code,
            :observation_time
        )
        """)

        session.execute(query, weather)
        session.commit()
        logger.info(f"Inserted weather data for {weather['city']}")

    except Exception:
        logger.exception("Database insert failed")
        if session:
            session.rollback()

    finally:
        if session:
            session.close()