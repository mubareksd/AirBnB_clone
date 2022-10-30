#!/usr/bin/python3
"""
test_place module
"""
from unittest import TestCase
from models.place import Place


class TestPlace(TestCase):
    """
    TestPlace class
    """

    def test_module_doc(self):
        """test module documentation"""
        doc = __import__('models.place').__doc__
        self.assertGreater(len(doc), 1)

    def test_class_doc(self):
        """test class documentation"""
        doc = Place.__doc__
        self.assertGreater(len(doc), 1)