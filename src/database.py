import os
import time
import psycopg2
from dotenv import load_dotenv
from logger import logger

load_dotenv()

def get_connection(retries=10,delay=5):
    attempt = 1
    while attempt <= retries:
        try:
            logger.info(f"Connecting to PostgreSQL (attempt {attempt}/{retries})")
            conn = psycopg2.connect(
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT"),
                database=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
            )
            logger.info("PostgreSQL connection successful")
            return conn

        except psycopg2.Error as e:
            logger.warning(f"Database connection failed: {e}")
            if attempt == retries:
                logger.exception("Could not connect to PostgreSQL")
                raise

            time.sleep(delay)
            attempt += 1