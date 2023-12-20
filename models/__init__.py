#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage 

# Check the value of HBNB_TYPE_STORAGE environment variable
storage_type = os.getenv('HBNB_TYPE_STORAGE', 'file')

# Choose storage type based on the environment variable 
if storage_type == 'db': 
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
