#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.city import City
from models.place import Place

name_class = ["BaseModel", "City", "State",
              "Place", "Amenity", "Review", "User"]


class FileStorage:
    """
    that serializes instances to a JSON file
    and deserializes JSON file to instances
    Attributes:
    __file_path: private attribute that have the path of the json file
    __objects: private attribute that contain the dic of instance
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """  returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """
        This method adds a new object to the
        __objects dictionary. The object is stored
        with a key in the format "<class_name>.<object_id>"
        """
        class_name = obj.__class__.__name__
        key = "{}.{}".format(class_name, str(obj.id))
        value_dict = obj
        self.__objects[key] = value_dict

    def save(self):
        """ serializes __objects to the JSON file """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(new_dict, f)

    def reload(self):
        """ deserializes the JSON file to __objects """
        try:
            with open(FileStorage.__file_path, "r") as f:
                python_dic = json.load(f)
            for key, value in python_dic.items():
                class_name = key.split(".")[0]
                if class_name in name_class:
                    FileStorage.__objects[key] = eval(class_name)(**value)
        except FileNotFoundError:
            pass
