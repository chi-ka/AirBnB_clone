import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        try:
            os.remove(self.storage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_all_empty(self):
        all_objects = self.storage.all()
        self.assertEqual(len(all_objects), 0)

    def test_new_and_all(self):
        obj = BaseModel()
        self.storage.new(obj)
        all_objects = self.storage.all()
        self.assertEqual(len(all_objects), 1)
        self.assertIn(f"{obj.__class__.__name__}.{obj.id}", all_objects)

    def test_save_and_reload(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        # Create a new storage instance to simulate a program restart
        new_storage = FileStorage()
        new_storage.reload()

        all_objects = new_storage.all()
        self.assertEqual(len(all_objects), 1)
        self.assertIn(f"{obj.__class__.__name__}.{obj.id}", all_objects)

    def test_reload_nonexistent_file(self):
        # Ensure that reloading a non-existent file doesn't raise an error
        self.storage.reload()

    def test_reload_empty_file(self):
        # Create an empty file to simulate an empty file scenario
        with open(self.storage._FileStorage__file_path, 'w') as file:
            file.write("")

        self.storage.reload()

        all_objects = self.storage.all()
        self.assertEqual(len(all_objects), 0)

if __name__ == '__main__':
    unittest.main()

