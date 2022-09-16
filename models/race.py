# External Modules
from sqlalchemy import Column, Integer, String, Date, ForeignKey
# Internal Modules
from config.db import Base


class Race(Base):
    __tablename__ = 'race'
    #
    raceId = Column(Integer, primary_key=True)
    year = Column(String, nullable=True)
    name = Column(String, nullable=True)
    circuitId = Column(Integer, nullable=True)
    round = Column(Integer, nullable=True)
    time = Column(String, nullable=True)
    date = Column(Date, nullable=True)
    url = Column(String, nullable=True)
    #
    circuitId = Column(Integer, ForeignKey("circuit.circuitId"))