#!/usr/bin/python3
"""
the storage engine to serialize and deserialize objects
"""


import json
import os
from models.base_model import BaseModel


class FileStorage:
    """
    the file storage engine
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        obj_dic = {key: value.to_dict() for key, value in self.__objects.items()}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dic, f)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                json_dict = json.load(f)

                for key, value in json_dict.items():
                    self.__objects[key] = eval(value['__class__'])(**value)
