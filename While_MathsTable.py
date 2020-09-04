# initialization, condition, incre/decre
num = int(input("Enter a number: "))
i = 1               # initialization
while i < 21:       # condition
    print("{0} * {1} = {2}".format(i, num, i*num))        # action or body of loop
    i = i + 1       # increment or decrement statement