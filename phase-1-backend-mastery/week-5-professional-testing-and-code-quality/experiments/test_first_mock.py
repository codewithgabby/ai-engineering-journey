from unittest.mock import MagicMock


def process_payment(payment_gateway):
    response = payment_gateway.charge(5000)

    if response["status"] == "success":
        return "Subscription Activated"

    return "Payment Failed"


def test_successful_payment():
    fake_gateway = MagicMock()

    fake_gateway.charge.return_value = {
        "status": "success"
    }

    result = process_payment(fake_gateway)

    assert result == "Subscription Activated"


def test_failed_payment():
    fake_gateway = MagicMock()

    fake_gateway.charge.return_value = {
        "status": "failed"
    }

    result = process_payment(fake_gateway)

    assert result == "Payment Failed"