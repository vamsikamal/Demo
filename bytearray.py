# Collection of numbers
# Range from 0 to 256
# Immutable -> we can change
a = [10, 20, 30, 40]
b = bytearray(a)
print(b)
print(type(b))
for i in b: print(i)

b[0] = 100
for i in b: print(i)