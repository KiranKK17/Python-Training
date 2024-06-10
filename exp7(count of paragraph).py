#Write a python program to do a word count of a paragraph.
s = input("Enter a paragraph: ")
count = 1
for char in s:
    if char == ' ':
        count += 1
print("Word count:", count)
