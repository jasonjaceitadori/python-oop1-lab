#!/usr/bin/env python3

class Book:
    """Represents a book with a title and page count."""

    def __init__(self, title, page_count):
        self.title = title
        self._page_count = None
        self.page_count = page_count

    @property
    def page_count(self):
        """Return the current page count."""
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        """Validate page_count input and store it if it is an integer."""
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        """Simulate turning a page in the book."""
        print("Flipping the page...wow, you read fast!")
