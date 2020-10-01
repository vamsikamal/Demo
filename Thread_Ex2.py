from threading import *
from time import *



def display():
    for i in range(10):
        print('display1 Thread', current_thread().name)
        sleep(3)

def display2():
    for i in range(10):
        print('display2 ', current_thread().name)
        sleep(3)

t = Thread(target=display)
t.start()
print("Threads count is : " , active_count())

t2 = Thread(target=display2)
t2.start()


