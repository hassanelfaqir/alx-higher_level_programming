#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """print the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
