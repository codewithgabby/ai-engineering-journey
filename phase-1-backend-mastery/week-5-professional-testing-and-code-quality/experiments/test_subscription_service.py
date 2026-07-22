from unittest.mock import MagicMock


def activate_subscription(payment_gateway):
    response = payment_gateway.charge()

    if response["status"] == "success":
        return {
            "success": True,
            "message": "Subscription Activated",
            "reference": response["reference"],
            "amount": response["amount"]
        }

    return {
        "success": False,
        "message": "Payment Failed"
    }


def test_subscription_success():
    fake_gateway = MagicMock()

    fake_gateway.charge.return_value = {
        "status": "success",
        "reference": "TXN123456",
        "amount": 5000
    }

    result = activate_subscription(fake_gateway)

    assert result["success"] is True
    assert result["message"] == "Subscription Activated"
    assert result["reference"] == "TXN123456"
    assert result["amount"] == 5000


def test_subscription_failure():
    fake_gateway = MagicMock()

    fake_gateway.charge.return_value = {
        "status": "failed"
    }

    result = activate_subscription(fake_gateway)

    assert result["success"] is False
    assert result["message"] == "Payment Failed"