"""class person:
    def __init__(self,name):
        self.name = name
    def say_hi(self):
        print("hello my name is ",self.name)

p = person('kiran')
p.say_hi()


#multi level inheritance
class Parent:
    def func1(self):
        print("first function")
class Child(Parent):
    def func2(self):
        print("second function")
class Child2(Child):
    def func3(self):
        print("third function")
ob=Child2()
ob.func1()
ob.func2()
ob.func3()



class parent:
    def func1(self):
        print("this is function 1")
class child(parent):
    def func2(self):
        super().func1()
        print("this is function 2")

ob = child()
ob.func2()


class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound

    def make_sound(self):
        print(f"The {self.species} named {self.name} goes {self.sound}")

class Lion(Animal):
    def __init__(self, name):
        super().__init__(name, "Lion", "roar")

    def get_info(self):
        print("Lions are the kings of the jungle.")

class Elephant(Animal):
    def __init__(self, name):
        super().__init__(name, "Elephant", "trumpet")

    def get_info(self):
        print("Elephants are the largest land animals.")

class Snake(Animal):
    def __init__(self, name):
        super().__init__(name, "Snake", "hiss")

    def get_info(self):
        print("Snakes can be found on every continent except Antarctica.")


lion = Lion("Leo")
elephant = Elephant("Dumbo")
snake = Snake("Kaa")

lion.make_sound()
lion.get_info()

elephant.make_sound()
elephant.get_info()

snake.make_sound()
snake.get_info()
"""

n = int(input())
s = input().strip()

anton_wins = s.count('A')
danik_wins = s.count('D')

if anton_wins > danik_wins:
    print("Anton")
elif danik_wins > anton_wins:
    print("Danik")
else:
    print("Friendship")
