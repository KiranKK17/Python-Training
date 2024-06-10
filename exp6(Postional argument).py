#POSITIONAL ARGUMENT
def nameAge(name, age):
    print("hi, i am", name)
    print("my age is", age)
print("case-1:")     #you wil get coorect output bcz argument is in order
nameAge("Sravya", 20)
print("\nCase-2:")   #you wil get incoorect output bcz argument is not in order
nameAge(20, "Sravya")
