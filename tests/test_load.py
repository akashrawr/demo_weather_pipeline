from unittest.mock import patch
from src.load import load_weather

def test_load_weather():
    weather = {
        "city": "Suva",
        "latitude": -18.1416,
        "longitude": 178.4419,
        "temperature": 25,
        "wind_speed": 10,
        "weather_code": 1,
        "observation_time": "2026-07-11T12:00"
    }

    with patch("src.load.get_session") as mock_session:
        session = mock_session.return_value
        load_weather(weather)
        session.execute.assert_called_once()
        session.commit.assert_called_once()