import pytest


@pytest.fixture
def user():
    print("\nSetting up user...")
    return {
        "name": "Gabby",
        "role": "admin"
    }


def test_user_name(user):
    assert user["name"] == "Gabby"


def test_user_role(user):
    assert user["role"] == "admin"