list = [10, 20, 30, 1, 2, 3, 100, 200, 300, 400]
num = int(input("Enter number: "))
isItemFound = False
for i in list:
    if num == i:
        isItemFound = True
        break

if isItemFound == True:
    print("Item found")
else:
    print("Item Not found")