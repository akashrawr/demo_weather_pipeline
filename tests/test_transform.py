from src.transform import transform_weather

def test_transform_weather():
    raw_data = {
        "latitude": -18.1416,
        "longitude": 178.4419,
        "current": {
            "temperature_2m": 25.5,
            "wind_speed_10m": 12.3,
            "weather_code": 1,
            "time": "2026-07-11T12:00"
        }
    }
    
    result = transform_weather(raw_data,"Suva")
    assert result["city"] == "Suva"
    assert result["temperature"] == 25.5
    assert result["wind_speed"] == 12.3
    assert result["weather_code"] == 1