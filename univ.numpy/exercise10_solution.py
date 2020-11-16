import numpy as np
import random as rd
from math import sqrt


names = ["John", "Maria", "Poul", "Denis", "Alex",
         "Nikita", "Mykyta", "Dmytro", "Pasha", "Ola"]

"""
 weight = random.randint(50, 100)
 height = random.randint(150, 200)
"""
# I can generate random values into 2 different arrays and then use array to complete 2 dimension array
# array = np.random.random().reshape(2, 10).T
height = np.random.randint(150, 200 + 1, size=(1, 10))
weight = np.random.randint(50, 100 + 1, size=(1, 10))

h_w = height, weight
array = np.array(h_w).T
# print("Weight | Height\n", array)


"""
 BMI = weight / height
    height - convert to meters(divide by 100)
    height = (height / 100) ** 2
"""


def bmi():
    global height_element, weight_element, sqrt_height
    sqrt_height = []

    for height_element in height:
        for weight_element in weight:
            print("Height element: {}\nWeight element: {}".format(height_element, weight_element))

    for h in height_element:
        sqrt_height.append((h / 100) ** 2)
    # print("Weights: ", weight_element, "\nHeights: ", height_element, "\nsqrt from heights: ", sqrt_height)
    return weight_element / sqrt_height


def fat_detector(arr):
    fat_array = []
    for elements in arr:
        if elements >= 18.5 <= 25:
            fat_array.append("Medium")
        elif elements < 18.5:
            fat_array.append("Drish")
        elif elements > 25:
            fat_array.append("Zurny")
    return fat_array


bmi_array = bmi()
bmi_result = fat_detector(bmi_array)
print(*zip(names, bmi_result))
