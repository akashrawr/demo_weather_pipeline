from unittest.mock import patch, MagicMock
from src.load import load_weather

def test_load_weather():
    weather = {
        "city": "Suva",
        "temperature": 25,
        "wind_speed": 10,
        "weather_code": 1,
        "observation_time": "2026-07-11T12:00"
    }
    with patch("src.load.get_session") as mock_session:
        session = mock_session.return_value
        mock_location = MagicMock()
        mock_location.id = 1
        mock_location.city = "Suva"
        session.query.return_value.filter_by.return_value.first.return_value = (mock_location)
        load_weather(weather)
        session.add.assert_called_once()
        session.commit.assert_called_once()