def totalBill(*n):
    sum = 0
    for i in n:
        sum = sum + i

    print("Total Bill is ", sum)


totalBill(10,20,30)
totalBill(2,3,4,5,6,7,8,9.5)
# totalBill("SLC", "PYTHON") # Error