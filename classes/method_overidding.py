class Animal:

    def __init__(self):
        print("Animal Constructor")
        self.age = 12

    def eat(self):
        print("Eat")


class Mammal(Animal):
    def __init__(self):
        print("Mammal Constructor")
        self.weight = 20
        super().__init__()

    def walk(self):
        print("walk")


m = Mammal()
print(m.age)
print(m.weight)
