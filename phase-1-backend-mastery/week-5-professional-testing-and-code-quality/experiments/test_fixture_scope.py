import pytest


@pytest.fixture(scope="module")
def user():
    print("\nCreating user...")
    return {
        "name": "Gabby",
        "role": "admin"
    }


def test_name(user):
    assert user["name"] == "Gabby"


def test_role(user):
    assert user["role"] == "admin"