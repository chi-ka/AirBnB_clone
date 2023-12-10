#!/usr/bin/python3

import uuid
from datetime import datetime as dt
from models import storage


class BaseModel():
    '''The base model of other creationa'''


    def __init__(self, *args, **kwargs):
        '''initializing the base model and it's attributes'''

        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key in ['created_at', 'updated_at']:
                    if isinstance(value, str):
                        setattr(self, key, dt.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = dt.now()
            self.updated_at = dt.now()
            storage.new(self)


    def save(self):
        '''updates the public instance attribute updated_at
        with the current datetime'''
        self.updated_at = dt.now()
        storage.save()

    def __str__(self):
        '''prints [<class name>] (<self.id>) <self.__dict__>'''

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__
        of the instance"""

        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat() if isinstance(self.created_at, dt) else None
        obj_dict['updated_at'] = self.updated_at.isoformat() if isinstance(self.updated_at, dt) else None

        return obj_dict
