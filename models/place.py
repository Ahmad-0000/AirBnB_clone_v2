#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.review import Review

place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", ForeignKey("amenities.id"),
                             primary_key=True),
                      Column("amenity_id", ForeignKey("places.id"),
                             primary_key=True))


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
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False)
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

        @property
        def amenities(self):
            """Retriving all objects of "Amenity" class in "Place.amentiyt_ids"
            which has an "id" equal to the current "Place.id" attribute"""
            amenities_list = []
            for amenity in amenity_ids:
                if amenity.id == Place.id:
                    amenities_list.append(amenity)
            return amenities_list

        @amenities.setter
        def amenities(self, amenity_obj):
        '''Adding "amenity_obj" to "Place.amenity_ids" if it is an instance
        of "Amenity" class'''
            if isinstance(amenity_obj, Amenity):
                Place.amenity_ids.append(amenity_obj)

    amenity_ids = []
