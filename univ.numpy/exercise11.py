"""
 create numpy array 3x10
 random elements, range(10, 20) both exclusive
"""
import numpy as np
from numpy import random


array = random.randint(10, 20+1, size=(3, 10))


def identifier(arr):
    for line in arr:
        for element in line:
            if element == 15:
                print("Searched element: {} | in line: {}".format(element, line))
            else:
                # print("element: {} | line: {}".format(element, line))
                pass
    return arr


print(identifier(array))
