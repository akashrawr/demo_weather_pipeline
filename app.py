import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = (
    f"postgresql://"
    f"{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}"
)

engine = create_engine(DATABASE_URL)

st.title("Fiji Weather Dashboard")

query = """
SELECT
    l.city,
    w.temperature,
    w.wind_speed,
    w.observation_time
FROM weather w
JOIN locations l
ON w.location_id = l.id
ORDER BY observation_time DESC
"""

df = pd.read_sql(query,engine)
st.subheader("Latest Weather")
st.dataframe(df)
st.subheader("Temperature Trends")
st.line_chart(
    df,
    x="observation_time",
    y="temperature"
)
st.subheader("Average Temperature by City")
city_avg = (
    df.groupby("city")
    ["temperature"]
    .mean()
)

st.bar_chart(city_avg)