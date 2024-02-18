#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), primary_key=True, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""

        mandatories = ['id', 'created_at', 'updated_at']
        dict_mandatories = {
            'id': str(uuid.uuid4()),
            'created_at': datetime.now(),
            'updated_at': datetime.now()
        }
        # creates / updates instances with missing attributes
        if (kwargs):
            for k in mandatories:
                if k in kwargs.keys():
                    if k == 'id':
                        dict_mandatories[k] = kwargs[k]
                    else:
                        dict_mandatories[k] = datetime.strptime(
                            kwargs[k], '%Y-%m-%dT%H:%M:%S.%f'
                            )
                    del kwargs[k]

            if '__class__' in kwargs.keys():
                del kwargs['__class__']

        dict_mandatories.update(kwargs)
        self.__dict__.update(dict_mandatories)
        # ensure to check the save possibility of this class

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.to_dict())

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        if "_sa_instance_state" in dictionary.keys():
            del dictionary['_sa_instance_state']

        return dictionary

    def delete(self):
        """deletes itself from"""
        from models import storage
        storage.delete(self)
