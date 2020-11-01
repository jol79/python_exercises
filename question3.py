"""
 add key/value pairs into dict with given number
 between 1 and n(with both included)
 e.g. inp = 8
    >>> {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
"""

# custom class with init and add methods
class my_dict(dict):
    # initializing dict data type:
    def __init__(self):
        self = dict()

    # add method:
    def add(self, key, value): 
        self[key] = value

dictionary = my_dict()

def integral(n):
    for inp in range(1, n+1):
        dictionary.add(inp, inp * inp)
    return dictionary

# print(integral(8))


###
# alternative without overriding dict class
###
def integral_alternative(inp=8):
    dictionary2 = dict()
    for number in range(1, inp+1):
        dictionary2[number] = number * number
    return dictionary2

print(integral_alternative())
