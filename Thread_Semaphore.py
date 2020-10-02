from threading import *
from time import *

s = Semaphore(2)

def wish(name):
    s.acquire()
    for i in range(10):
        print('Good evening', name)
        sleep(2)

    s.release()

t1 = Thread(target=wish, args=('Vamsi',))
t2 = Thread(target=wish, args=('Kamal',))
t3 = Thread(target=wish, args=('Ram',))
t4 = Thread(target=wish, args=('Rohith',))
t5 = Thread(target=wish, args=('Krish',))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()