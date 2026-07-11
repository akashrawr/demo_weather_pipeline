# Weather Data Pipeline

An end-to-end weather data engineering project that extracts weather data, transforms and validates it, loads it into PostgreSQL, and provides an interactive analytics dashboard.

The project demonstrates a production-style data pipeline using Python, PostgreSQL, SQLAlchemy, Alembic, Docker, GitHub Actions, and Streamlit.

---

# Project Architecture

```
                    Weather API
                        |
                        |
                 Extract Layer
              (Python Requests)
                        |
                        |
                Transform Layer
        (Cleaning, Validation, Quality Checks)
                        |
                        |
                  Load Layer
             (SQLAlchemy ORM)
                        |
                        |
              PostgreSQL Database
                        |
                        |
              Streamlit Dashboard

```

---

# Features

## ETL Pipeline

* Extracts weather information from external APIs
* Supports multiple locations
* Transforms raw API responses into structured datasets
* Loads processed data into PostgreSQL
* Uses SQLAlchemy ORM for database operations
* Uses Alembic for database migrations

## Data Quality Checks

Implemented validation checks:

* Missing value validation
* Data type validation
* Temperature range validation
* Wind speed validation
* Schema validation
* Database connectivity validation

---

# Technology Stack

| Category             | Technology     |
| -------------------- | -------------- |
| Programming Language | Python 3.12    |
| Database             | PostgreSQL 16  |
| ORM                  | SQLAlchemy     |
| Migration Tool       | Alembic        |
| Dashboard Framework  | Streamlit      |
| Visualization        | Plotly Express |
| Data Processing      | Pandas         |
| Testing              | Pytest         |
| Containerization     | Docker         |
| CI/CD                | GitHub Actions |

---

# Local Setup

## Clone Repository

```bash
git clone <repository-url>

cd Weather_data_pipeline
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Activate environment:

Windows:

```bash
.venv\Scripts\activate
```

Linux/Mac:

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Database Setup

Configure database connection:

```
DATABASE_URL=postgresql://username:password@localhost:5432/weather_db
```

Run migrations:

```bash
alembic upgrade head
```

---

# Running the Pipeline

Start the ETL pipeline:

```bash
python -m src.main
```
---

# Running the Dashboard

Install dashboard dependencies:

```bash
pip install streamlit plotly pandas
```

Start Streamlit:

```bash
streamlit run app.py
```

Dashboard available at:

```
http://localhost:8501
```

---

# Docker Deployment

Build and start containers:

```bash
docker compose up --build
```

Services:

```
weather-postgres
weather-etl
```

View logs:

```bash
docker compose logs -f
```

Stop services:

```bash
docker compose down
```

---

# Testing

Run all tests:

```bash
pytest -v
```

---

# Database Schema

## locations table

| Column    | Type    |
| --------- | ------- |
| id        | Integer |
| city      | String  |
| latitude  | Float   |
| longitude | Float   |

## weather table

| Column           | Type        |
| ---------------- | ----------- |
| id               | Integer     |
| location_id      | Foreign Key |
| temperature      | Float       |
| wind_speed       | Float       |
| weather_code     | Integer     |
| observation_time | Timestamp   |
| created_at       | Timestamp   |

---

# Future Improvements

* Add Apache Airflow orchestration
* Add cloud deployment
* Add data warehouse layer
* Add automated monitoring
* Add weather forecasting model
* Add Grafana dashboards
* Add CI/CD deployment pipeline
