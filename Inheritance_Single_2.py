# Single inheritance
# One parent class and one child class

class Parent:
    def __init__(self):
        print("I am parent class's constructor ")

    def m1(self):
        print("I am from parent class")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("I am child class's constructor ")
    def m1(self):
        super().m1()
        print("I am from child class")

c = Child()
c.m1()