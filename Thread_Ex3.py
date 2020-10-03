from threading import *
class Test(Thread):
    def run(self):
        for i in range(10):
            print('Child thread')

t = Test()
t.start()

for i in range(10):
    print('Main thread')