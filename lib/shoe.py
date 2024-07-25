#!/usr/bin/env python3
# lib/shoe.py
class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "New"

    # Brand property
    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not isinstance(value, str):
            raise ValueError("Brand must be a string")
        self._brand = value

    # Size property
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value

    # Cobble method
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
