#!/usr/bin/python3
"""Unittests for models/base_model.py

Unittests:
    TestBaseModel_instantiation
    TestBaseModel_to_dict
    TestBaseModel_save
"""

import os
import sys
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Test BaseModel instantiation."""

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_new_instances_have_different_ids(self):
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_two_new_instances_have_different_created_at(self):
        instance1 = BaseModel()
        sleep(0.05)
        instance2 = BaseModel()
        self.assertNotEqual(instance1.created_at, instance2.created_at)

    def test_two_new_instances_have_different_updated_at(self):
        instance1 = BaseModel()
        sleep(0.05)
        instance2 = BaseModel()
        self.assertNotEqual(instance1.updated_at, instance2.updated_at)

    def test_one_arg_instantiates(self):
        self.assertEqual(str, type(BaseModel("Betty")))

    def test_two_args_instantiates(self):
        self.assertEqual(str, type(BaseModel("Betty", 12)))

    def test_passing_kwargs_instantiates(self):
        self.assertEqual(str, type(BaseModel(name="Betty", age=12)))

    def test_passing_kwargs_stored_as_attributes(self):
        instance = BaseModel(name="Betty", age=12)
        self.assertEqual("Betty", instance.name)
        self.assertEqual(12, instance.age)

    def test_str_magic_method(self):
        instance = BaseModel()
        self.assertEqual(str, type(instance.__str__()))

    def test_args_unused(self):
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)


class TestBaseModel_to_dict(unittest.TestCase):
    """Test BaseModel to_dict method."""

    def test_to_dict_type(self):
        self.assertEqual(dict, type(BaseModel().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertIn("id", bm_dict)
        self.assertIn("created_at", bm_dict)
        self.assertIn("updated_at", bm_dict)
        self.assertIn("__class__", bm_dict)

    def test_to_dict_contains_added_attribute(self):
        bm = BaseModel()
        bm.name = "Hasan"
        bm_dict = bm.to_dict()
        self.assertEqual("Hasan", bm_dict['name'])

    def test_to_dict_datetime_is_str(self):
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(str, type(bm_dict['created_at']))
        self.assertEqual(str, type(bm_dict['updated_at']))

    def test_to_dict_class_key_value(self):
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual("BaseModel", bm_dict["__class__"])

    def test_to_dict_output(self):
        bm = BaseModel()
        bm.id = "123"
        bm.created_at = datetime(2000, 1, 1, 0, 0, 0, 0)
        bm.updated_at = datetime(2000, 1, 1, 0, 0, 0, 0)
        expected = {
            'id': '123',
            '__class__': 'BaseModel',
            'created_at': '2000-01-01T00:00:00',
            'updated_at': '2000-01-01T00:00:00'
        }
        self.assertDictEqual(bm.to_dict(), expected)

    def test_contrast_to_dict_dunder_dict(self):
        bm = BaseModel()
        self.assertNotEqual(bm.to_dict(), bm.__dict__)

    def test_to_dict_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict(None)


"""Test BaseModel save method."""


if __name__ == "__main__":
    unittest.main()
