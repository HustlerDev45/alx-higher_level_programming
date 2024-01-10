#!/usr/bin/python3
"""Ddefines a class Student."""


class Student:
    """Defines a Student class."""

    def __init__(self, first_name, last_name, age):
        """Sets a Student instance with first_name, last_name, and age.

            Parameter:
                first_name (str): First name of the student.
                last_name (str): Last name of the student.
                age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a student instance."""
        return self.__dict__
