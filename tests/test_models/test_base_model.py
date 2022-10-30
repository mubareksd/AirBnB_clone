#!/usr/bin/python3
"""
test_base_model module
"""
import unittest
from uuid import uuid4
from datetime import datetime
import time
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class
    """

    def setUp(self):
        """"""
        pass

    def tearDown(self):
        """"""
        pass

    def test3(self):
        """"""
        my_model = BaseModel()

    def test3save(self):
        """"""
        my_model = BaseModel()
        time.sleep(0.5)
        current = datetime.now()
        my_model.save()

    def test3dict(self):
        """"""
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
