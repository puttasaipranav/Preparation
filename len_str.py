#Write a Python program to count the number of strings 
# where the string length is 2 or more
def leng(a):
    g=[]
    for i in a:
        if len(i)>=2:
            g.append(i)
    print(len(g))
leng(['sai','f','fg'])

#Output : 2