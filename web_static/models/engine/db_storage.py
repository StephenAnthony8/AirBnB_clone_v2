#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from sqlalchemy import create_engine
import os

class DBStorage:
    """This class manages storage of hbnb models in databases"""
    __engine = None
    __session = None

    def __init__(self):

        #engine creation parameters
        dialect = "mysql"
        driver = "mysqldb"
        user = os.environ.get('HBNB_MYSQL_USER')
        pwd = os.environ.get('HBNB_MYSQL_PWD')
        host = os.environ.get('HBNB_MYSQL_HOST')
        database = os.environ.get('HBNB_MYSQL_DB')

        #engine creation string
        database_url = f"{dialect}+{driver}://{user}:{pwd}@{host}/{database}"

        self.__engine = create_engine(database_url, pool_pre_ping=True)

    def all(self, cls=None):
        """Queries on the current database section all / specifiec objects"""
        ...

    def new(self, obj):
        """add obj to the current database session"""
        ...
    
    def save(self):
        """Commit all changes of the current database session"""
        ...
    
    def delete(self, obj=None):
        """delete current object from the database session if not None"""
        ...
    
    def reload(self):
        """create all tables in the current database session"""
        # using the sessionmaker option
        # expire on commit option must be set to False
        # ensure Session is thread-safe 