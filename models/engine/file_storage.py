#!/usr/bin/python3
'''Write a class FileStorage that serializes instances
to a JSON file and deserializes JSON file to instances'''
import json
import importlib


class FileStorage():
    '''serializes instances to a JSON file and deserializes
    JSON file to instances'''

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        '''Initializes an instance of a class FileStorage'''

    def all(self):
        '''Returns the dictionary __objects'''
        return self.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        Classname = obj.__class__.__name__
        Obj_id = obj.id
        Obj_key = Classname + '.' + Obj_id
        self.__objects[Obj_key] = obj

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)'''
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        '''deserializes the JSON file to __objects if
        the JSON file (__file_path) exists;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)'''
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                if not data:
                    data = {}
                for key, obj_dict in data.items():
                    class_name, obj_id = key.split('.')
                    if class_name == 'BaseModel':
                        module_name = f"models.base_model"
                    if class_name == 'User':
                        module_name = f"models.user"
                    module = importlib.import_module(module_name)
                    class_ = getattr(module, class_name)
                    obj_instance = class_(**obj_dict)
                    self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass
