class Parent1:
    def m1(self):
        print("I am from Parent1 class")

    def m5(self):
        print("M5 from Parent1")

class Parent2():
    def m2(self):
        print("I am from Parent2 class")

    def m5(self):
        print("M5 from Parent2")

class Child(Parent1, Parent2):
    def m3(self):
        print("I am from child class")



c = Child()
c.m1()
c.m2()
c.m3()
c.m5()