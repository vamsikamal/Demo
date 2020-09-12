def calc(a,b):
    s = a+b
    d = a-b
    p = a*b
    q = a/b

    return s,d,p,q


sum,diff, prod, quotient = calc(30,10)
print(sum)
print(diff)
print(prod)
print(quotient)