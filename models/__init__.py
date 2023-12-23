#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os

# switch to commented for testing
storage_type = os.getenv('HBNB_TYPE_STORAGE', 'file')
# storage_type = 'db'
# Choose storage type based on the environment variable

if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()

else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
