#!/usr/bin/python3
'''a class User that inherits from BaseModel'''

from models.base_model import BaseModel


class Amenity(BaseModel):
    '''BaseModel SubClass Named State'''

    name = ''

    def __init__(self, *args, **kwargs):
        """Initialize User instance"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """String representation of User"""
        temp = self.__class__.__name__
        return "[{}] ({}) {}".format(temp, self.id, self.__dict__)
