def add(input1,input2):
    total=0
    for i in range(input1-1):
        addi=input2[i] + input2[i+1]
        sum=total+addi
    return sum
add(2,[1,2])

