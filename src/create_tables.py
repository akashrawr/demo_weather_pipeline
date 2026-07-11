from src.database import engine, Base
from src.models import Location,Weather

def create_tables():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_tables()