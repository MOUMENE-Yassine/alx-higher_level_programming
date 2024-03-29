#!/usr/bin/python3
"""Defines a square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square"""

    def __init__(self, size, x=0, y=0, identifier=None):
        """Initialize a new Square"""
        super().__init__(size, size, x, y, identifier)

    @property
    def size(self):
        """Get/set the size of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """Return the print() and str() representation of a Square"""
        str_square = f"[{self.__class__.__name__}] "
        identifier = f"({self.id}) "
        x_y = f"{self.x}/{self.y} - "
        size = f"{self.size}"
        return str_square + identifier + x_y + size

    def update(self, *args, **kwargs):
        """Update the Square"""
        if args is not None and len(args) > 0:
            keys = ['id', 'size', 'x', 'y']
            for key, value in zip(keys, args):
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)
        elif kwargs is not None and len(kwargs) > 0:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    if key == 'size':
                        setattr(self, 'width', value)
                        setattr(self, 'height', value)
                    else:
                        setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the Square"""
        return {k: self.getatt(k) for k in ['id', 'size', 'x', 'y']}

    def getatt(self, k):
        """ Returns attributes """
        return getattr(self, 'width') if k == 'size' else getattr(self, k)
