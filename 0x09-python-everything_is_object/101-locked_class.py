#!/usr/bin/python3
"""Define a lock class."""


class LockedClass:
    """
    Prevent the user from instantiating new LockClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
