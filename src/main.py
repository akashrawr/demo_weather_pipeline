from extract import get_weather
from transform import transform_weather
from load import load_weather
from locations import LOCATIONS
from logger import logger

def main():
    logger.info("Starting Weather ETL Pipeline")

    for location in LOCATIONS:
        city = location["city"]

        try:
            logger.info(f"Processing {city}")

            raw_data = get_weather(
                location["latitude"],
                location["longitude"]
            )

            if raw_data is None:
                continue

            weather = transform_weather(raw_data, city)
            load_weather(weather)

        except Exception as e:
            logger.error(f"Pipeline failed for {city}: {e}")

    logger.info(f"Pipeline completed")

if __name__ == "__main__":
    main()