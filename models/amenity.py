#!/usr/bin/python3
""" Amenity Module for HBNB project """

from models.base_model import BaseModel
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel):
    '''class Amenity'''

    __tablename__ = 'amenities'
    name = Column(String(128))
    place_amenities = relationship(
        "Place", secondary='place_amenity', backref='amenities')
