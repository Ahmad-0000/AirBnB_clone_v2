#!/usr/bin/python3
""" Amenity Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from models.place import place_amenity
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


if getenv("HBNB_TYPE_STORAGE") == "db":
    class Amenity(BaseModel, Base):
        """Representing amenities objects"""

        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary=place_amenity)
else:
    class Amenity(BaseModel):
        """Representing amenities objects"""
        name = ""
