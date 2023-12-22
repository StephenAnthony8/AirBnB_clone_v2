#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float

class Place(BaseModel):
    """ Pace - Contains city_id, user_id, name, description, \
        number_rooms, number_bathrooms, max_guest, price_by_night, \
            latitude & longitude"""
    __tablename__ = 'places'

    # this entire block has an issue
    
    #city_id = Column(ForeignKey('cities.id'), String(128), nullable=False)
    #user_id = Column(ForeignKey('users.id'), String(128), nullable=False)
    """ name = "" # Column(String(128), nullable=False)
    description = "" # Column(String(128), nullable=False)
    number_rooms = "" # Column(Integer, nullable=False, default=0)
    number_bathrooms = "" # Column(Integer, nullable=False, default=0)
    max_guest ="" # Column(Integer, nullable=False, default=0)
    price_by_night = "" # Column(Integer, nullable=False, default=0)
    latitude = "" # Column(Float, nullable=False, default=0)
    longitude = "" # Column(Float, nullable=False, default=0)
    # amenity_ids = [] """
