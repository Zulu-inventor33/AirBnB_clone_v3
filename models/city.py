#!/usr/bin/python3
"""This will hold class City"""
import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import ForeignKey
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """The Representation of city """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'cities'
        name = Column(String(128),
                      nullable=False)
        state_id = Column(String(60),
                          ForeignKey('states.id'),
                          nullable=False)
        places = relationship("Place",
                              backref="cities",
                              cascade="all, delete-orphan")
    else:
        name = ""
        state_id = ""

    def __init__(self, *args, **kwargs):
        """initializes a city"""
        super().__init__(*args, **kwargs)
