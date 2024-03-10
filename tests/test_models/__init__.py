#!/usr/bin/python3
"""__init__ magic method for models directory"""

from models.engine.file_storage import FileStorage
"""
Reloading the FileStorage instance
"""
storage = FileStorage()
storage.reload()
