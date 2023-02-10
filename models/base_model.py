#!/usr/bin/python3
""" class BaseModel base class attributes/methods for other classes"""
from datetime import datetime
import uuid


class BaseModel:
    """ Represent Base class """

    def __init__(self):
        """ Initialize a base class

        Args:
        id (int): The identity of the new base
        created_at(datetime): created time
        updated_at(datetime): updated time
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Update the attribute updated_at with the current time """
        self.updated_at = datetime.now()

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
