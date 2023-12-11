#!/usr/bin/python3
'''a class User that inherits from BaseModel'''

from models.base_model import BaseModel


class User(BaseModel):
    '''BaseModel SubClass Named User'''

    def __init__(self, *args, **kwargs):
        """Initialize User instance"""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

    def __str__(self):
        """String representation of User"""
        tmp = self.__class__.__name__
        return "[{}] ({}) {}".format(tmp, self.id, self.__dict__)
