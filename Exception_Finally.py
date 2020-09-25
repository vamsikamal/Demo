try:
    a = int(input("Enter first num: "))   # ten
    b = int(input("Enter second num: "))
    c = a / b
    print(c)

except (ZeroDivisionError, ValueError) as msg:
    print("Error: ", msg)

finally:
    print("Closing resources")