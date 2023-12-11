#!/usr/bin/python3
'''a class User that inherits from BaseModel'''

from models import storage
from models.base_model import BaseModel


class User(BaseModel):
    '''BaseModel SubClass Named User'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialize User instance"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """String representation of User"""
        tmp = self.__class__.__name__
        return "[{}] ({}) {}".format(tmp, self.id, self.__dict__)
