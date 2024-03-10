#!/usr/bin/python3
"""unittest for models/user.py.
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUserInstantiation(unittest.TestCase):
    """Unittest for testing instantiation of the User class."""

    def test_no_args_instantiates(self):
        """Test that User can be instantiated with no arguments."""
        self.assertEqual(User, type(User()))

    def test_new_instance_stored_in_objects(self):
        """Test that a new instance of User is stored in objects."""
        self.assertIn(User(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Test that the id attribute of User is of type str."""
        self.assertEqual(str, type(User().id))

    def test_created_at_is_public_datetime(self):
        """Test that the created_at attribute of User is of type datetime."""
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_public_datetime(self):
        """Test that the updated_at attribute of User is of type datetime."""
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_public_str(self):
        """Test that the email attribute of User is of type str."""
        self.assertEqual(str, type(User.email))

    def test_password_is_public_str(self):
        """Test that the password attribute of User is of type str."""
        self.assertEqual(str, type(User.password))

    def test_first_name_is_public_str(self):
        """Test that the first_name attribute of User is of type str."""
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_public_str(self):
        """Test that the last_name attribute of User is of type str."""
        self.assertEqual(str, type(User.last_name))

    def test_two_users_unique_ids(self):
        """Test that two instances of User have unique ids."""
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_two_users_different_created_at(self):
        """Test that two instances of User have different created_at values."""
        user1 = User()
        sleep(0.05)
        user2 = User()
        self.assertLess(user1.created_at, user2.created_at)

    def test_two_users_different_updated_at(self):
        """Test that two instances of User have different updated_at values."""
        user1 = User()
        sleep(0.05)
        user2 = User()
        self.assertLess(user1.updated_at, user2.updated_at)

    def test_str_representation(self):
        """Test the string representation of User."""
        dt = datetime.today()
        dt_repr = repr(dt)
        user = User()
        user.id = "123456"
        user.created_at = user.updated_at = dt
        user_str = user.__str__()
        self.assertIn("[User] (123456)", user_str)
        self.assertIn("'id': '123456'", user_str)
        self.assertIn("'created_at': " + dt_repr, user_str)
        self.assertIn("'updated_at': " + dt_repr, user_str)

    def test_args_unused(self):
        """Test that passing None as argument does not affect User
        attributes."""
        user = User(None)
        self.assertNotIn(None, user.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Test instantiation of User with keyword arguments."""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        user = User(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(user.id, "345")
        self.assertEqual(user.created_at, dt)
        self.assertEqual(user.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        """Test instantiation of User with None as keyword arguments."""
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)


class TestUserSave(unittest.TestCase):
    """Unittest for testing save method of the User class."""

    @classmethod
    def setUpClass(cls):
        """test"""
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass

    def tearDown(self):
        """test"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("temp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        """test"""
        user = User()
        sleep(0.05)
        first_updated_at = user.updated_at
        user.save()
        self.assertLess(first_updated_at, user.updated_at)

    def test_two_saves(self):
        """test"""
        user = User()
        sleep(0.05)
        first_updated_at = user.updated_at
        user.save()
        second_updated_at = user.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        user.save()
        self.assertLess(second_updated_at, user.updated_at)

    def test_save_with_arg(self):
        """test"""
        user = User()
        with self.assertRaises(TypeError):
            user.save(None)

    def test_save_updates_file(self):
        """test"""
        user = User()
        user.save()
        user_id = "User." + user.id
        with open("file.json", "r") as f:
            self.assertIn(user_id, f.read())


class TestUserToDict(unittest.TestCase):
    """Unittests for testing to_dict method of the User class."""

    def test_to_dict_type(self):
        """Test if the return type of to_dict method is a dictionary."""
        self.assertTrue(dict, type(User().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """Test if the dictionary returned by to_dict method contains
        the correct keys."""
        user = User()
        self.assertIn("id", user.to_dict())
        self.assertIn("created_at", user.to_dict())
        self.assertIn("updated_at", user.to_dict())
        self.assertIn("__class__", user.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """Test if the dictionary returned by to_dict method contains
        the added attributes."""
        user = User()
        user.middle_name = "Hasan"
        user.my_number = 20
        self.assertEqual("Hasan", user.middle_name)
        self.assertIn("my_number", user.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """Test if the datetime attributes in the dictionary returned by
        to_dict method are strings."""
        user = User()
        user_dict = user.to_dict()
        self.assertEqual(str, type(user_dict["id"]))
        self.assertEqual(str, type(user_dict["created_at"]))
        self.assertEqual(str, type(user_dict["updated_at"]))

    def test_to_dict_output(self):
        """Test the output of the to_dict method."""
        dt = datetime.today()
        user = User()
        user.id = "123456"
        user.created_at = user.updated_at = dt
        expected_dict = {
            'id': '123456',
            '__class__': 'User',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(user.to_dict(), expected_dict)

    def test_contrast_to_dict_dunder_dict(self):
        """Test if the dictionary returned by to_dict method is different
        from the __dict__ attribute."""
        user = User()
        self.assertNotEqual(user.to_dict(), user.__dict__)

    def test_to_dict_with_arg(self):
        """Test if to_dict method raises a TypeError when called
        with an argument."""
        user = User()
        with self.assertRaises(TypeError):
            user.to_dict(None)


if __name__ == "__main__":
    unittest.main()
