# Project 2: Weather Data Pipeline with Python and PostgreSQL

## Overview

This project introduces aspiring data engineers to the fundamental process of building a data pipeline, focusing on three core aspects:

- **Data Collection**
- **Data Cleansing (Transformation)**
- **Data Storage**

Using **Python**, you'll fetch weather conditions and forecasts from **Open-Meteo**, a completely free weather API that requires **no API key**.

After collecting the weather data, you'll process the raw JSON by:

- Converting temperature units (if needed)
- Handling missing values
- Standardizing location names
- Cleaning and organizing the data for analysis

Finally, you'll store the transformed data in a **PostgreSQL** database.

---

## Modern Twist (Recommended)

Instead of installing PostgreSQL directly on your computer, run it inside a **Docker container**.

This approach:

- Keeps your development environment clean
- Makes your project portable
- Demonstrates Docker knowledge, which is an essential modern data engineering skill
- Mimics real-world production environments

---

# Project Workflow

```text
        Open-Meteo API
               │
               ▼
      Python (Extract)
               │
               ▼
   Clean & Transform JSON
               │
               ▼
      PostgreSQL Database
               │
               ▼
     Query & Analyze Data
```

---

# Tech Stack

- Python
- Requests
- Pandas (optional)
- PostgreSQL
- Docker
- SQL
- psycopg2 or SQLAlchemy

---

# Learning Objectives

By completing this project, you'll learn how to:

- Build a Python ETL pipeline
- Collect data from external APIs
- Clean and transform JSON data
- Work with PostgreSQL databases
- Write SQL queries
- Connect Python to PostgreSQL
- Use Docker to run database services
- Organize a real-world data engineering project

---

# Resources

## Documentation

### Open-Meteo Documentation

The official documentation includes a URL builder that lets you preview the API response before writing any code.

---

## GitHub Repositories

### Weather and Air Quality ETL Pipeline

Demonstrates an ETL pipeline that:

- Extracts weather and air quality data from public APIs
- Transforms it into a clean, analyzable format
- Loads it into PostgreSQL

### Weather Data Integration Project

An end-to-end weather ETL pipeline that:

- Extracts weather data
- Cleans and transforms the data
- Loads it into PostgreSQL

---

## Courses

### Creating PostgreSQL Databases

A comprehensive PostgreSQL course covering:

- Database creation
- Tables
- Constraints
- Indexes
- SQL
- Database optimization

### Data Engineer in Python

Covers foundational data engineering topics, including:

- Data collection
- Data transformation
- ETL pipelines
- Data storage
- Python best practices

---

# Skills Developed

After completing this project, you'll gain experience with:

- Writing data pipeline applications in Python
- Collecting data from REST APIs
- Cleaning and transforming JSON data
- Running PostgreSQL inside Docker
- Creating and managing PostgreSQL databases
- Writing SQL queries
- Loading data into relational databases
- Building an end-to-end ETL workflow