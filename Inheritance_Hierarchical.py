class Parent:
    def m1(self):
        print("I am from parent class")

class Child1(Parent):
    def m2(self):
        print("I am from child 1 class")

class Child2(Parent):
    def m3(self):
        print("I am from child 2 class")


c1 = Child1()
c1.m1()
c1.m2()

c2 = Child2()
c2.m1()
c2.m3()

