from abc import *
class Test(ABC):
    @abstractmethod
    def m1(self):              # Abstract method
        pass

    def m2(self):              # Non-abstract or concrete method
        print("Not abstract method")

class Child(Test):
    def m1(self):
        print("I am from child class")

t = Child()
t.m1()

