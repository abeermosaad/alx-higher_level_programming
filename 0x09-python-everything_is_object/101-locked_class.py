#!/usr/bin/python3
"""LockedClass"""


class LockedClass:
    """prevents the user from dynamically creating new instance attributes"""

    __slots__ = ["first_name", "last_name"]

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
