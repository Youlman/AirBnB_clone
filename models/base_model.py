#!/usr/bin/python3
"""This script is the base model"""

import uuid
from datetime import datetime
import uuid


class BaseModel:

    """Class from which all other classes will inherit"""

    def __init__(self):
        """ Initialize a base class

        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value

    def save(self):
        """updates the public instance attribute updated_at"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns the dictionary representation of a Base class """
        self.__dict__["__class__"] = self.__class__.__name__
        self.__dict__["created_at"] = self.created_at.isoformat()
        self.__dict__["updated_at"] = self.updated_at.isoformat()
        return self.__dict__
