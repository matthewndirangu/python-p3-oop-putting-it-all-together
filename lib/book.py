#!/usr/bin/env python3
# lib/book.py
class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    # Title property
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise ValueError("Title must be a string")
        self._title = value

    # Page count property
    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value

    # Turn page method
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
