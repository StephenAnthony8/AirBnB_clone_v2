#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id', ondelete='CASCADE'), nullable=False)

    # child reference to State
    state = relationship(
        "State",
        back_populates="cities"
    )

    # parent reference to Place
    places = relationship(
        "Place",
        cascade="all, delete",
        passive_deletes=True,
        back_populates="cities"
    )
