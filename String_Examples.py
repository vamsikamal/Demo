# String methods
s1 = "Welcome to Python"
print(s1[0])            # W
print(s1[7])            # Space
print(s1[0], s1[8])     # W t

# Reverse Index
print(s1[-2])           # o

# Slicing
print(s1[2:6])          # lcom
print(s1[2:])           # lcome to Python
print(s1[:10])          # Welcome to
print(s1[:])            # Welcome to Python
print(s1[-6:-2])        # Pyth

# Step in slicing
print(s1[1:17:2])       # ecm oPto
print(s1[::3])          # Wceoyo

# Reverse
print(s1[::-1])
print(''.join(reversed(s1)))

# Length
print(len(s1))

# Trimming
s2 = "  Hyderbad"
print(s2.lstrip())  # Removes right hand side spaces

s2 = "Hyd    "
print(s2.rstrip())  # Removes right hand side spaces

s2 = "    HYD     "
print(s2.strip())   # Removes spaces from both ends

# Find()
s1 = "Welcome to Python"
s3 = "Python"
print(s1.find(s3))      # 11
print(s1.find(s2))      # -1
print(s1.rfind("Python")) #?

# index()
print(s1.index(s3))    # 11
#print(s1.index(s2))    # Error

# Replace
s4 = "Welcome to HYD"
s5 = s4.replace("HYD", "Hyderabad")
print(s5)       # Welcome to Hyderabad
print(s4)       # Welcome to HYD

# Split
s6 = s4.split()
print(s6)       # ['Welcome', 'to', 'HYD']
print(s6[0])    # Welcome
print(s6[1])    # to
print(s6[2])    # HYD
print(type(s6)) # <class 'list'>

# Case
print(s1)               # Welcome to Python
print(s1.lower())       # welcome to python
print(s1.upper())       # WELCOME TO PYTHON
print(s1.title())       # Welcome To Python
print(s1.capitalize())  # Welcome to python
print(s1)               # Welcome to Python

# Checking case
print(s1.islower())     # False
print(s1.isupper())     # False