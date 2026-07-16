""" import pytest


@pytest.fixture(scope="module")
def user():
    print("\nSetting up user...")

    yield {
        "name": "Gabby",
        "role": "admin"
    }

    print("Cleaning up user...")


def test_username(user):
    assert user["name"] == "Gabby"


def test_role(user):
    assert user["role"] == "admin" """