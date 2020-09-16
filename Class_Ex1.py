class demoClass:
    '''This is first class example'''
    x = 10
    y = 20
    def sum(self):
        a = 20
        b = 30
        print(a+b)


# print(demoClass.__doc__)
# print(help(demoClass))
# print(demoClass.__dict__)

d = demoClass()  # d is my object
d.sum()

d1 = demoClass()
d1.sum()