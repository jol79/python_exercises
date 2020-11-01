"""
 calc the factorial of the given number
 req:
   1) print in ", " sequence
"""
def factr(x): 
    if x == 0: 
        return 1
    print(x)
    return x * factr(x - 1)

print(factr(8))