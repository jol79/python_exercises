"""
 Takes 2 digits as input and generates a 2-dimensional
 array
"""

i = 3
j = 5

# matrix = [[rows] for rows in range(0, i)]

def gen_rows(data, inp = i):
    matrix = []

    for rows in range(0, inp):
        matrix.append(data)
        print("Here is columns {}".format(rows))
    return matrix

def gen_cols(inp = j):
    matrix = []

    for elements in range(0, inp):
        matrix.append(elements)
    return matrix
        

dimen_array = gen_cols()
print(gen_rows(dimen_array))