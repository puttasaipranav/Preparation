def same(input1,input2):
    for i in input1:
        found=False
        if i in input2:
            print(i)
            found=True
    if found==False:
        print('None')
same([1,2,3,4,5],[1,32,2,4,7])