#!/usr/bin/python3
"""
file_storage module
"""
import json
import os.path


class FileStorage:
    """
    FileStorage class
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects["{}.{}"
                       .format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, mode="w") as f:
            dict_storage = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(dict_storage, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise,
        do nothing. If the file doesn’t exist, no exception should be raised)
        """
        from models.base_model import BaseModel
        if not os.path.isfile(FileStorage.__file_path):
            return
        classes = {"BaseModel": BaseModel}
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: classes[v["__class__"]]
                        (**v) for k, v in obj_dict.items()}
            FileStorage.__objects = obj_dict
