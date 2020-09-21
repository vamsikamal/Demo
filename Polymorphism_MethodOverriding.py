class Parent:
    def m1(self):
        print("Parent")
class Child(Parent):
    def m1(self):
        print("Child")

c = Child()
c.m1()