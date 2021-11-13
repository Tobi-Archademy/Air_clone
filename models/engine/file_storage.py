#!/usr/bin/python3
"""
Defines a FileStorage Class
"""

import json

class FileStorage:
    """Representation of a FileStorage"""
    __file_path = "file.json"
    __objects = {}
    def __init__(self):
        """initializes the storage"""

    def all(self):
        """returns the dictionary objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = __class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(json_objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as k:
                j_obj = json.load(k)
            for key in j_obj:
                self.__objects[key] = classes[j_obj[key]["__class__"]](**j_obj[key])
        except:
            pass
        
