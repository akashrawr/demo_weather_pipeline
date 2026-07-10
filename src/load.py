from database import get_connection
import psycopg2
from logger import logger

def load_weather(weather):
    conn = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
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
        VALUES (%s, %s, %s, %s, %s, %s, %s);
        """

        cursor.execute(
            query,
            (
                weather["city"],
                weather["latitude"],
                weather["longitude"],
                weather["temperature"],
                weather["wind_speed"],
                weather["weather_code"],
                weather["observation_time"],
            ),
        )

        conn.commit()
        logger.info(f"Inserted weather data for {weather['city']}")

    except Exception as e:
        logger.error(f"Database insert failed: {e}")

    finally:
        if conn:
            cursor.close()
            conn.close()