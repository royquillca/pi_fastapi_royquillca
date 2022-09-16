
# External Modules
from sqlalchemy import Column, Integer, String, Date, ForeignKey
# Internal Modules
from config.db import Base


class Result(Base):
    __tablename__ = 'result'
    # PK
    resultId = Column(Integer, primary_key=True)
    #
    number = Column(String,nullable=True)
    grid = Column(String, nullable=True)	
    position = Column(String, nullable=True)
    positionText = Column(String,nullable=True)
    positionOrder = Column(String, nullable=True)
    points = Column(String, nullable=True)
    laps = Column(String, nullable=True)	
    time = Column(String, nullable=True)
    milliseconds = Column(String, nullable=True)
    fastestLap = Column(String, nullable=True)
    rank = Column(String, nullable=True)	
    fastestLapTime = Column(String, nullable=True)
    fastestLapSpeed = Column(String, nullable=True)
    statusId = Column(String, nullable=True)
    # FK
    raceId = Column(Integer, ForeignKey('race.raceId'))
    driverId = Column(Integer, ForeignKey('driver.driverId'))
    constructorId = Column(Integer, ForeignKey('constructor.constructorId'))