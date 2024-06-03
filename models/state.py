#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship('City', back_populates='state',
                          cascade='all, delete, delete-orphan')
    else:
        @property
        def cities(self):
            '''Returning a list of "City" instances with "state_id" equal
            to the current "State.id"'''
            initial_cities_list = []
            initial_cities_list = storage.all(City)
            cities_list = []
            for city in initial_cities_list:
                if city.state_id == State.id:
                    cities_list.append(city)
            return cities_list
