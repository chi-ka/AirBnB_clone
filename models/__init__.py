#!/usr/bin/python3
'''Import the classes or functions that you want to make available'''

from models.engine import FileStorage

__all__ = ['BaseModel']
storage = FileStorage()
storage.reload()
