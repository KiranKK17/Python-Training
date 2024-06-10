#own code for animal using super class
class Animal:
    def __init__(self,name,location,age):
        self.name=name
        self.location=location
        self.age=age
    def description(self):
        print(f"This is {self.name} and iam from {self.location} and iam {self.age}")
class Cat(Animal):
    def __init__(self,name,breed,age,location):
        super().__init__(name,age,location)
        self.breed=breed
    def description(self):
        print(f"The cutiee {self.name} she is so cute and she is {self.age} her breed is {self.breed} and she is {self.location}")      
cat=Cat(name="bisshu", age=9, breed="pershian", location="bhemaram")
animal=Animal(name="sujji", location="hmk", age=10)
cat.description()
animal.description()
