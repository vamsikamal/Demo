# List Type
# Collection of itmes of different type
# Mutable
mylist = []  # Empty List
mylist1 = [1,2,3,'Hello',4.5]
print(mylist1)
print(type(mylist1))
print(mylist1[0])   # 1
print(mylist1[1:3]) # [2, 3]
print(mylist1[::2]) # [1,3,4.5]

# Nested list
nlist = [10, 20, [30, 40, 50], 60]
print(nlist[2])  # [30, 40, 50]
print(nlist[2][1])  # 40

# Changing values
n = [1,2,3,4,5,6,7]
n[0] = 100
print(n)   # [100, 2, 3, 4, 5, 6, 7]
n[1:3] = ['x', 'y', 'z','p']
print(n) # [100, 'x', 'y', 'z', 5, 6, 7]

n.append(200)
print(n)   #  [100, 'x', 'y', 'z', 'p', 4, 5, 6, 7, 200]

n.extend([111,222,33])
print(n)   # [100, 'x', 'y', 'z', 'p', 4, 5, 6, 7, 200, 111, 222, 33]

odd = [1,3,5] + [7,9,11]
print(odd)   # [1, 3, 5, 7, 9, 11]
print(odd * 3) # [1, 3, 5, 7, 9, 11, 1, 3, 5, 7, 9, 11, 1, 3, 5, 7, 9, 11]

#Insert
a = [1,2,3,4,5]
a.insert(2, 'Hello')
print(a)   # [1, 2, 'Hello', 3, 4, 5]

# Remove
b = [1,2,3,4,5]
del b[3]
print(b)  # [1, 2, 3, 5]

b = [1,2,3,4,5]
del b[1:3]
print(b) # [1, 4, 5]

b.clear()  # deletes all elements of list
print(b)

#del b
#print(b)  # list deleted

c = [1,2,3,4,5]
p = c.pop()  # Last item will be popped
print(p)    # 5
print(c)    # [1, 2, 3, 4]

c = [1,2,3,4,5]
p = c.pop(3)  # index 3 item will be popped
print(p)    # 4
print(c)    # [1, 2, 3, 5]

d = [10,20,30,20,30,40,50,60,20,30]
print(d.index(30))  # 2 -> Index of first occurrance
print(d.count(30))  # 3
print(d.count(1))   # 0

# sort
e = [20, 5, 30, 2]
e.sort()
print(e)   #  [2, 5, 20, 30]

# reverse
e.reverse()
print(e)   #  [30, 20, 5, 2]

# sorted
f = [20, 5, 30, 2]
f1 = sorted(f)
print(f1)   #  [2, 5, 20, 30]
print(f)

s = ['b', 'c', 'a']
print(s.sort())   # None


# reversed
f = [20, 5, 30, 2]
f1 = reversed(f)
#for i in f1: print(i)
print(reversed(f))  # <list_reverseiterator object at 0x0344B370>
print(f)


print(len(f)) # 4
print(max(f)) # 30
print(min(f)) # 2
print(sum(f)) # 57
print(any(f)) # True
print(all(f)) # True
f2 = [0,10]
print(any(f2)) # True
print(all(f2)) # False
f3 = [0,0,0]
print(any(f3)) # False
print(all(f3)) # False

