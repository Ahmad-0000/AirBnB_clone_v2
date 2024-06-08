#!/usr/bin/python3
""" User Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

if getenv("HBNB_TYPE_STORAGE") == "db":
    class User(BaseModel, Base):
        """Representing User objects"""
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship('Place', back_populates='user',
                              cascade="all, delete, delete-orphan")
        reviews = relationship("Review", back_populates="user",
                               cascade="all, delete, delete-orphan")
else:
    class User(BaseModel):
        """Representing User objects"""
        email = ''
        password = ''
        first_name = ''
        last_name = ''
