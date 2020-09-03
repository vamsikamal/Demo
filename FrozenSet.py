# Frozen set is like set only but it is immutable.
s = {10, 20, 30, 40}
f = frozenset(s)
print(type(f))

for i in f: print(i)
