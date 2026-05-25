# ==========================================
# FIRST-CLASS FUNCTIONS
# ==========================================

""" def greet():
    print("Hello Engineer")


say_hello = greet

say_hello()


def execute_function(func):
    func()


execute_function(greet) """

#############################

""" def create_multiplier(number):

    def multiplier(x):
        return x * number

    return multiplier


times_3 = create_multiplier(3)

print(times_3(5)) """

# ==========================================
# SIMPLE DECORATOR
# ==========================================

""" def logger(func):

    def wrapper():
        print("Function is about to run")

        func()

        print("Function finished running")

    return wrapper


@logger
def greet():
    print("Hello Engineer")


greet() """

# ==========================================
# DECORATOR WITH ARGUMENTS
# ==========================================

""" def log_message(message):

    def decorator(func):

        def wrapper():

            print(f"[LOG]: {message}")

            func()

        return wrapper

    return decorator


@log_message("Starting greeting function")
def greet():
    print("Hello Engineer")


greet() """

# ==========================================
# PROFESSIONAL DECORATOR
# ==========================================

def logger(func):

    def wrapper(*args, **kwargs):

        print("Function started")

        result = func(*args, **kwargs)

        print("Function finished")

        return result

    return wrapper


@logger
def add_numbers(a, b):
    return a + b


print(add_numbers(5, 10))