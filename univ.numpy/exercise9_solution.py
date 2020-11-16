import numpy as np


"""
 build [[ 1 4 7 10 13 16 19 22 25 28]
        [ 2 5 8 11 14 17 20 23 26 29]
        [ 3 6 9 12 15 18 21 24 27 30]]
"""
# using transposition to replace in different order
y = np.arange(1, 31).reshape(10, 3).T
print(y)
