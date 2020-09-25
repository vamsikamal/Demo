a = int(input("Enter first num: "))
b = int(input("Enter second num: "))
try:
    c = a / b
    print(c)
except ZeroDivisionError:
    print("Plz provide valid numbers. And try again. ")