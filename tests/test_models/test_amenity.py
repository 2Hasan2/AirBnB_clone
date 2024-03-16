#!/usr/bin/python3
"""Defines unittests for models/amenity.py."""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenityInstantiation(unittest.TestCase):
	"""Unittests for testing instantiation of the Amenity class."""

	def test_no_args_instantiates(self):
		"""Test that Amenity can be instantiated with no arguments."""
		self.assertEqual(Amenity, type(Amenity()))

	def test_new_instance_stored_in_objects(self):
		"""Test that a new instance of Amenity is stored in objects."""
		self.assertIn(Amenity(), models.storage.all().values())

	def test_id_is_public_str(self):
		"""Test that the id attribute of Amenity is a string."""
		self.assertEqual(str, type(Amenity().id))

	def test_created_at_is_public_datetime(self):
		"""Test that the created_at attribute of Amenity is a datetime object."""
		self.assertEqual(datetime, type(Amenity().created_at))

	def test_updated_at_is_public_datetime(self):
		"""Test that the updated_at attribute of Amenity is a datetime object."""
		self.assertEqual(datetime, type(Amenity().updated_at))

	def test_name_is_public_class_attribute(self):
		"""Test that name is a public class attribute of Amenity."""
		am = Amenity()
		self.assertEqual(str, type(Amenity.name))
		self.assertIn("name", dir(Amenity()))
		self.assertNotIn("name", am.__dict__)

	def test_two_amenities_unique_ids(self):
		"""Test that two instances of Amenity have different ids."""
		am1 = Amenity()
		am2 = Amenity()
		self.assertNotEqual(am1.id, am2.id)

	def test_two_amenities_different_created_at(self):
		"""Test that two instances of Amenity have different created_at values."""
		am1 = Amenity()
		sleep(0.05)
		am2 = Amenity()
		self.assertLess(am1.created_at, am2.created_at)

	def test_two_amenities_different_updated_at(self):
		"""Test that two instances of Amenity have different updated_at values."""
		am1 = Amenity()
		sleep(0.05)
		am2 = Amenity()
		self.assertLess(am1.updated_at, am2.updated_at)
