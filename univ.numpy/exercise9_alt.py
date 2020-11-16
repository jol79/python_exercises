import numpy as np
start = 1
quantity = 30
step = 3
n = 3
a = [[i for i in np.arange(start, quantity, step)] for x in range(0, n)]
print(a)

# a = []
# for x in range(0, n):
#     for i in np.arange(start, quantity, step):
#         a.append(i)
#     start += 1