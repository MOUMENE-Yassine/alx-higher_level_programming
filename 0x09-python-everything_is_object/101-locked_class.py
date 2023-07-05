#!/usr/bin/python3
"""prevents the user from dynamically creating"""

class LockedClass():
    """prevents the user from dynamically attributes creating"""
    __slots__ = ['first_name']

    def __init__(self):
        
        pass
