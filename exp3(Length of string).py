#write a python program to calculate the length of a string.
str="coder123"
print(len(str))


def len1(str1):
    count=0
    for char in str1:
        count += 1
    return count
str1=input()
print(len1(str1))
