#!/usr/bin/python3
""" Review module for the HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


if getenv("HBNB_TYPE_STORAGE") == "db":
    class Review(BaseModel, Base):
        """Representing Review objects"""
        __tablename__ = 'reviews'
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        text = Column(String(1024), nullable=False)
        user = relationship("User", back_populates='reviews')
        place = relationship("Place", back_populates='reviews')
else:
    class Review(BaseModel):
        """Representing Review objects"""
        place_id = ""
        user_id = ""
        text = ""
