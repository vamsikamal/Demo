f = open('demo.txt','r')
data = f.read(20)          # Reads only 20 characters from file
f.close()
print(data)


f = open('demo.txt','r')
line1 = f.readline()
line2 = f.readline()
print(line1)
print(line2)
f.close()


f = open('demo.txt','r')
data = f.readlines()
print(data)
f.close()