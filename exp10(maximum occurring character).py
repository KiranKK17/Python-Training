#Write a python program to find the maximum occurring character in a given string.
s=input()
max_char=max(s, key=s.count)
print(f"Maximum occuring character: {max_char}")
