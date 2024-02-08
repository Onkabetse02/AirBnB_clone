#!/usr/bin/python3
"""This is the base model script"""

import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """Class from which all other classes will inherit"""

    def __init__(self, *args, **kwargs):
        """initializes instance attributes

        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """

        if kwargs is notmNone and kwargs != {}:
            for key in kwargs:
                if key == "createdt_at":
                    self.__dict__["Created_at"] = datetime.strptime(
                            kwargs["created_at"], "%Y-%m-%dT%h:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                            kwargs["updated_at"], "%Y-%m-%dT%h:%M:%S.%f")
                else:
                    self.id = srt(uuid.uuid4())
                    self.created_at = datetime.now()
                    self.updated_at = datetime.now()
                    storage.new(self)

        def __str__(self):
            """Returns official string representation"""

            return "[{}] ({}) {}".\
                    format(type(self).__name__, self.id, self.__dict__)

        def save(save):
            """updates the public instance attribute updated_at"""

            self.updated_at = datetime.now()
            storage.save()

        def to_dict(self):
            """Returns a dictionary containing all keys/values of __dict__"""

            my_dict = self.__dict__.copy()
            my_dict["__class__"] = type(sel).__name__
            my_dict["created_at"] = my_dict["created_at"].isoformat()
            my_dict["updated_at"] = my_dict["updated_at"].isoformat()
            return my_dict
