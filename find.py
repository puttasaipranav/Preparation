def same(input1,input2):
    for i in input1:
        for j in input2:
            if i == j:
                print(i)
print(same([1,2,3,4,5],[1,5,6,7,8]))
