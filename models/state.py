#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from models.city import City
from models import storage
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'

    name = Column(String(128), nullable=True)
    cities = relationship('City',
        backref='state',
        cascade='delete-orphan')

    @property
    def cities(self):
        """ get instances with the same id from 
            states mapped class
        """

        cities = storage.all(City)
        id = self.id
        instance_list = []

        if cities is not None:
            for k, v in cities.items():
                if v.id == id: list.append(v)
        return instance_list
