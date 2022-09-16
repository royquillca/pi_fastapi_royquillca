from datetime import datetime
from pydantic import BaseModel


class CarreraBase(BaseModel):
    raceId: int
    name: str
    round: int
    time: str
    date: datetime
    circuitId: int

class RaceRes(BaseModel):
    anio: int
    counter: int

    class Config:
        orm_mode = True