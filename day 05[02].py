"""import operator
w ={}
n = int(input("enter the no.of elemnts"))
for i in range(n):
    k = input("enter key for first dict:")
    v = input("enter first value")
    w[k] = v
key = input()
value = input()
w.update({key:value})
print(w)

#WAP To check whether a given key already exists in a dictionary
w ={}
n = int(input("enter the no.of elemnts"))
for i in range(n):
    k = input("enter key for first dict:")
    v = input("enter first value")
    w[k] = v
check = input("enter key")
if check in w:
    print(True)
else:
    print(False)

    
# WAP to generate and print a dictionary that contains a number (between 1 and n) in form (x,x*x)
n = int(input("input a number"))
ac = dict()
for i in range(n):
    ac[i] = i*i
print(ac)


#Merge two dictionaries
w ={}
n = int(input("enter the no.of elemnts"))
for i in range(n):
    k = input("enter key for first dict:")
    v = input("enter first value")
    w[k] = v
print(w)
z ={}
q = int(input("enter the no.of elemnts"))
for i in range(n):
    e = input("enter key for first dict:")
    ev = input("enter first value")
    z[e] = ev
zz = z.copy()
zz.update(z)
print(zz)


##WAP to remove a key from dictionary
w ={}
n = int(input("enter the no.of elemnts"))
for i in range(n):
    k = input("enter key for first dict:")
    v = input("enter first value")
    w[k] = v
print(w)
w.pop(input())
print(w)



#WAP to map two lists into a dictonary

a = list(map(int,input().split()))
b = list(map(int,input().split()))
d = {}
for i in range(len(a)):
    k = a[i]
    v = b[i]
    d[k] = v
print(d)






###WAP to combine two dictonary adding values for common keys
from collections import Counter
w ={}
n = int(input("enter the no.of elemnts"))
for i in range(n):
    k = input("enter key for first dict:")
    v = input("enter first value")
    w[k] = v

z ={}
q = int(input("enter the no.of elemnts"))
for i in range(n):
    e = input("enter key for first dict:")
    ev = input("enter first value")
    z[e] = ev
combined_dict ={}
for key in w:
    if key in z:
        combined_dict[key] = w[key] + z[key]
    else:
        combined_dict[key] = w[key]

for key in z:
    if key not in combined_dict:
        combined_dict[key] = z[key]

print("combined dictionary:", combined_dict)

"""
