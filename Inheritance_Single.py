# Single inheritance
# One parent class and one child class

class Parent:
    def m1(self):
        print("I am from parent class")

class Child(Parent):
    def m2(self):
        print("I am from child class")


p = Parent()
p.m1()

c = Child()
c.m1()
c.m2()