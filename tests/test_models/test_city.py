#!/usr/bin/python3
"""Defines unittests for models/city.py.

Unittest classes:
    TestCityInstantiation
    TestCitySave
    TestCityToDict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCityInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the City class."""

    def test_no_args_instantiates(self):
        """Test that City class can be instantiated with no arguments."""
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        """Test that a new instance of City is stored
        in the objects dictionary of models.storage."""
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Test that the id attribute of City is of type str."""
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        """Test that the created_at attribute of City is of type datetime."""
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        """Test that the updated_at attribute of City is of type datetime."""
        self.assertEqual(datetime, type(City().updated_at))

    def test_name_is_public_str(self):
        """Test that the name attribute of City is of type str."""
        self.assertEqual(str, type(City.name))

    def test_state_id_is_public_str(self):
        """Test that the state_id attribute of City is of type str."""
        self.assertEqual(str, type(City.state_id))

    def test_two_cities_unique_ids(self):
        """Test that two instances of City have unique ids."""
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_two_cities_created_at(self):
        """Test that two instances of City have
        different created_at timestamps."""
        city1 = City()
        sleep(0.05)
        city2 = City()
        self.assertLess(city1.created_at, city2.created_at)

    def test_two_cities_different_updated_at(self):
        """Test that two instances of City have
        different updated_at timestamps."""
        city1 = City()
        sleep(0.05)
        city2 = City()
        self.assertLess(city1.updated_at, city2.updated_at)

    def test_str_representation(self):
        """Test the string representation of City."""
        dt = datetime.today()
        dt_repr = repr(dt)
        city = City()
        city.id = "123456"
        city.created_at = city.updated_at = dt
        city_str = city.__str__()
        self.assertIn("[City] (123456)", city_str)
        self.assertIn("'id': '123456'", city_str)
        self.assertIn("'created_at': " + dt_repr, city_str)
        self.assertIn("'updated_at': " + dt_repr, city_str)

    def test_args_unused(self):
        """Test that passing None as an argument
        to City does not affect the instance attributes."""
        city = City(None)
        self.assertNotIn(None, city.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Test that City can be instantiated with keyword arguments."""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        city = City(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(city.id, "345")
        self.assertEqual(city.created_at, dt)
        self.assertEqual(city.updated_at, dt)

    def test_instantiation_None_kwargs(self):
        """Test that passing None as keyword
        arguments to City raises a TypeError."""
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


class TestCitySave(unittest.TestCase):
    """Unittests for testing save method of the City class."""

    @classmethod
    def setUpClass(cls):
        """Set up for all tests in the class."""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        """Clean up after each test."""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        """Test that updating an instance of
        City updates the updated_at attribute."""
        city = City()
        sleep(0.05)
        first_updated_at = city.updated_at
        city.save()
        self.assertLess(first_updated_at, city.updated_at)

    def test_two_saves(self):
        """Test that updating an instance of
        City updates the updated_at attribute."""
        city = City()
        sleep(0.05)
        first_updated_at = city.updated_at
        city.save()
        second_updated_at = city.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        city.save()
        self.assertLess(second_updated_at, city.updated_at)

    def test_save_with_arg(self):
        """Test that passing an argument to save raises a TypeError."""
        city = City()
        with self.assertRaises(TypeError):
            city.save(None)

    def test_save_updates_file(self):
        """Test that updating an instance
        of City updates the file.json file."""
        city = City()
        city.save()
        city_id = "City." + city.id
        with open("file.json", "r") as f:
            self.assertIn(city_id, f.read())


class TestCityToDict(unittest.TestCase):
    """Unittests for testing to_dict method of the City class."""

    def test_to_dict_type(self):
        """Test if the return type of to_dict() is a dictionary."""
        self.assertTrue(dict, type(City().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """Test if the dictionary returned by
        to_dict() contains the correct keys."""
        city = City()
        self.assertIn("id", city.to_dict())
        self.assertIn("created_at", city.to_dict())
        self.assertIn("updated_at", city.to_dict())
        self.assertIn("__class__", city.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """Test if the dictionary returned by
        to_dict() contains added attributes."""
        city = City()
        city.middle_name = "Holberton"
        city.my_number = 98
        self.assertEqual("Holberton", city.middle_name)
        self.assertIn("my_number", city.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """Test if the datetime attributes
        in the dictionary returned by to_dict() are strings."""
        city = City()
        city_dict = city.to_dict()
        self.assertEqual(str, type(city_dict["id"]))
        self.assertEqual(str, type(city_dict["created_at"]))
        self.assertEqual(str, type(city_dict["updated_at"]))

    def test_to_dict_output(self):
        """Test the output of to_dict() against the expected dictionary."""
        dt = datetime.today()
        city = City()
        city.id = "123456"
        city.created_at = city.updated_at = dt
        expected_dict = {
            'id': '123456',
            '__class__': 'City',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(city.to_dict(), expected_dict)

    def test_contrast_to_dict_dunder_dict(self):
        """Test to_dict method against instance __dict__."""
        city = City()
        self.assertNotEqual(city.to_dict(), city.__dict__)

    def test_to_dict_with_arg(self):
        """Test to_dict method with an argument."""
        city = City()
        with self.assertRaises(TypeError):
            city.to_dict(None)


if __name__ == "__main__":
    unittest.main()
