# ==========================================
# ITERATORS
# ==========================================

""" numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator)) """

#################################3

""" numbers = [1, 2, 3]

for item in numbers:
    print(item) """

# ==========================================
# GENERATORS
# ==========================================

""" def generate_numbers():

    yield 1
    yield 2
    yield 3


numbers = generate_numbers()

print(next(numbers))
print(next(numbers))
print(next(numbers)) """

#############################

""" def infinite_counter():

    number = 1

    while True:

        yield number

        number += 1


counter = infinite_counter()

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter)) """

# ==========================================
# LARGE FILE STREAMING SIMULATION
# ==========================================

def read_large_file():

    for number in range(1, 6):

        yield f"Processing line {number}"


file_reader = read_large_file()

for line in file_reader:
    print(line)