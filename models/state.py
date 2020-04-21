#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from models.city import City
import models
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    if os.environ.get("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref='state', cascade='delete')
    else:
        name = ""

        @property
        def cities(self):
            """ get instances with the same id from
            states mapped class
            """
            cities = models.storage.all(City)
            instance_list = []
            for key in cities.values():
                    if key.states.id == self.id:
                        instance_list.append(v)
            return instance_list
