from threading import *
l = RLock()
print('Main thread is trying to lock ')
l.acquire()
print('Main thread is trying to lock again ')

l.acquire()
print('End of program')
