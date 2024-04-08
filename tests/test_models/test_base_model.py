#!/usr/bin/python3
"""Defines unittests for models/base_model.py"""

import unittest
from models.base_model import BaseModel


class TestBasemodel(unittest.TestCase):
    """unittest for testing instantiation of basemodel"""
    def test_init(self):
        """test if an object is an type basemodel"""
        my_model = BaseModel()

        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_save(self):
        """check if date updated when saved"""
        my_model = BaseModel()

        first_update = my_model.updated_at
        sec_update = my_model.save()
        self.assertNotEqual(first_update, sec_update)
        
    def test_to_dict(self):
        '''check if to_dict returns a dictionary, if add a class
        key with class name of the object and if updated_at and
        created_at are converted to string object in ISO format.'''
        my_model = BaseModel()

        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)

        self.assertEqual(my_model_dict["__class__"], 'BaseModel')
        self.assertEqual(my_model_dict['id'], my_model.id)
        self.assertEqual(my_model_dict['created_at'], my_model.created_at.isoformat())
        self.assertEqual(my_model_dict['updated_at'], my_model.updated_at.isoformat())

    def test_str(self):
        """check if the output of str is in the specified format"""
        my_model = BaseModel()
        dictionary = my_model.__dict__

        string1 = "[BaseModel] ({}) {}".format(my_model.id, dictionary)
        string2 = str(my_model)
        self.assertEqual(string1, string2)


if __name__ == '__main__':
    unittest.main()
