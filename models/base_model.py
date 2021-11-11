#!/usr/bin/python3
"""
Contains class Base_model
"""

from datetime import datetime
import uuid

time = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    """Representation of a BaseModel class"""
    def __init__(self):
        """Initializes the base"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = self.created_at

    def __str__(self):
        """ overwrites the str """
        return("[{}]: ({}) - {}".format(str(self.__class__.__name__), self.id, self.__dict__))

    def save(self):
        """updates with the current date time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        dic = self.__dict__.copy()
        if "created_at" in dic:
            dic["created_at"] = dic["created_at"].strftime(time)
        if "updated_at" in dic:
            dic["updated_at"] = dic["updated_at"].strftime(time)
        dic["__class__"] =  self.__class__.__name__

        return dic



