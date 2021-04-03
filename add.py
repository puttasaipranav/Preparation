def add(input1,input2):
    total=0
    for i in range(input1-1):
        addi=input2[i] + input2[i+1]
        sum=total+addi
        print(sum)
    return sum
add(5,[10,20,30,40,50])