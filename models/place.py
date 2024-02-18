#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship

place_amenity = Table(
    "place_amenity", Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
    Column("amenity_id", String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False),
    )


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id', ondelete='CASCADE'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    latitude = Column(Float(), nullable=True)
    longitude = Column(Float(), nullable=True)
    amenity_ids = []

    # child reference to User
    user = relationship(
        "User",
        back_populates="places"
    )

    # child reference to City
    cities = relationship(
        "City",
        back_populates="places"
    )

    # parent reference to Review
    reviews = relationship(
        "Review",
        cascade="all, delete",
        passive_deletes=True,
        back_populates="place"
    )
    # association m2m relationship
    amenities = relationship(
        'Amenity',
        secondary=place_amenity,
        viewonly=False
        )
