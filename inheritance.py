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


m = Mammal()
m.eat()
print(f"Age is {m.age}")
