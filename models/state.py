#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from models.city import City
import models
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import relationship
import os

storage = os.getenv(HBNB_TYPE_STORAGE)

class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'

    if storage == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City',
            backref = 'state',
            cascade = 'all, delete-orphan'
        )

    else:
        name = ""
        @property
        def cities(self):
            """ get instances with the same id from 
                states mapped class
            """

            if cities is not None:
                id = self.id
                instance_list = []
                for k, v in cities.items():
                    if v.id == id: instance_list.append(v)
            return instance_list
