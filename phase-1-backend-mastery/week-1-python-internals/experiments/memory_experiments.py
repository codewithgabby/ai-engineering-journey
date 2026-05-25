# PYTHON MEMORY EXPERIMENTS
""" 
a = [1, 2, 3]

b = a

print(a)
print(b)

b.append(4)

print("a:", a)
print("b:", b) """

#####################

""" x = 10

y = x 

y = 20

print("x:", x)
print("y:", y) """

######################

""" a = [1, 2, 3]

b = a

print(a is b)

print(id(a))
print(id(b)) """

####################

""" a = [1, 2, 3]

b = [1, 2, 3]

print(a == b)

print(a is b)

print(id(a))
print(id(b)) """

###################

""" a = [1, 2, 3]

b = a.copy()

print(a == b)

print(a is b)

print(id(a))
print(id(b))

b.append(4)

print(a)
print(b) """

#####################

""" a = [[1, 2], [3, 4]]

b = a.copy()

b[0].append(99)

print(a)
print(b) """

#######################

""" import copy

a = [[1, 2], [3, 4]]

b = copy.deepcopy(a)

b[0].append(99)

print(a)
print(b) """

########################

def change_data(data):
    data.append(99)

numbers = [1, 2, 3]

change_data(numbers)

print(numbers)
