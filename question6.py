"""
 calc Q = sqrt((2 * C * D) / H)
 d should be *args (>=1 can be printed)
"""
from math import sqrt 

def calc_smth(d):
    c = 50 
    h = 30

    q = sqrt((2 * c * d) / h)
    return int(q)


# containers for elements
input_elements = []
output_elements = []

qunt = int(input("How many elements should be added: "))
for el in range(0, qunt):
    element = int(input("Provide number to work with: "))
    input_elements.append(element)
    output_elements.append(calc_smth(element))

print("Start elements sequnce: {}".format(input_elements))
print("Exit elements sequnce: {}".format(output_elements))


"""
 Alternative solution:
"""
# import math

# c = 50
# h = 30 
# value = []
# items = [x for x in input().split(',')]

# for d in items:
#     value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

# print(','.join(value))