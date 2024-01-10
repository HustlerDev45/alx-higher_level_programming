#!/usr/bin/python3
"""Defines a function that returns the dictionary description."""


def class_to_json(obj):
    """Returns the dictionnary with simple data structure."""
    return obj.__dict__
