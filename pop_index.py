#Write a Python program to print a specified list 
# after removing the 0th, 4th and 5th elements
def rem(a):
    a.pop(0)
    a.pop(3)
    a.pop(4)
    print(a)
rem([1,2,3,4,5,6,7])
# Output: [2, 3, 4, 6]