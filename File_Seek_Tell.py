f = open('demo.txt','r')
print(f.tell())
line1 = f.readline()
print(f.tell())
print(line1)
print(f.tell())
f.close()


f = open('demo.txt','r')
print(f.tell())
line1 = f.readline()
print(f.tell())
print(line1)
f.seek(10)                    # Cursor goes to 10th position
print(f.tell())
f.close()
