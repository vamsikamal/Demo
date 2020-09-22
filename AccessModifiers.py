class Test:
    x = 10             # public
    _y = 20            # protected
    __z = 30           # Private
    def m1(self):
        print(Test.x)
        print(Test._y)
        print(Test.__z)

class Child(Test):
    def m2(self):
        print(Test.x)
        print(Test._y)
       # print(Test.__z)


print(Test.__z)
'''
c = Child()
c.m2()
print(c._y)
'''