# Tuple is a collection of items of different type
# Tuple is immutable

a = (2, 3, 4, 5)
print(a)
print(type(a))  # (2, 3, 4, 5)

b = 2,3,4,5     # Packaging
print(b)        # (2, 3, 4, 5)

v1, v2, v3, v4 = b # Unpacking
print(v1)   # 2
print(v2)   # 3
print(v3)   # 4
print(v4)   # 5

print(b[0])  # 2
print(b[-1]) # 5
print(b[1:3]) # (3,4)

# Cannont append(), extend(), update, delete, pop() items from tuple

f = 20, 5, 30, 2
print(len(f)) # 4
print(max(f)) # 30
print(min(f)) # 2
print(sum(f)) # 57
print(any(f)) # True
print(all(f)) # True
f2 = (0,10)
print(any(f2)) # True
print(all(f2)) # False
f3 = (0,0,0)
print(any(f3)) # False
print(all(f3)) # False

# sort
b = (10, 2, 30, 4)
# c = b.sort()  # Not supported
c = sorted(b)
print(c)        # [2, 4, 10, 30]

# Tuple cannot be modified even if it is inside a list 
li = [1,2,3, (10, 20)]
#li[3][0] = 100   # We cannot change
print(li)

# List inside tuple can be mutable
tup = (1,2,3, [10,20])
tup[3][0] = 100
print(tup)  # (1, 2, 3, [100, 20])