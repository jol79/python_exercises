"""
 each element of the sequence is sum of 2 previous
"""
length = int(input("Provide length: "))

n1, n2 = 0, 1
counter = 0

if length <= 0:
    print("Negative nums and 0s as input are not allowed")
elif length == 1:
    print("F sequence up to: {}".format(n1))
else:
    print(n1)
    while counter < length:
        nxt = n1 + n2
        print(nxt)
        # change the start values
        n1 = n2
        n2 = nxt

        counter += 1

