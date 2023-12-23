#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from sqlalchemy.exc import NoSuchTableError
class DBStorage:
    """Defines the DBStorage engine for database storage"""

    __engine = None
    __session = None

    def __init__(self):
        
        """Initialize the DBStorage engine"""
        dialect = 'mysql'
        driver = 'mysqldb'
        user = 'hbnb_dev' #os.getenv('HBNB_MYSQL_USER')
        pwd = 'hbnb_dev_pwd' #os.getenv('HBNB_MYSQL_PWD')
        host = 'localhost' #os.getenv('HBNB_MYSQL_HOST', 'localhost')
        dbase = 'hbnb_dev_db' #os.getenv('HBNB_MYSQL_DB')
        db_env = os.getenv('HBNB_ENV', 'production')

        db_url = f'{dialect}+{driver}://{user}:{pwd}@{host}/{dbase}'

        self.__engine = create_engine(db_url, pool_pre_ping=True)

        self.__session = scoped_session(sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
        ))

    def all(self, cls=None): # Query objects from the db based on class name
        """Query objects from the db based on class name"""
        from models.base_model import Base
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review

        self.reload()
        objects_dict = {}
        classes = [User, State, City, Place, Amenity, Review]

        if cls:
            for cl_ass in classes:
                name = cl_ass.__name__
                if cl_ass.__name__ == cls:
                    classes = [cl_ass]

        for c in classes:
            try:
                query_result = self.__session.query(c).all()
                for obj in query_result:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    objects_dict[key] = obj
            except NoSuchTableError:
                continue

        return objects_dict
    
    def new(self, obj): # Add the object to the current db session
        """Add the object to the current db session"""
        Base.metadata.create_all(self.__engine)
        self.__session.add(obj)
    
    def save(self): # Commit all changes of the current db session
        """Commit all changes of the current db session"""
        self.__session.commit()

    def reload(self): # create all tables and current db session
        """
        Create all tables in the db
        Create the current db session
        """
        Base.metadata.create_all(self.__engine)
    
    def delete(self, obj=None): # delete from the current db session
        """Delete from the current database session"""
        if obj:
            self.__session.delete(obj)