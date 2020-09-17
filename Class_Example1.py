# Instance Variables
# Instance Methods
# Constructors
# Initializing instance variables in constructor

class student:
    def __init__(self):        # Constructor
        self.name = "SLC"      # Instance variables
        self.Id = 123          # Instance variables

    def disp(self):            # Instance method
        print("Name is ", self.name)
        print("ID is ", self.Id)

s = student()
s.disp()
