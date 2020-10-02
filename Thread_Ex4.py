from threading import *
class Demo:
    def display(self):
        for i in range(10):
            print('Child thread')

obj = Demo()
t = Thread(target = obj.display)
t.start()

for i in range(10):
    print('Main thread')