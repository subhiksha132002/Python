class Animal:

    def __init__(self):
        self.age = 12

    def eat(self):
        print("Eat")


class Mammal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


f = Fish()
print(f"Instance : {isinstance(f, Fish)}")
print(f"Instance : {isinstance(f, Animal)}")
print(f"Instance : {isinstance(f, object)}")
o = object()
print(f"Sub class : {issubclass(Fish, Animal)}")
print(f"Sub class : {issubclass(Fish, object)}")
