# External modules
from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List
# Internal Modules
from config.db import get_pidb
from models.race import Race

from schemas.race import RaceRes

race_route = APIRouter(tags=['Q2: Year with more races'])

@race_route.get('/year-with-more-races',
                 status_code=status.HTTP_200_OK,
                 response_model=List[RaceRes])
def get(db: Session = Depends(get_pidb)):
    query = (
        db.query(Race)
            .group_by(func.year(Race.date))
            .order_by(func.count(Race.raceId).desc())
            .limit(1)
            .with_entities(
                func.year(Race.date).label('year'),
                func.count(Race.raceId).label('round')
            ).all()
    )
    return query
