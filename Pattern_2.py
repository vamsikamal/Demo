num = int(input("Enter a number to print: "))
dim = int(input("Enter a number rows: "))

for i in range(dim):
    for j in range(dim):
        print(num, end=' ')
    print()