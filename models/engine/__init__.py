#!/usr/bin/python3
"""
This is the initialization file for the web_flask package.
It sets up the Flask application and configures
the necessary routes and settings.
"""
import os
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

# Choose storage type based on environment variable
storage_type = os.getenv('HBNB_TYPE_STORAGE')

if storage_type == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
