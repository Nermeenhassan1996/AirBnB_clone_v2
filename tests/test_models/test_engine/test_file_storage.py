#!/usr/bin/python3
"""
Test for storage
"""
import json
import os
from models import storage
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """Tests for FileStorage class"""

    def setUp(self):
        """Set up for tests"""
        if os.path.isfile("file.json"):
            os.rename("file.json", "tempfile.json")

    def tearDown(self):
        """Tear down for tests"""
        if os.path.isfile("file.json"):
            os.remove("file.json")
        if os.path.isfile("tempfile.json"):
            os.rename("tempfile.json", "file.json")

    def test_file_path(self):
        """Test __file_path"""
        self.assertEqual(type(storage._FileStorage__file_path), str)
        self.assertEqual(storage._FileStorage__file_path, "file.json")

    def test_objects(self):
        """Test __objects"""
        self.assertEqual(type(storage._FileStorage__objects), dict)

    def test_all(self):
        """test all method"""
        storage = FileStorage()
        objects = storage.all()
        self.assertIsNotNone(objects)
        self.assertEqual(type(objects), dict)

    def test_new(self):
        """test new method"""
        obj = BaseModel()
        storage.new(obj)
        objects = storage.all()
        class_name = obj.__class__.__name__
        key = "{}.{}".format(class_name, str(obj.id))
        self.assertEqual(objects[key] is obj, True)

    def test_save(self):
        """test save method"""
        obj1 = BaseModel()
        obj2 = User()
        obj3 = State()
        obj4 = Place()
        obj5 = City()
        obj6 = Amenity()
        obj7 = Review()
        storage.new(obj1)
        storage.new(obj2)
        storage.new(obj3)
        storage.new(obj4)
        storage.new(obj5)
        storage.new(obj6)
        storage.new(obj7)
        storage.save()
        text = ""
        with open("file.json", "r") as f:
            text = f.read()
            self.assertIn("BaseModel." + obj1.id, text)
            self.assertIn("User." + obj2.id, text)
            self.assertIn("State." + obj3.id, text)
            self.assertIn("Place." + obj4.id, text)
            self.assertIn("City." + obj5.id, text)
            self.assertIn("Amenity." + obj6.id, text)
            self.assertIn("Review." + obj7.id, text)

    def test_reload(self):
        """test reload method"""
        obj1 = BaseModel()
        obj2 = User()
        obj3 = State()
        obj4 = Place()
        obj5 = City()
        obj6 = Amenity()
        obj7 = Review()
        storage.new(obj1)
        storage.new(obj2)
        storage.new(obj3)
        storage.new(obj4)
        storage.new(obj5)
        storage.new(obj6)
        storage.new(obj7)
        storage.save()
        storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + obj1.id, objs)
        self.assertIn("User." + obj2.id, objs)
        self.assertIn("State." + obj3.id, objs)
        self.assertIn("Place." + obj4.id, objs)
        self.assertIn("City." + obj5.id, objs)
        self.assertIn("Amenity." + obj6.id, objs)
        self.assertIn("Review." + obj7.id, objs)


if __name__ == '__main__':
    unittest.main()
