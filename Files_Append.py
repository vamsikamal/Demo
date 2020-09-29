f = open('demo.txt', 'a')
f.write('VamsiKamal')
f.write("Demo file program\n")
f.write("How are you today? \n")

lst = ['sunday\n','monday\n','tuesday\n']
f.writelines(lst)

f.close()