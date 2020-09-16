a = 10

def test():
    global a
    a = 20
    print(a)

def demo():
    a = 30
    print(a)

test()
demo()
print(a)