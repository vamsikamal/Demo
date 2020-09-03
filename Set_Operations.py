A = {1,2,3,4,5}
B = {4,5,6,7,8}

print(A|B)  # {1,2,3,4,5,6,7,8}
print(A.union(B))  # {1,2,3,4,5,6,7,8}

print(A&B)  # {4,5}
print(A.intersection(B)) # {4,5}

print(A-B)  # {1,2,3}
print(A.difference(B)) # {1,2,3}

print(A^B)  # {1, 2, 3, 6, 7, 8}
print(A.symmetric_difference(B)) # {1, 2, 3, 6, 7, 8}

# Update
C = {1, 2}
D = { 2, 3}
C |= D    # C = C | D
C.update(D) # C= C.Union(D)
print(C)

C &= D  # C = C & D
C.intersection_update(D)

C ^= D   # C = C^D
C.symmetric_difference_update(D)

C -= D
C.difference_update(D)