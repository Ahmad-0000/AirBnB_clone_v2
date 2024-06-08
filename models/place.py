#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship

place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", ForeignKey("places.id"),
                             primary_key=True),
                      Column("amenity_id", ForeignKey("amenities.id"),
                             primary_key=True))

if getenv('HBNB_TYPE_STORAGE') == "db":
    class Place(BaseModel, Base):
        """ Representing Place objects"""
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
        reviews = relationship("Review", back_populates='place',
                               cascade="all, delete, delete-orphan")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False)
        amenity_ids = []
else:
    class Place(BaseModel):
        """ Representing Place objects"""
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """Property method to retrive all reviews objects with an "id"
            equal to the current "Place" class id"""
            from models import storage
            from models.review import Review
            reviews_dict = storage.all(Review)
            reviews_list = []
            for key, value in review_dict.items():
                reviews_list.append(value)
            filtered_reviews_list = []
            for review in filtered_reviews_list:
                if review.place_id == self.id:
                    filtered_reviews_list.append(review)
            return filtered_reviews_list

        @property
        def amenities(self):
            """Retriving all objects of "Amenity" class in "Place.amentiyt_ids"
            which has an "id" equal to the current "Place.id" attribute"""
            amenities_list = []
            for amenity in Place.amenity_ids:
                if amenity.id == self.id:
                    amenities_list.append(amenity)
            return amenities_list

        @amenities.setter
        def amenities(self, amenity_obj):
            '''Adding "amenity_obj" to "Place.amenity_ids" if it is an instance
            of "Amenity" class'''
            if isinstance(amenity_obj, Amenity):
                Place.amenity_ids.append(amenity_obj)
