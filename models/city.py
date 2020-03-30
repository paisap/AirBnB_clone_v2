#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel
from sqlalchemy import Column. Integer, String, Sequence

class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """

    __tablename__ = 'cities'

    name = Column(String(128), nullable=True)
    state_id = Column(String(60), ForeigKey('states.id'), nullable=True)

