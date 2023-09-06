class Employee:
    def greet(self):
        print("Employee here")


class Person:
    def greet(self):
        print("Person here")


class Manager(Person, Employee):
    pass


m = Manager()
m.greet()
