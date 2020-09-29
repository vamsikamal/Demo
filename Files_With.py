with open('demo.txt','r') as f:
    data = f.readlines()
    print(data)
    print(f.closed)

print(f.closed)

 