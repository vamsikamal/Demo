# Insertion order is not preserved
# Stores unique
# No index concept
# We can add items to set

A = {1,2,3,4}
print(A)
print(type(A))

A.add(20)
A.add(3)
print(A)

A.update([10,30,40])
print(A)

A.remove(10)
A.discard(20)
print(A)