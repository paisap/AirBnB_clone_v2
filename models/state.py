#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from models.city import City
import models
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship('City',
        backref = 'state',
        cascade = 'delete, delete-orphan'
    )

    @property
    def cities(self):
        """ get instances with the same id from 
            states mapped class
        """

        cities = models.storage.all(City)
        id = self.id
        instance_list = []

        if cities is not None:
            for k, v in cities.items():
                if v.id == id: instance_list.append(v)
        return instance_list
