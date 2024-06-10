#Write a python program to create a string from two given strings concatenating uncommon characters of the said strings.
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
s = ""
for char in s1:
    if char not in s2 and char not in s:
        s += char
for char in s2:
    if char not in s1 and char not in s:
        s += char
print("String with uncommon characters are :", s)

s1=input()
s2=input()
uncommon_chars=" ".join(set(s1)^set(s2))
print(uncommon_chars)
