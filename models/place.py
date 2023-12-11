#!/usr/bin/python3
'''a class User that inherits from BaseModel'''

from models.base_model import BaseModel


class Place(BaseModel):
    '''BaseModel SubClass Named State'''

    city_id = ''
    user_id = ''
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_id = []

    def __init__(self, *args, **kwargs):
        """Initialize User instance"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """String representation of User"""
        temp = self.__class__.__name__
        return "[{}] ({}) {}".format(temp, self.id, self.__dict__)
