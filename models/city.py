#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey

class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """

    __tablename__ = 'cities'

    name = Column(String(128), nullable=True)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=True)

