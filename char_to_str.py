#Write a Python program to convert a list of characters into a string.
def ch(a):
    x=''
    for i in a:
        x+=i
    return x
print(ch(['a','b','c','d','e']))

#Output: abcde