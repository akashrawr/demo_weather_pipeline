from datetime import datetime
from sqlalchemy import Column,Integer,String,Numeric,Float,DateTime,ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base

class Location(Base):
    __tablename__ = "locations"
    id = Column(Integer, primary_key=True)
    city = Column(String,unique=True,nullable=False)
    latitude = Column(Float,nullable=False)
    longitude = Column(Float,nullable=False)
    weather = relationship("Weather",back_populates="location")

class Weather(Base):
    __tablename__ = "weather"
    id = Column(Integer,primary_key=True)
    location_id = Column(Integer,ForeignKey("locations.id"),nullable=False)
    temperature = Column(Numeric)
    wind_speed = Column(Numeric)
    weather_code = Column(Integer)
    observation_time = Column(DateTime)
    created_at = Column(DateTime,default=datetime.utcnow)
    location = relationship("Location",back_populates="weather")