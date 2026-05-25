""" def calculate_total(price: float, quantity: int) -> float:
    return price * quantity


result = calculate_total(99.99, 3)

print(result) """

########################

""" def create_user(name: str, age: int, is_admin: bool) -> dict:
    return {
        "name": name,
        "age": age,
        "is_admin": is_admin
    }


user = create_user("Gabby", 25, False)

print(user) """

################################# 

""" def process_order(
    customer_name: str,
    total_amount: float,
    is_paid: bool = False
) -> dict:

    return {
        "customer": customer_name,
        "amount": total_amount,
        "paid": is_paid
    }


order = process_order("Gabby", 25000.0)

print(order) """

#################################

from typing import List


def calculate_average(numbers: List[int]) -> float:
    return sum(numbers) / len(numbers)


result = calculate_average([10, 20, 30])

print(result)