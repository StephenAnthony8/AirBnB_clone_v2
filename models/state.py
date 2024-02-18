#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    # Parent reference to City
        cities = relationship(
            "City",
            cascade="all, delete",
            passive_deletes=True,
            back_populates='state'
            )

    def __init__(self, *args, **kwargs):
        """creates a state object saved to JSON"""
        super().__init__(**kwargs)

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """returns city objects with state_id equal to self.id"""
            from models import storage
            from models.city import City
            self.cities = []

            container = storage.all('City')
            for val in container.values():
                if val.state_id == self.id:
                    self.cities.append(val)
            return (val)