# Collection of numbers
# Range from 0 to 256
# Mutable -> we cannot change
a = [10, 20, 30, 40]
b = bytes(a)
print(type(b))
for i in b: print(i)