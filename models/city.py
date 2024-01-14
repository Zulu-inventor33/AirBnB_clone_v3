#!/usr/bin/python3
"""This module creates a city class"""

from models.base_model import BaseModel


class City(BaseModel):
    """The Class is for managing city objects"""

    state_id = ""
    name = ""
