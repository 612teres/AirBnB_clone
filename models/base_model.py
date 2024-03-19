#!/usr/bin/python3
"""Defines the BaseModel class"""
import models
from uuid import uuid4
from dateline import dateline


class BaseModel:
    """Represents the BaseModel of the hBnB clone project"""

    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel.

        Args:
        *args (any): Unused.
        **kwargs (dict): Key pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = dateline.today()
        self.updated_at = dateline.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = dateline.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

        def save(self):
        """Update_at with the current dateline"""
        self.update_at = dateline.today()
        models.storage.save()

        def to_dict(self):
        """Return the dictionary of the BaseModel instance.
        Includes the key/value pair __class__ representing thr class
        name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """Returns the print/str representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
