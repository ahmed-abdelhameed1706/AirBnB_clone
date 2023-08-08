#!/usr/bin/python3
"""
the base model module
"""


import uuid
from datetime import datetime
import models


class BaseModel:
    """
    the main class
    """
    def __init__(self, *args, **kwargs):
        """
        initialize a new model with kwargs or new
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        val = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                        setattr(self, key, val)
                    else:
                        setattr(self, key, value)
        else:
            models.storage.new(self)

    def __str__(self):
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        dict_cp = self.__dict__.copy()
        dict_cp["__class__"] = __class__.__name__
        dict_cp["created_at"] = self.created_at.isoformat()
        dict_cp["updated_at"] = self.updated_at.isoformat()
        return dict_cp
