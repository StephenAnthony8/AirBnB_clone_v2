#!/usr/bin/python3
"""This module defines a class User"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        # parent reference to Place
        places = relationship(
            "Place",
            cascade="all, delete",
            passive_deletes=True,
            back_populates="user"
        )

        # parent reference to Review
        reviews = relationship(
            "Review",
            cascade="all, delete",
            passive_deletes=True,
            back_populates="user"
        )
