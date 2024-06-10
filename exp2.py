#Creating a class make sure to print capital “p” while defining.
class Person:
    def __init__(self,name,college,group):
        self.name=name    #attributes
        self.college=college
        self.group=group
    def introduce(self,lang):      #calling a method
        print(f"Hi iam {self.name} and my college is {self.college} and my group is {self.group} and my mothertounge is {lang}")
#creating a object
P1= Person(name="Pogu Sravya Geervani", college="SR University", group="ECE")
P2= Person(name="Rohith", college="Vagdhevi", group="CSE")
P1.introduce("Telugu")    #calling a function
