from extract import get_weather
from transform import transform_weather
from load import load_weather
from locations import LOCATIONS


def main():
    print("Starting Weather ETL Pipeline...\n")

    for location in LOCATIONS:
        print(f"Fetching weather for {location['city']}...")

        raw_data = get_weather(
            location["latitude"],
            location["longitude"]
        )

        weather = transform_weather(
            raw_data,
            location["city"]
        )

        load_weather(weather)

    print("\nPipeline completed successfully!")


if __name__ == "__main__":
    main()