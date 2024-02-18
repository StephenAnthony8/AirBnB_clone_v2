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

    # Parent reference to City
    cities = relationship(
        "City",
        cascade="all, delete",
        passive_deletes=True,
        back_populates='state'
        )

