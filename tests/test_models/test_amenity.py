#!/usr/bin/python3
"""Defines unittests for models/amenity.py.

Unittest classes:
    TestAmenity_instantiation
    TestAmenity_save
    TestAmenity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Amenity class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_public_class_attribute(self):
        my_model = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", my_model.__dict__)

    def test_id(self):
        """ test that id is unique """
        my_objectId = Amenity()
        my_objectId1 = Amenity()
        self.assertNotEqual(my_objectId.id, my_objectId1.id)

    def test_str(self):
        '''check if the output of str is in the specified format'''
        my_object = Amenity()
        _dict = my_object.__dict__
        string1 = "[Amenity] ({}) {}".format(my_object.id, _dict)
        string2 = str(my_object)
        self.assertEqual(string1, string2)

    def test_save(self):
        """ check if date update when save """
        my_object = Amenity()
        first_updated = my_object.updated_at
        my_object.save()
        second_updated = my_object.updated_at
        self.assertNotEqual(first_updated, second_updated)

    def test_Amenity_dict(self):
        """Amenity_dict"""
        my_object = Amenity()
        self.assertTrue('id' in my_object.__dict__)
        self.assertTrue('created_at' in my_object.__dict__)
        self.assertTrue('updated_at' in my_object.__dict__)
        self.assertTrue('name' in my_object.__dict__)


if __name__ == "__main__":
    unittest.main()
