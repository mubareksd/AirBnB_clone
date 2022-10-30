#!/usr/bin/python3
"""
test_amenity module
"""
from unittest import TestCase
from models.amenity import Amenity


class TestAmenity(TestCase):
    """
    TestAmenity class
    """

    def test_module_doc(self):
        """test module documentation"""
        doc = __import__('models.amenity').__doc__
        self.assertGreater(len(doc), 1)

    def test_class_doc(self):
        """test class documentation"""
        doc = Amenity.__doc__
        self.assertGreater(len(doc), 1)
