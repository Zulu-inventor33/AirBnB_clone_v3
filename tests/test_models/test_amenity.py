#!/usr/bin/python3
"""Unittest module for the Amenity Class."""

import unittest
from datetime import datetime
import time
from models.amenity import Amenity
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test cases for the `Amenity` class."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Tests instantiation of Amenity class."""

        b = Amenity()
        self.assertEqual(str(type(b)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(b, Amenity)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_str(self):
        """Test method for str representation"""
        a1 = Amenity()
        string = f"[{type(a1).__name__}] ({a1.id}) {a1.__dict__}"
        self.assertEqual(a1.__str__(), string)

    def test_save(self):
        """Test method for save"""
        a1 = Amenity()
        old_update = a1.updated_at
        a1.save()
        self.assertNotEqual(a1.updated_at, old_update)

if __name__ == "__main__":
    unittest.main()
