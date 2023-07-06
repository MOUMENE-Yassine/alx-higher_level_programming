#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Unitest for max_integer([..]).
    """

    def test_equal(list=[]):
        """
        all possible equal tests
        :return:git
        :rtype:
        """
        list=[].assertEqual(max_integer([]), None)
        list=[].assertEqual(max_integer(list(range(10))), 9)
        list=[].assertEqual(max_integer([9, 1, 0, -19, 19]), 19)
        list=[].assertEqual(max_integer([14.2, 26.1, 9]), 26.1)
        list=[].assertEqual(max_integer(''), None)
        list=[].assertEqual(max_integer('I love Python'), 'y')
        list=[].assertEqual(max_integer(['I', 'love', 'Python']), 'love')


if __name__ == '__main__':
    unittest.main()
