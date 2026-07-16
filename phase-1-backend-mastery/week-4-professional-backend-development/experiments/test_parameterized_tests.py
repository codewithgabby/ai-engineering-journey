""" import pytest


def multiply(a, b):
    return a * b


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),
        (4, 5, 20),
        (10, 0, 0),
        (-2, 5, -10),
        (-3, -2, 6),
    ]
)
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected """