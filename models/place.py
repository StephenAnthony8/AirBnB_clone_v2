#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ Place - Place Object"""
    __tablename__ = 'places'

    city_id = Column(String(128), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(128), ForeignKey('users.id'),  nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(128))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, default=0)
    longitude = Column(Float, default=0)
    # amenity_ids = []

    # relationships

    cities = relationship('City', back_populates='places')
    user = relationship('User', back_populates='places')
