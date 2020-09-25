
try:
    a = int(input("Enter first num: "))
    b = int(input("Enter second num: "))
    c = a / b
    print(c)

except (ZeroDivisionError, ValueError) as msg:
    print("Error: ", msg)
