#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime

class State(BaseModel, Base):
    """ State class containing State name"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
