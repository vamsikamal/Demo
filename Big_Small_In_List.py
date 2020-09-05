list = [10, 20, 30, 40, 5, 3, 8, 2]
big = list[0]
small = list[0]

for i in list:
    if i > big:
        big = i
    if i < small:
        small = i

print("Biggest number is ", big)
print("Smallest number is ", small)
