DROP TABLE IF EXISTS weather;

CREATE TABLE weather (
    id SERIAL PRIMARY KEY,
    latitude NUMERIC(8,5),
    longitude NUMERIC(8,5),
    temperature NUMERIC(5,2),
    wind_speed NUMERIC(5,2),
    weather_code INTEGER,
    observation_time TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);