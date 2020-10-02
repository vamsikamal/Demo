from threading import *
from time import *
l = RLock()
def fact(n):
    l.acquire()
    if n==0:
        res = 1
    else:
        res = n * fact(n-1)
    l.release()
    return res

def result(n):
    print('The factorial of ', n, ' is ', fact(n))

t1 = Thread(target=result, args=(5, ))
t2 = Thread(target=result, args=(6, ))
t1.start()
t2.start()