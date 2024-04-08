#!/usr/bin/python3
"""Defines unittests for models/city.py.

Unittest classes:
    TestCity_instantiation
    TestCity_save
    TestCity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from models.city import City


class TestCity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the City class."""

    def test_no_args_instantiates(self):
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_is_public_class_attribute(self):
        my_model = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(my_model))
        self.assertNotIn("state_id", my_model.__dict__)

    def test_name_is_public_class_attribute(self):
        my_model = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(my_model))
        self.assertNotIn("name", my_model.__dict__)

    def test_id(self):
        """ test that id is unique """
        my_objectId = City()
        my_objectId1 = City()
        self.assertNotEqual(my_objectId.id, my_objectId1.id)

    def test_str(self):
        '''check if the output of str is in the specified format'''
        my_strobject = City()
        _dict = my_strobject.__dict__
        string1 = "[City] ({}) {}".format(my_strobject.id, _dict)
        string2 = str(my_strobject)
        self.assertEqual(string1, string2)

    def test_save(self):
        """ check if date update when save """
        my_object = City()
        first_updated = my_object.updated_at
        my_object.save()
        second_updated = my_object.updated_at
        self.assertNotEqual(first_updated, second_updated)

    def test_City_dict(self):
        """ City_dict """
        my_object = City()
        self.assertTrue('id' in my_object.__dict__)
        self.assertTrue('created_at' in my_object.__dict__)
        self.assertTrue('updated_at' in my_object.__dict__)
        self.assertTrue('state_id' in my_object.__dict__)
        self.assertTrue('name' in my_object.__dict__)
        self.assertTrue('__class__' in my_object.__dict__)


if __name__ == "__main__":
    unittest.main()
