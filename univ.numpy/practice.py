import numpy as np

"""
 generates array with elements from range(1, 10)
"""
x = np.arange(1, 13)

# elements in x ** 2
square = x ** 2

"""
 x array in 2 dimensional presentation 
"""
two_dimensional = x.reshape(3, 4)
# print(two_dimensional)

"""
 build [[ 1 4 7 10 13 16 19 22 25 28]
        [ 2 5 8 11 14 17 20 23 26 29]
        [ 3 6 9 12 15 18 21 24 27 30]]
"""
y = np.arange(1, 31)
two_dimensional2 = y.reshape(10, 3)
# print(two_dimensional2.T)

"""
 np.array() to create multidimensional array from defined shapes(common arrays)
 and it's content
"""
l1 = ['00', '01', '02', '03']
l2 = ['04', '05', '06', '07']

r_array = [l1, l2]
array = np.array(r_array)

"""
 [ 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 ]
"""
array = np.arange(0, 100, 10)
# will show the positions with true / false if value of that position > 40
# print(array > 40)
# will show the elements of array that is > 40
# print(array[array > 40])
# will show position of the array with true if value == 30
# print(array == 30)
# will show the value that is == 30
# print(array[array == 30])
array = np.arange(15)
# print("Even:", array[array % 2 == 0])
# print("Odd:", array[array % 2 != 0])

"""
 BMI = weight / height
    height - convert to meters(divide by 100)
    height = (height / 100) ** 2
"""
stats = np.array([np.random.randint(50, 100+1, size=10),
                  np.random.randint(150, 200+1, size=10)])

# print(stats)

"""
 iterate through array by index
"""
arr = [1, 2, "10", 12, 40, "56"]
index = 0

while index < len(arr):
    print("Element: {} with id = {}".format(arr[index], index))
    index += 1
