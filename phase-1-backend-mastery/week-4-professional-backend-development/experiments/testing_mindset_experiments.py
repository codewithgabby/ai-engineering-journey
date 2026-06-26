"""
Day 16 Experiment
Topic: Testing Mindset

Goal:
Learn to think like a tester before learning pytest.
"""

# ==========================================
# Experiment 1
# Happy Path
# ==========================================

print("=== Happy Path ===")

balance = 10000
withdraw_amount = 2000

remaining_balance = balance - withdraw_amount

print(f"Remaining Balance: {remaining_balance}")

# Expected Output:
# Remaining Balance: 8000


# ==========================================
# Experiment 2
# Edge Case - Withdraw Too Much
# ==========================================

print("\n=== Edge Case: Insufficient Balance ===")

balance = 10000
withdraw_amount = 20000

if withdraw_amount > balance:
    print("Insufficient balance.")
else:
    print("Withdrawal successful.")


# ==========================================
# Experiment 3
# Edge Case - Negative Deposit
# ==========================================

print("\n=== Edge Case: Negative Deposit ===")

deposit = -500

if deposit <= 0:
    print("Invalid deposit amount.")
else:
    print("Deposit successful.")


# ==========================================
# Experiment 4
# Registration Test Cases
# ==========================================

print("\n=== Registration Test Cases ===")

test_cases = [
    {
        "email": "gabby@gmail.com",
        "password": "StrongPassword123",
        "expected": "Registration Successful"
    },
    {
        "email": "",
        "password": "StrongPassword123",
        "expected": "Email Required"
    },
    {
        "email": "gabbygmail.com",
        "password": "StrongPassword123",
        "expected": "Invalid Email Format"
    },
    {
        "email": "gabby@gmail.com",
        "password": "123",
        "expected": "Weak Password"
    }
]

for test in test_cases:
    print(test)