from threading import *
from time import *

def display():
    for i in range(10):
        print('Child Thread', current_thread().name)
        sleep(3)

t = Thread(target=display)
t.start()

for i in range(10):
    print('Main thread', current_thread().name)
    sleep(2)


