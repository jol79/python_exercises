# num % 7 == 0 -> +
# num % 5 == 0 -> -
# in range (2000, 3200), both included


def division(low, top):
    nums = []

    for num in range(low, top+1): 
        if num % 7 == 0:
            if num % 5 == 0:
                continue
        nums.append(num)
    
    return nums


# print(division(2000, 3200))


# output must be with comma+space and only in one line: 
nums = []

for num in range(2000, 3200+1): 
    if num % 7 == 0:
        if num % 5 == 0:
            continue
    nums.append(str(num))

print(', '.join(nums))