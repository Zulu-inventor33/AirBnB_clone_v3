#!/usr/bin/python3
"""A module that creates a User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class to manage user objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
