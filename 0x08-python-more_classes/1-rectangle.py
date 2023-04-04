#!/usr/bin/python3
"""A class that defines a rectangle"""

class Rectangle:
    """this represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing this rectangle class
        Args:
            width: represent the width of the rectangle
            height: represents the height of the rectanglr
        Raises:
            TypeError: if size is not integer
            ValueError: if siz is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves width attribute"""
        return self.__width

    @width.setter
    def width(self):
        """sets width attribbute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
     def height(self):
         """retrieves height attribute"""
         return self.__height
     
     @height.setter
     def height(self, value):
         """sets height attribute"""
         if not isinstance(value, int):
             raise TypeError("height must be an integer")
         if value < 0:
             raise ValueError("height must be >= 0")
         self.__height = value
