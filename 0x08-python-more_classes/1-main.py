#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rect = Rectangle(2, 4)
print(my_rect.__dict__)

my_rect.width = 10
my_rect.height = 3
print(my_rect.__dict__)
