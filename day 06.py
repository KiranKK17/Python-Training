"""
str = "sasankanaaaa"
a = (str.index('a') + str.rindex('a'))//2
print(a)

string.capitalize()
string.find()
string.rfind()
string.count()
len()
max()
min()
string.ascii()
string.punctuation()
replace()
string.isdecimal()
string.islitte()
string.isalnum()
string.rindex()
string.partition()
string.capitalize()



##wAP to calculate the length of a string
a = input()
print(len(a))

###WAP that takes input from the user and displays theinput back in upper and lower cases
b = input("Enter the paragraph: ")
c = input("Enter the word to caps: ")

# Replace all occurrences of the word with its uppercase version
new_paragraph = b.replace(c, c.upper())

print("Your input with the word in upper case:", new_paragraph)
print("Your input in lower case:", b.lower())

####WAP to remove all consecutive duplicates from a given string
a = input()
result = str[0]
for i in range(1,len(str)):
    if str[i] != result[-1]:
        result += str[i]
print(result)


###WAP to move all spaces to the front of a given string in a single traversal
s = input()
space = ""
result = ""
for i in s:
    if i == " ":
        space += i
    else:
        result += i
string = space + result
print(string)

###WAP to create  a string from two given strings concatenating uncommon characters of the said strings
# Input from user
str1 = input()
str2 = input()
set1 = set(str1)
set2 = set(str2)
uncommon_set1 = set1 - set2
uncommon_set2 = set2 - set1
result = '='.join(uncommon_set1) + ''.join(uncommon_set2)
print(result)


###WAP to find the maximum occuring character in a given string
# Input from user
input_string = input("Enter a string: ")

# Initialize an empty dictionary to store character counts
char_count = {}
for char in input_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
max_char = max(char_count, key=char_count.get)
max_count = char_count[max_char]
print(f"The maximum occurring character is '{max_char}' with {max_count} occurrences.")





#####FUNCTIONS#######

def check_prime():
    num=int(input("enter the a num: "))
    if num > 1:
        for i in range (2, int(num**0.5)+1):
            if num % i== 0:
                print(num, "is not a prime")
                break
            else:
                print(num,"is prime num")
    else:
        print(num,"is not prime")
check_prime()

####default argument


def my_sum(*args):
    
    result = 0
    for x in args:
        result+= x
    return result

print(my_sum(1,2,3))


def concatenate(**words):
    result = "words"
    for arg in words.values():
        result += arg
    return result

print(concatenate(a = "real",b ="python",c = "is", d= "great",e = "!")


####recursion###
def sum_recursive(n):
    if n <= 0:
        return 0
    return n + sum_recursive(n - 1)

# Example usage
print(sum_recursive(5))


"""
def print_(n,i =1):
    if i > n:
        return
    print(i)
    print_(n,i + 1)
print_(5) 
print("hello")
def print_reverse(n):
    if n < 0:
        return
    print(n)
    print_reverse(n - 1)
print_reverse(5) 


def fibonacci(f):
    if f <= 0:
        return 0
    elif f == 1:
        return 1
    else:
        return fibonacci(f-1) + fibonacci(f-2)

num = int(input("Enter the number of terms: "))
for i in range(num):
    print(f"Fibonacci({i}) = {fibonacci(i)}")
