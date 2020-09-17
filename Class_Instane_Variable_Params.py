# Initializing instance variables in constructor by sending parameters
class student:
    def __init__(self, name1, id1):        # Constructor
        self.name = name1      # Instance variables
        self.Id = id1          # Instance variables

    def disp(self):            # Instance method
        print("Name is ", self.name)
        print("ID is ", self.Id)

s = student("SLC", 100)
s.disp()
print(s.__dict__)

s2 = student("SLC Python", 101)
s2.disp()