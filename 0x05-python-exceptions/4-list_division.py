#!/usr/bin/python3

"""
    Divides element by element 2 lists.

    Return:
        A new list (list_length) with all division.
"""


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            div_result = my_list_1[i] / my_list_2[i]
        except (TypeError):
            print("wrong type")
            div_result = 0
        except (ZeroDivisionError):
            print("division by 0")
            div_result = 0
        except (IndexError):
            print("out of range")
            div_result = 0
        finally:
            new_list.append(div_result)
    return (new_list)
