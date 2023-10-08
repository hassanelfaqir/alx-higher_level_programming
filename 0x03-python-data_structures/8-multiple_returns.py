#!/usr/bin/python3

def multiple_returns(sentence):
    """Returns the length of a string and its first character"""
    return (len(sentence), sentence[0] if len(sentence) > 0 else None)
