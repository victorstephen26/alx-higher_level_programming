#!/usr/bin/python3
"""
This module contains a fucntion that prints a name
"""


def say_my_name(first_name, last_name=""):
    '''This function prints name (<first name>)
    Args:
        first_name (str): The first name to be printed
        last_name (str): The last numbr to be printed
    Raises:
        TypeError: If either the first_name and last_name are not strings
    '''

    if not isinstance(first_name, str):
        raise TypeError("first_name must be string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be string")
    print(f"My name is {first_name} {last_name}")
