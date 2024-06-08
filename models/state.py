#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

if getenv("HBNB_TYPE_STORAGE") == "db":
    class State(BaseModel, Base):
        """Representing State objects"""
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship('City', back_populates='state',
                              cascade='all, delete, delete-orphan')  # Be ware,
        # you don't fully understand this

else:
    class State(BaseModel):
        """Representing State objects"""
        name = ""

        @property
        def cities(self):
            """Return all cities linked to this  state"""
            from models import storage
            from models.city import City
            all_cities = storage.all(City)
            init_cities_list = []
            for key, value in all_cities.items():
                if key.split(".")[0] == "City":
                    init_cities_list.append(value)
            filtered_cities_list = []
            for city in init_cities_list:
                if city.state_id == self.id:
                    filtered_cities_list.append(city)
            return filtered_cities_list
