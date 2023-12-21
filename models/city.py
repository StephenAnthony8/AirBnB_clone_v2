#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime


class City(BaseModel):
    """ The city class, contains state ID and name """
    state_id = ""
    name = ""
