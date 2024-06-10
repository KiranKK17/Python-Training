#introduction of yourself 
class Person:
    def __init__(self,name,college,group):
        self.name=name    #attributes
        self.college=college
        self.group=group
    def introduce(self):        #calling the methods
        print(f"Hi iam {self.name} and my college is {self.college} and my group is {self.group}")
    def study(self):
        print(f"{self.name} is studying in the {self.group} group at {self.college}")
        print()
#creating an object 
P1= Person(name="Pogu Sravya Geervani", college="SR University", group="ECE")
P2= Person(name="Rohith", college="Vagdhevi", group="CSE")
P1.introduce()                #calling functions
P1.study()
P2.introduce()
P2.study()
