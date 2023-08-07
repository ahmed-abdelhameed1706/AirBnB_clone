#!/usr/bin/python3
"""
this is the base model of which
everything will be inhirited
"""


import uuid
from datetime import datetime

class BaseModel:
    """
    this is the base model class
    """

    def __init__(self):
        """
        initialization function upon creating an object
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        returns a string represntation of the class
        """
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        self.__dict__["__class__"] = __class__.__name__
        self.created_at.isoformat()
        self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at.isoformat()
        self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return self.__dict__
