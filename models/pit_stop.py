from config.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class PitStop(Base):
    __tablename__ = 'pit_stop'
    
    stop = Column(String, nullable=True)
    lap = Column(Integer, nullable=True)
    time = Column(String, nullable=True)
    duration = Column(String, nullable=True)
    milliseconds = Column(Integer, nullable=True)
    # FK
    raceId = Column(Integer, ForeignKey("race.raceId"))
    driverId = Column(Integer, ForeignKey("driver.driverId"))
