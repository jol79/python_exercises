import numpy as np
import random as rd

"""
 BMI = weight / sqrt(height)
"""
names = ["John", "Maria", "Poul", "Denis", "Alex"]

array = [[rd.randint(150, 200), rd.randint(50, 100)] for length in range(0, 5)]
bmi = []

print("length of an array: {}".format(len(array)))

i = 0
for el in range(0, len(array)):
    for block in array[i]:
        print("block with id: {} and the block: {}".format(i, block))
        # result =
        # bmi.append()
    i += 1

print(array)
print("BMI: {}".format(bmi))
