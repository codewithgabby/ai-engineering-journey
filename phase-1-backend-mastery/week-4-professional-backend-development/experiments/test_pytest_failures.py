"""
Day 18 Experiment
Topic: Understanding Failing Tests with pytest

Goal:
Learn how pytest reports failed assertions and how engineers
use those reports to debug applications.
"""


def add(a, b):
    return a + b


def test_add_two_numbers():
  
    assert add(2, 3) == 6

########################################################  

def add(a, b):
    return a + b


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_zero():
    assert add(5, 0) == 5


def test_add_negative_numbers():
    assert add(-2, -3) == -5