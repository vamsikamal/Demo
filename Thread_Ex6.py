from threading import *
from time import *

def display():
    for i in range(10):
        #print('Started: ', current_thread().name)
        sleep(3)

t1 = Thread(target=display, name = 'First Thread')
t2 = Thread(target=display, name = 'Second Thread')
t3 = Thread(target=display, name = 'Third Thread')

t1.start()
t2.start()
t3.start()
print(t1.is_alive())

enum = enumerate()              # Gets list of all current threads
for t in enum:
    print(t.getName())