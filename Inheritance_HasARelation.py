# Has A example
class Engine:
    hp = 100
    def __init__(self):
        self.pwr = 1199
    def m1(self):
        print("Engine method")
class car:
    def __init__(self):
        self.eng = Engine()
    def m2(self):
        print('Car is using engine ')
        print(self.eng.pwr)
        print(self.eng.hp)
        self.eng.m1()

c = car()
c.m2()