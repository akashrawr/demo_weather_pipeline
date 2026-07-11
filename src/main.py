from src.extract import get_weather
from src.transform import transform_weather
from src.load import load_weather
from src.locations import LOCATIONS
from src.logger import logger
from src.quality import validate_weather

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
                logger.warning(f"Skipping {city} because no weather data was received")
                continue

            weather = transform_weather(raw_data, city)

            if validate_weather(weather):
                load_weather(weather)
            else:
                logger.warning("Skipping invalid weather record")

        except Exception:
            logger.exception(f"Pipeline failed for {city}")

    logger.info(f"Pipeline completed")

if __name__ == "__main__":
    main()