#!/usr/bin/python3
""" class BaseModel base class attributes/methods for other classes"""
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """ Represent Base class """

    def __init__(self, *args, **kwargs):
        """ Initialize a base class

        Args:
        id (int): The identity of the new base
        created_at(datetime): created time
        updated_at(datetime): updated time
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                else:
                    if key == "created_at" or key == "updated_at":
                        self.__dict__[key] = datetime.strptime(value,
                                                               time_format)
                    else:
                        self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """Update the attribute updated_at with the current time """
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """ Return the print and str representation of Base model """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)

    def to_dict(self):
        """Returns the dictionary representation of a Base class """
        bdict = self.__dict__.copy()
        bdict["__class__"] = self.__class__.__name__
        bdict["created_at"] = self.created_at.isoformat()
        bdict["updated_at"] = self.updated_at.isoformat()
        return bdict
