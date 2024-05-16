#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.review import Review

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    user = relationship('User', back_populates='places')
    cities = relationship('City', back_populates='places')
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        reviews = relationship("Review", back_populates='place',
                               cascade="all, delete, delete-orphan")
    else:
        @property
        def reviews(self):
            """Property method to retrive all reviews objects with an "id"
            equal to the current "Place" class id"""
            from models import storage
            intial_reviews_list = storage.all(Review)
            reviews_list = []
            for review in intial_reviews_list:
                if review.place_id == Place.id:
                    reviews_list.append(review)
            return reviews_list

    amenity_ids = []
