##.remove() - removes elements
##pop() 
##discard()
##union()
##intersection()
##intersection_update() - updates the set with the intersection of itself and another
#difference 
##difference_update()
## symmetric_difference common elemenbts will be removed and returns combination
##isdisjoint() - TRUE if no intersection availabe
##issubset() - if a set is in another set ,it returns TRUE
##issuperset() - if a set is in another set ,it returns TRUE
##add() - addsan element


"""
all()
any()
sorted()


a = frozenaet([1,2,3,4])
print(a)

set1 = {1,4,3,9,6,7}
s2 = set(sorted(set1))
print(s2)


###Set Comprehension
res = {s for s in [1,2,3] if s%2}
print(res)
res2 = {s for s in [1,2,3,4,5,6,7,8,9,10] if s/10 == 1}
print(res2)






d = {1 : "hello",'a' : 'kiran','bf':1463}
print(d[1])
print(d.get('a'))
for i in d:
    print(i,':',d[i])
d['asdfgh'] = 'python'##add an element
print(d)
##update()
d.update({1:'abacus',2:143})
print(d)

#pop
d.pop('asdfgh')
print(d)
#popitem()
d.popitem()
print(d)
d.popitem()
print(d)
##clear
#d.clear()
#print(d)
###keys()
print(d.keys())
print(d.values())
print(d.items())
##fromkeys()
d = dict.fromkeys(d,10)
print(d)
print(d.setdefault('c',200))
####dictionary inside a dictionary
d69 = {'and' : 'hi','or':'a13','xor':{2 : 'abc0','c':'def'}}

student ={"name":"emma","calss":9,"marks":75}
del student[0:2]
student.clear()
del student

"""

####WAP to add a key to a dictionary
import operator
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