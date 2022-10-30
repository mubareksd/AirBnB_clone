#!/usr/bin/python3
"""
test_state module
"""
from unittest import TestCase
from models.state import State


class TestState(TestCase):
    """
    TestState class
    """

    def test_module_doc(self):
        """test module documentation"""
        doc = __import__('models.state').__doc__
        self.assertGreater(len(doc), 1)

    def test_class_doc(self):
        """test class documentation"""
        doc = State.__doc__
        self.assertGreater(len(doc), 1)