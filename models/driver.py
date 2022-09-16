# External Modules
from sqlalchemy import Column, Integer, String, Date
# Internal Modules
from config.db import Base

class Driver(Base):
    __tablename__ = 'driver'

    driverId = Column(Integer, primary_key=True)
    driverRef = Column(String, nullable=True)
    number = Column(String, nullable=True)
    name = Column(String, nullable=True)
    apellido = Column(String, nullable=True)
    fecha_nacimiento = Column(Date, nullable=True)
    nacionalidad = Column(String, nullable=True)