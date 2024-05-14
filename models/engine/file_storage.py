#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}
    classes = ['BaseModel', 'User', 'State', 'City', 'Amenity',
               'Place', 'Review']

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None and type(cls) is not type:
            raise TypeError('"cls" must a class or None')
        if cls is not None and cls.__name__ not in FileStorage.classes:
            raise ValueError(f'{cls} does not exist')
        if cls is not None:
            filtered_dict = {}
            for key in FileStorage.__objects.keys():
                if cls.__name__ in key:
                    filtered_dict[key] = FileStorage.__objects[key]
            return filtered_dict
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        if obj:
            cls_name = obj.__class__.__name__
            if cls_name not in FileStorage.classes:
                raise TypeError('obj is not valid')
            del self.__objects[f'{cls_name}.{obj.id}']
