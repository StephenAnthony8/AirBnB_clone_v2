#!/usr/bin/python3
"""Module defines the DBStorage class for db storage"""

import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class DBStorage:
    """Defines the DBStorage engine for database storage"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize the DBStorage engine"""
        db_user = os.getenv('HBNB_MYSQL_USER')
        db_pwd = os.getenv('HBNB_MYSQL_PWD')
        db_host = os.getenv('HBNB_MYSQL_HOST', 'localhost')
        db_name = os.getenv('HBNB_MYSQL_DB')
        db_env = os.getenv('HBNB_ENV', 'production')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.
            format(db_user, db_pwd, db_host, db_name),
            pool_pre_ping=True
        )

        if db_env == 'test':
            Base.metadata.drop_all(self.__engine)

        self.__session = scoped_session(sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
        ))

    def all(self, cls=None):
        """Query objects from the db based on class name"""
        objects_dict = {}
        classes = [User, State, City, Amenity, Place, Review]

        if cls:
            classes = [cls]

        for c in classes:
            query_result = self.__session.query(c).all()
            for obj in query_result:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objects_dict[key] = obj

        return objects_dict

    def new(self, obj):
        """Add the object to the current db session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Create all tables in the db
        Create the current db session
        """
        Base.metadata.create_all(self.__engine)
