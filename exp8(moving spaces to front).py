#Write a python program to move all spaces to the front of a given string in single traversal.
s=input()
spaces=" "
result= " "
for char in s:
    if char==" ":
        spaces+=char
    else:
        result+=char
final_string=spaces+result
print(final_string)
