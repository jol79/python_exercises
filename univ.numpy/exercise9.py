import numpy as np

"""
 solution using numpy
"""


def generator(start_from, quantity, step_size=3):
    array = []
    for value in np.arange(start_from, quantity, step_size):
        array.append(value)
    return array


first_array = generator(1, 30)
second_array = generator(2, 30)
third_array = generator(3, 30+1)
final_array = [first_array, second_array, third_array]

# print(final_array)

# alternative solution:
array1 = []
start = 1
quantity = 30
step = 3
position = 0

# using comprehensions
# array = [value for value in np.arange(start, quantity, step)]
for i in range(0, 3):
    for value in np.arange(start, quantity, step):
        array1.append(value)
    start += 1

# print(array1)

n = 3
a = [[i for i in np.arange(start, quantity, step)] for x in range(0, n)]
print(a)