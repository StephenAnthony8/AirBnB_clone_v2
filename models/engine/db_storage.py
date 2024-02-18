#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""

from sqlalchemy import create_engine, MetaData
import os
from models.base_model import Base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.exc import NoSuchTableError, ArgumentError


class DBStorage:
    """Defines the DBStorage engine for database storage"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize the DBStorage engine"""

        dialect_driver = "mysql+mysqldb"

        # env variables
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST', 'localhost')
        dbase = os.getenv('HBNB_MYSQL_DB')
        env_var = os.getenv('HBNB_ENV', 'production')

        db_url = f'{dialect_driver}://{user}:{pwd}@{host}/{dbase}'

        # creation of engine
        self.__engine = create_engine(db_url, pool_pre_ping=True)

        # drop all tables if the environment variable is 'test'
        if os.getenv('HBNB_ENV') == 'test':
            metadata = MetaData()
            metadata.drop_all(self.__engine)

    def all(self, cls=None):  # Query objects from the db based on class name
        """Query objects from the db based on class name"""
        from models.base_model import Base
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review

        # self.reload() # ...will come back to this
        objects_dict = {}
        classes = [State, City, User, Place, Review, Amenity]

        if cls:
            if isinstance(cls, str) is False:
                cls = cls.__name__

            for cl_ass in classes:
                name = cl_ass.__name__
                if cl_ass.__name__ == cls:
                    classes = [cl_ass]

        for c in classes:
            try:
                query_result = self.__session.query(c).all()
                # print(dir(query_result))
                for obj in query_result:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    objects_dict[key] = obj
                query_result = []
            except NoSuchTableError:  # argument error for now
                continue

        return (objects_dict)

    def new(self, obj):  # Add the object to the current db session
        """Add the object to the current db session"""
        # Base.metadata.create_all(self.__engine) # return to this as well
        self.__session.add(obj)

    def save(self):  # Commit all changes of the current db session
        """Commit all changes of the current db session"""
        self.__session.commit()

    def reload(self):  # create all tables and current db session
        """
        Create all tables in the db
        Create the current db session
        """
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review

        # creation of tables in database
        Base.metadata.create_all(self.__engine)

        # creation of session (scoped session)
        self.__session = scoped_session(sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
        ))

    def delete(self, obj=None):  # delete from the current db session
        """Delete from the current database session"""
        if (obj):
            try:
                obj_name = f"{obj.__class__.__name__}.{obj.id}"
                dict_obj = self.all()
                if obj_name in dict_obj.keys():
                    self.__session.delete(obj)

            except AttributeError:
                return
