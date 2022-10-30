#!/usr/bin/python3
"""
test_review module
"""
from unittest import TestCase
from models.review import Review


class TestReview(TestCase):
    """
    TestReview class
    """

    def test_module_doc(self):
        """test module documentation"""
        doc = __import__('models.review').__doc__
        self.assertGreater(len(doc), 1)

    def test_class_doc(self):
        """test class documentation"""
        doc = Review.__doc__
        self.assertGreater(len(doc), 1)