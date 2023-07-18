class Animal:
    def __init__(self):
        self.eyes=2
    def breath(self):
        print("yes animal can breath")

class Fish(Animal):#inheriting the animal class in fish class
    def breath(self):
        super().breath()#this is to access the animal class and add extra instruction
        print("yes fish can breath")
    def swin(self):
        print("yes fish can swim")

nemo=Fish()
nemo.swin()
nemo.breath()
print(nemo.eyes)


class Dog:
    def __init__(self):
        self.temperament = "loyal"


class Labrador(Dog):
    def __init__(self):
        super().__init__()
        self.temperament = "gentle"


doggo = Dog()
print(f"A dog is {doggo.temperament}")

sparky = Labrador()
print(f"Sparky is {sparky.temperament}")

