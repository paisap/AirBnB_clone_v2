#!/usr/bin/python3
""" New engine """
from sqlalchemy import create_engine
import os


class DBStorage:
    """ class DBStorage """

    __engine = None
    __session = None

    def __init__(self):
        """ the init method """
        self.__engine = create_engine('mysql+mysqldb://\
        {}:{}@{}/{}'.format(os.enviroment.get("HBNB_MYSQL_USER"),
                            os.environ.get("HBNB_MYSQL_PWD"),
                            os.environ.get("HBNB_MYSQL_HOST"),
                            os.environ.get("HBNB_MYSQL_DB")),
                            pool_pre_ping=True)
        if os.environ.get("HBNB_ENV") == 'test':
            drop_all()

    def all(self, cls=None):
        """ class all
        """
        