#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Unit test class for testing the `max_integer()` function.
    """
    def test_should_return_None(self):
        """
        Test that `max_integer()`
        should return None when called with no arguments.
        """
        self.assertEqual(max_integer(), None)

    def test_normal_arguments(self):
        """
        Test that `max_integer()`
        correctly identifies the maximum integer in a list
        when called with a list of integers and floats.
        """
        self.assertEqual(max_integer([3]), 3)
        self.assertEqual(max_integer([3, 2, 1]), 3)
        self.assertEqual(max_integer([3, 1, 4.5]), 4.5)
        self.assertEqual(max_integer([-3, -1, -4.5]), -1)
        self.assertEqual(max_integer([0, 3, -4.5]), 3)
        self.assertEqual(max_integer([0.1, 0.2, 0.3]), 0.3)

    def test_errors(self):
        """
        Test that `max_integer()` raises a TypeError when called with arguments
        that are not iterable.
        """
        with self.assertRaises(TypeError):
            max_integer(None)
        with self.assertRaises(TypeError):
            max_integer({"abcd"})
        with self.assertRaises(TypeError):
            max_integer(max_integer(2, 3, 5))

    def test_weird_arg(self):
        """
        Test if the max_integer() function correctly handles unusual arguments.
        """
        self.assertEqual(max_integer("abcd"), "d")
        self.assertEqual(max_integer((2, 3, 5)), 5)
