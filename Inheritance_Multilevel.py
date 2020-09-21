class Parent:
    def m1(self):
        print("I am from parent class")

class Child(Parent):
    def m2(self):
        print("I am from child class")

class Child2(Child):
    def m3(self):
        print("I am from child 2")


c = Child2()
c.m1()
c.m2()
c.m3()