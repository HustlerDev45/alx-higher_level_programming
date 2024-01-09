#!/usr/bin/python3
"""Legacy."""


class MyList(list):
    """Class that inherits from list."""
    
    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))
