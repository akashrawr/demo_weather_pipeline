from unittest.mock import patch
from src.extract import get_weather

@patch("src.extract.requests.get")
def test_get_weather(mock_get):
    mock_response = {
        "latitude": -18.1416,
        "longitude": 178.4419,
        "current": {
            "temperature_2m": 25
        }
    }

    mock_get.return_value.json.return_value = mock_response
    mock_get.return_value.raise_for_status.return_value = None

    result = get_weather(
        -18.1416,
        178.4419
    )

    assert result["latitude"] == -18.1416
    assert result["current"]["temperature_2m"] == 25