#!/usr/bin/python3
""" New class for file storage """

import json
from os.path import exists
from models.base_model import BaseModel

class FileStorage:
    """ Serializes and deserializes objects to/from JSON """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ Serializes __objects to JSON file """
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(obj_dict, file)

    def reload(self):
        """ Deserializes JSON file to __objects """
        if exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name = value['__class__']
                    obj = eval(class_name)(**value)
                    self.__objects[key] = obj

    def close(self):
        """ Calls reload() method for deserializing the JSON file to objects """
        self.reload()
