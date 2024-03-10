#!/usr/bin/python3
"""Defines unittests for models/place.py."""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlaceInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""

    def test_no_args_instantiates(self):
        """Test that Place can be instantiated with no arguments."""
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored_in_objects(self):
        """Test that a new instance of Place is stored in objects."""
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Test that the id attribute of Place is a string."""
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public_datetime(self):
        """Test that the created_at attribute of Place is a datetime object."""
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_public_datetime(self):
        """Test that the updated_at attribute of Place is a datetime object."""
        self.assertEqual(datetime, type(Place().updated_at))

    def test_name_is_public_str(self):
        """Test that the name attribute of Place is a string."""
        self.assertEqual(str, type(Place.name))

    def test_description_is_public_str(self):
        """Test that the description attribute of Place is a string."""
        self.assertEqual(str, type(Place.description))

    def test_number_rooms_is_public_int(self):
        """Test that the number_rooms attribute of Place is an integer."""
        self.assertEqual(int, type(Place.number_rooms))

    def test_number_bathrooms_is_public_int(self):
        """Test that the number_bathrooms attribute of Place is an integer."""
        self.assertEqual(int, type(Place.number_bathrooms))

    def test_max_guest_is_public_int(self):
        """Test that the max_guest attribute of Place is an integer."""
        self.assertEqual(int, type(Place.max_guest))

    def test_price_by_night_is_public_int(self):
        """Test that the price_by_night attribute of Place is an integer."""
        self.assertEqual(int, type(Place.price_by_night))

    def test_latitude_is_public_float(self):
        """Test that the latitude attribute of Place is a float."""
        self.assertEqual(float, type(Place.latitude))

    def test_longitude_is_public_float(self):
        """Test that the longitude attribute of Place is a float."""
        self.assertEqual(float, type(Place.longitude))

    def test_amenity_ids_is_public_list(self):
        """Test that the amenity_ids attribute of Place is a list."""
        self.assertEqual(list, type(Place.amenity_ids))

    def test_two_places_unique_ids(self):
        """Test that two instances of Place have unique ids."""
        place1 = Place()
        place2 = Place()
        self.assertNotEqual(place1.id, place2.id)

    def test_two_places_different_created_at(self):
        """Test that two instances of Place have different
        created_at timestamps."""
        place1 = Place()
        sleep(0.05)
        place2 = Place()
        self.assertLess(place1.created_at, place2.created_at)

    def test_two_places_different_updated_at(self):
        """Test that two instances of Place have different
        updated_at timestamps."""
        place1 = Place()
        sleep(0.05)
        place2 = Place()
        self.assertLess(place1.updated_at, place2.updated_at)

    def test_str_representation(self):
        """Test the string representation of Place."""
        dt = datetime.today()
        dt_repr = repr(dt)
        place = Place()
        place.id = "123456"
        place.created_at = place.updated_at = dt
        place_str = place.__str__()
        self.assertIn("[Place] (123456)", place_str)
        self.assertIn("'id': '123456'", place_str)
        self.assertIn("'created_at': " + dt_repr, place_str)
        self.assertIn("'updated_at': " + dt_repr, place_str)

    def test_args_unused(self):
        """Test that passing None as an argument does not
        affect the instance attributes."""
        place = Place(None)
        self.assertNotIn(None, place.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Test instantiation of Place with keyword arguments."""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        place = Place(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(place.id, "345")
        self.assertEqual(place.created_at, dt)
        self.assertEqual(place.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        """Test instantiation of Place with None as keyword arguments."""
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)


class TestPlaceSave(unittest.TestCase):
    """Unittests for testing save method of the Place class."""

    @classmethod
    def setUpClass(cls):
        """test"""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        """test"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        """test"""
        place = Place()
        sleep(0.05)
        first_updated_at = place.updated_at
        place.save()
        self.assertLess(first_updated_at, place.updated_at)

    def test_two_saves(self):
        """test"""
        place = Place()
        sleep(0.05)
        first_updated_at = place.updated_at
        place.save()
        second_updated_at = place.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        place.save()
        self.assertLess(second_updated_at, place.updated_at)

    def test_save_with_arg(self):
        """test"""
        place = Place()
        with self.assertRaises(TypeError):
            place.save(None)

    def test_save_updates_file(self):
        """test"""
        place = Place()
        place.save()
        place_id = "Place." + place.id
        with open("file.json", "r") as f:
            self.assertIn(place_id, f.read())


class TestPlaceToDict(unittest.TestCase):
    """Unittests for testing to_dict method of the Place class."""

    def test_to_dict_type(self):
        """Test if the return type of to_dict() is a dictionary."""
        self.assertTrue(dict, type(Place().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """Test if the dictionary returned by to_dict()
        contains the correct keys."""
        place = Place()
        self.assertIn("id", place.to_dict())
        self.assertIn("created_at", place.to_dict())
        self.assertIn("updated_at", place.to_dict())
        self.assertIn("__class__", place.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """Test if the dictionary returned by to_dict()
        contains added attributes."""
        place = Place()
        place.middle_name = "Holberton"
        place.my_number = 98
        self.assertEqual("Holberton", place.middle_name)
        self.assertIn("my_number", place.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """Test if the datetime attributes in the dictionary
        returned by to_dict() are strings."""
        place = Place()
        place_dict = place.to_dict()
        self.assertEqual(str, type(place_dict["id"]))
        self.assertEqual(str, type(place_dict["created_at"]))
        self.assertEqual(str, type(place_dict["updated_at"]))

    def test_to_dict_output(self):
        """Test the output of to_dict() method."""
        dt = datetime.today()
        place = Place()
        place.id = "123456"
        place.created_at = place.updated_at = dt
        expected_dict = {
            'id': '123456',
            '__class__': 'Place',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(place.to_dict(), expected_dict)

    def test_contrast_to_dict_dunder_dict(self):
        """Test if the dictionary returned by to_dict() is
        different from the __dict__ attribute."""
        place = Place()
        self.assertNotEqual(place.to_dict(), place.__dict__)

    def test_to_dict_with_arg(self):
        """Test if to_dict() raises a TypeError when called
        with an argument."""
        place = Place()
        with self.assertRaises(TypeError):
            place.to_dict(None)


if __name__ == "__main__":
    unittest.main()
