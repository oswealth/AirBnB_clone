#!/usr/bin/python3

"""the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User.

    Attributes:
        password (str): The password of the user.
        email (str): The email of the user.
        last_name (str): The last name of the user.
        first_name (str): The first name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
