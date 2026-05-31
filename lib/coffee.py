#!/usr/bin/env python3

class Coffee:
    """Represents a coffee item with size validation and tipping behavior."""

    ALLOWED_SIZES = ["Small", "Medium", "Large"]

    def __init__(self, size, price):
        self._size = None
        self._price = None
        self.size = size
        self.price = price

    @property
    def size(self):
        """Return the current coffee size."""
        return self._size

    @size.setter
    def size(self, value):
        """Validate the size to be Small, Medium, or Large."""
        if value in self.ALLOWED_SIZES:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    @property
    def price(self):
        """Return the current coffee price."""
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    def tip(self):
        """Add a tip to the coffee price and print a thank-you message."""
        print("This coffee is great, here’s a tip!")
        self.price = self.price + 1
