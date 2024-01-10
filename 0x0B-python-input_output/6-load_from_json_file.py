#!/usr/bin/python3
"""Defines a function that creates an Object."""
import json


def load_from_json_file(filename):
    """Function that creates an Object from a “JSON file”.

        Returns:
            Object from the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.loads(f.read())
