import numpy as np

"""
 BMI = weight / height
    height - convert to meters(divide by 100)
    height = (height / 100) ** 2
"""
names = ["John", "Maria", "Poul", "Denis", "Alex",
         "Nikita", "Yuri", "Dmytro", "Pasha", "Ola"]

stats = np.array([np.random.randint(50, 100+1, size=10),
                  np.random.randint(150, 200+1, size=10)])


def bmi(height_arr, weight_arr):
    # convert height from CM to M
    converted_height = (height_arr[1]/100) ** 2

    # calc BMI regarding BMI formula
    return weight_arr / converted_height


def classifier(bmi_arr):
    identifier = []
    for element in bmi_arr:
        if element <= 18.5 <= 25:
            identifier.append("NORMAL")
        if element < 18.5:
            identifier.append("LEAN")
        if element > 25:
            identifier.append("FATTY")
    return identifier


bmi_array = bmi(stats, stats[0])
print(*zip(names, classifier(bmi_array)))
