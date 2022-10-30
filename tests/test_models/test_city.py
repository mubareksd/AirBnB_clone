#!/usr/bin/python3
"""
test_city module
"""
from unittest import TestCase
from models.city import City


class TestCity(TestCase):
    """
    TestCity class
    """

    def test_module_doc(self):
        """test module documentation"""
        doc = __import__('models.city').__doc__
        self.assertGreater(len(doc), 1)

    def test_class_doc(self):
        """test class documentation"""
        doc = City.__doc__
        self.assertGreater(len(doc), 1)
