def find(input2):
    high=input2[0]
    for i in input2:
        if i > high:
            high = i
    return i
print(find([95,568]))