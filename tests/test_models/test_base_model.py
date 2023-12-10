#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):

    def test_initialization_with_args(self):
        my_model = BaseModel(name="Test Model", my_number=42)
        self.assertEqual(my_model.name, "Test Model")
        self.assertEqual(my_model.my_number, 42)

    def test_initialization_with_kwargs(self):
        initial_created_at = "2023-01-01T12:00:00.000000"
        initial_updated_at = "2023-01-01T12:30:00.000000"
        my_model = BaseModel(
            id="test_id",
            created_at=initial_created_at,
            updated_at=initial_updated_at,
            name="Test Model",
            my_number=42
        )

        self.assertEqual(my_model.id, "test_id")
        self.assertEqual(my_model.name, "Test Model")
        self.assertEqual(my_model.my_number, 42)
        self.assertEqual(my_model.created_at, datetime.strptime(initial_created_at, '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(my_model.updated_at, datetime.strptime(initial_updated_at, '%Y-%m-%dT%H:%M:%S.%f'))

    def test_str_representation(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        expected_str = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), expected_str)

    def test_save_method(self):
        my_model = BaseModel()
        initial_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(initial_updated_at, my_model.updated_at)

    def test_to_dict_method(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        obj_dict = my_model.to_dict()

        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['created_at'], my_model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], my_model.updated_at.isoformat())
        self.assertEqual(obj_dict['name'], 'My First Model')
        self.assertEqual(obj_dict['my_number'], 89)

if __name__ == '__main__':
    unittest.main()

