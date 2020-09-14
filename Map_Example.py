# map()

l1 = [1,2,3,4,5]
def doubleit(n):
    return 2*n

l2 =list(map(doubleit, l1))
print(l2)

# With lambda expression
l1 = [1,2,3,4,5]
l2 =list(map(lambda x:x*2, l1))
print(l2)