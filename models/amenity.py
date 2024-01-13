#!/usr/bin/python3

"""Defines the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """This stands for an amenity.

    Attributes:
        name (str): amenities name.
    """

    name = ""
