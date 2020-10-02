from threading import *
from time import *

def doubles(numbers):
    for i in numbers:
        sleep(1)
        print("Double", 2*i)

def squares(numbers):
    for i in numbers:
        sleep(1)
        print("Square", i*i)


num = [1,2,3,4,5,6,7,8,9]
begin = time()
t1 = Thread(target=doubles, args=(num,))
t2 = Thread(target=squares, args=(num,))
#t1.setName('Thread 1')
#t2.setName('Thread 2')
t1.start()
#print(t1.getName(), 'Started')
t2.start()
#print(t2.getName(), 'Started')
t1.join()
t2.join()
end = time()
print("Totao time taken : ", end - begin)
