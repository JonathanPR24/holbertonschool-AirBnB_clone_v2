#!/usr/bin/pyhton3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    # Relationship with the Place class
    places = relationship('Place', backref=backref(
        'user', cascade='all, delete-orphan'))

    # Relationship with the Review class
    reviews = relationship('Review', backref=backref(
        'user', cascade='all, delete-orphan'))

    class Place(BaseModel, Base):
        """ A place to stay """
        __tablename__ = 'places'

        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)

        # Relationship with the User class
        user = relationship('User', backref=backref(
            'places', cascade='all, delete-orphan'))

        # Relationship with the Review class
        reviews = relationship(
            'Review',
            backref=backref('place', cascade='all, delete-orphan'),
            cascade='all, delete-orphan'
        )


class Review(BaseModel, Base):
    """ Review class to store review information """
    __tablename__ = 'reviews'
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    # Relationship with the User class
    user = relationship('User', backref=backref(
        'reviews', cascade='all, delete-orphan'))