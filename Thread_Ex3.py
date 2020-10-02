from threading import *
class TestThread(Thread):
    def run(self):
        for i in range(10):
            print('Child thread')

t = TestThread()
t.start()
for i in range(10):
    print('Main thread')