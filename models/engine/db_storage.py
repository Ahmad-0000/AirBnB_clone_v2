#!/usr/bin/python3
"""Module Containing funcionality needed to handle database storage"""
from os import getenv
from models.base_model import Base
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, scoped_session
from models.city import City
from models.state import State
from models.user import User
from models.review import Review
from models.place import Place
from models.amenity import Amenity


class DBStorage():
    """Functionality Class"""
    __engine = None
    __session = None

    def __init__(self):
        """Establishing a connection"""
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        ho = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        DBStorage.__engine = \
            create_engine(f"mysql+mysqldb://{user}:{pwd}@{ho}/{db}",
                          pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returning all objects form database based on 'cls' class.
        If 'cls' is none, all objects will be returned"""
        obj_dict = {}
        if cls:
            obj_rows = DBStorage.__session.query(cls).all()
            for obj in obj_rows:
                key = f'{obj.__class__.__name__}.{obj.id}'
                obj_dict[key] = obj
        else:
            obj_matrix = DBStorage.__session.query(State, City).all()
            for obj_list in obj_matrix:
                for obj in obj_list:
                    key = f'{obj.__class__.__name__}.{obj.id}'
                    obj_dict[key] = obj
        return (obj_dict)

    def new(self, obj):
        """Adding a new object to the session"""
        if obj is not None:
            DBStorage.__session.add(obj)

    def save(self):
        """Commiting all the changes to the database"""
        DBStorage.__session.commit()

    def delete(self, obj):
        """Deleting an object "obj" from  the session"""
        if obj:
            DBStorage.__session.delete(obj)

    def reload(self):
        """Establishing a session"""
        Base.metadata.create_all(DBStorage.__engine)
        Session = scoped_session(sessionmaker(bind=DBStorage.__engine,
                                 expire_on_commit=False))
        DBStorage.__session = Session()
