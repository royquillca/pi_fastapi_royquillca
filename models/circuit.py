# External Modules
from sqlalchemy import Column, Integer, String
# Internal Modules
from config.db import Base

class Circuit(Base):
    __tablename__ = 'circuit'
    id_circuito = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=True)
    Ciudad = Column(String, nullable=True)
    Pais = Column(String, nullable=True)
    latitud = Column(String, nullable=True)
    longitud = Column(String, nullable=True)
    altitud = Column(Integer, nullable=True)