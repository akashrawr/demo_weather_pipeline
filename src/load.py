from database import get_connection
import psycopg2


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

        print("Weather inserted successfully!")

    except psycopg2.Error as e:
        print(f"Database Error: {e}")

    finally:
        if conn:
            cursor.close()
            conn.close()