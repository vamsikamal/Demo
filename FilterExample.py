# filter(function, sequence)
def isEven(x):
    if x%2 == 0:
        return True
    else:
        return False

l1 = [1,2,3,4,5,6,7,8]
l2 = list(filter(isEven, l1))
print(l2)


# filter with lambda example
l1 = [1,2,3,4,5,6,7,8]
l2 = list(filter(lambda x:x%2==0, l1))
print(l2)