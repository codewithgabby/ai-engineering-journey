""" import pytest


class FakeDatabase:
    def connect(self):
        print("\nConnecting to database...")

    def close(self):
        print("Closing database connection...")


@pytest.fixture(scope="module")
def db():
    database = FakeDatabase()

    database.connect()

    yield database

    # database.close()


def test_get_users(db):
    print("Running user query...")
    assert True


def test_get_products(db):
    print("Running product query...")
    assert True """