""" try:
    number = int(input("Enter number: "))
    answer = 100 / number
    print(answer)

except ZeroDivisionError:
    print("Cannot divide by zero.") """

###########################################

""" try:
    print("A")
    number = 10 / 0
    print("B")

except ZeroDivisionError:
    print("C")

print("D") """

##########################################

""" try:
    print("Start")
    age = int("hello")
    print("Middle")

except ValueError:
    print("Error")

print("Finish") """

##########################################

""" try:
    print("One")
    print("Two")
    number = int("50")
    print("Three")

except ValueError:
    print("Four")

print("Five") """

##########################################

""" try:
    print("A")
    age = int("25")
    print("B")

except ValueError:
    print("C")

print("D") """

###############################################

""" try:
    age = int(input("Age: "))

except ValueError:
    print("Please enter numbers only.")

else:
    print(f"You entered {age}") """

###########################################

""" try:
    print("Start")
    number = int("100")
    print("Middle")

except ValueError:
    print("Error")

else:
    print("Success")

print("Finish") """

#############################################

""" try:
    print("Opening database connection")
    print(10 / 2)

except ZeroDivisionError:
    print("Division failed")

finally:
    print("Closing database connection") """

#############################################

""" try:
    print("Opening database connection")
    print(10 / 0)

except ZeroDivisionError:
    print("Division failed")

finally:
    print("Closing database connection") """

##############################################

""" try:
    print("A")
    print(100 / 0)

except ZeroDivisionError:
    print("B")

finally:
    print("C")

print("D") """

################################################

""" try:
    balance = 1000
    amount = 5000

    if amount > balance:
        raise Exception("Insufficient balance.")

    print("Withdrawal successful.")

except Exception as e:
    print(e)

print("Program finished.") """

#################################################

""" try:
    age = 15

    if age < 18:
        raise Exception("Must be at least 18 years old.")

    print("Account created.")

except Exception as e:
    print(e)

print("End of program.") """

###################################################

class InsufficientBalanceError(Exception):
    pass


try:
    balance = 1000
    amount = 5000

    if amount > balance:
        raise InsufficientBalanceError(
            "Insufficient balance."
        )

    print("Withdrawal successful.")

except InsufficientBalanceError as e:
    print(e)

finally:
    print("Transaction finished.")