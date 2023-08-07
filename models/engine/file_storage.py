#!/usr/bin/python3
"""
the storage engine to serialize and deserialize objects
"""


import json
import os


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
        with open(self.__file_path, "w", encoding="utf-8") as f: 
            json.dump(self.__objects, f)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                self.__objects = json.load(f)
