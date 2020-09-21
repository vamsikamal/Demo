class Test:
    def m1(self):
        print("I am from m1")

    def m1(self, a):
        print(a)


t = Test()
t.m1(10)
