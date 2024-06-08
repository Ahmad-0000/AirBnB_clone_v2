#!/usr/bin/python3
"""Define the class to manage database storage for HBNB objects"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base


class DBStorage():
    """To manage database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialization of storage variable"""
        if getenv("HBNB_TYPE_STORAGE") == "db":
            usr = getenv("HBNB_MYSQL_USER")
            pwd = getenv("HBNB_MYSQL_PWD")
            db = getenv("HBNB_MYSQL_DB")
            host = getenv("HBNB_MYSQL_HOST")
            url = 'mysql+mysqldb://{}:{}@{}/{}'.format(usr, pwd, host, db)
            DBStorage.__engine = create_engine(url, pool_pre_ping=True)
            Session = sessionmaker(bind=DBStorage.__engine)
            DBStorage.__session = Session()
            if getenv("HBNB_ENV") == "test":
                Base.metadate.drop_all(DBStorage.__engine)

    def all(self, cls=None):
        """Return all instances of class cls or all instances if None"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review

        classes = {'User': User, 'BaseModel': BaseModel,
                   'State': State, 'City': City,
                   'Place': Place, 'Amenity': Amenity,
                   'Review': Review}

        obj_dict = {}
        if cls:
            if cls in classes.values():
                obj_rows = DBStorage.__session.query(cls).all()
                for obj in obj_rows:
                    key = f'{cls.__name__}.{obj.id}'
                    obj_dict[key] = obj
        else:
            obj_matrix = DBStorage.__session.query(State, City, User,
                                                   Place, User, Review).all()
            for obj_list in obj_matrix:
                for obj in obj_list:
                    key = f'{obj.__class__.__name__}.{obj.id}'
                    obj_dict[key] = obj
        return (obj_dict)

    def new(self, obj):
        """Add obj to the current session"""
        DBStorage.__session.add(obj)

    def save(self):
        """Save all the changes to the database"""
        DBStorage.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current session"""
        if obj:
            DBStorage.__session.delete(obj)

    def reload(self):
        """Reload all the objects from the database"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review

        Base.metadata.create_all(DBStorage.__engine)
        Session = scoped_session(sessionmaker(bind=DBStorage.__engine,
                                              expire_on_commit=False))
        DBStorage.__session = Session()

    def close(self):
        """Reloading the session"""
        DBStorage.__session.close()
