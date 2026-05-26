""" class User:

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email


user1 = User("Gabby", "gabby@gmail.com")

print(user1.name)
print(user1.email) """

##################################### 

""" class User:

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email


    def greet(self):
        print(f"Hello, {self.name}")


user1 = User("Gabby", "gabby@gmail.com")

user1.greet() """

#######################################

""" class BankAccount:

    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance


    def deposit(self, amount: float):
        self.balance += amount
        print(f"New balance: {self.balance}")


account1 = BankAccount("Gabby", 5000)

account1.deposit(2000) """

#####################################

class BankAccount:

    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance


    def deposit(self, amount: float):
        self.balance += amount
        print(f"New balance: {self.balance}")


    def withdraw(self, amount: float):

        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Remaining balance: {self.balance}")


account1 = BankAccount("Gabby", 5000)

account1.withdraw(2000)

