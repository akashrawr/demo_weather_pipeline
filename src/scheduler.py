from apscheduler.schedulers.blocking import BlockingScheduler
from src.main import main
from src.logger import logger

scheduler = BlockingScheduler()

@scheduler.scheduled_job("interval",hours=24,id="weather_pipeline_job")
def run_pipeline():
    logger.info("Scheduled pipeline started")
    try:
        main()
        logger.info("Scheduled pipeline completed successfully")

    except Exception:
        logger.exception("Scheduled pipeline failed")

if __name__ == "__main__":
    logger.info("Weather scheduler started")
    scheduler.start()