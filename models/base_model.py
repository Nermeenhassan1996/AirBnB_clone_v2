#!/usr/bin/python3
"""Module for Base class
Contains the Base class for the AirBnB clone console.
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """ class base """
    def __init__(self, *args, **kwargs):
        """ constructor """
        if kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                if key == "created_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key == "updated_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key == "__class__":
                    pass
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """ updates updated_at with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of the instance """
        dic_copy = self.__dict__.copy()
        dic_copy["__class__"] = self.__class__.__name__
        dic_copy["created_at"] = self.created_at.isoformat()
        dic_copy["updated_at"] = self.updated_at.isoformat()
        return dic_copy

    def __str__(self):
        """ Returns a human-readable string representation
        of an instance """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
