from threading import *
from time import *
def display():
    for i in range(10):
        print('Child Thread')
        sleep(3)

t = Thread(target=display)
t.start()
for i in range(10):
    print('Main thread')
    sleep(2)

