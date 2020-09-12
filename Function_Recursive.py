# Calling a function inside the same function is known as recursive
def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n-1)

f = fact(4)
print(f)