#!/usr/bin/python3
"""
file_storage module
"""


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
        self.__objects["{}.{}.format(type(obj).__name__, obj.id)"] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, mode="w") as f:
            dict_srorage = {key: value.to_dict() for key, value in self.__objects.items()}
            json.dump(dict_storage, f)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise,
        do nothing. If the file doesn’t exist, no exception should be raised)
        """
