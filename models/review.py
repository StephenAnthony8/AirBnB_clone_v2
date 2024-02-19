#!/usr/bin/python3
""" Review module for the HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """ Review classto store review information """

    __tablename__ = 'reviews'
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60),
                      ForeignKey('places.id'),
                      nullable=False)#, ondelete='CASCADE'

    user_id = Column(String(60),
                     ForeignKey('users.id'),
                     nullable=False)#, ondelete='CASCADE'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        # child reference to User
        user = relationship(
            "User",
            back_populates="reviews"
        )

        # child reference to Place
        place = relationship(
            "Place",
            back_populates="reviews"
        )
