class student:
    def __init__(self, name1, id1):        # Constructor
        self.name = name1      # Instance variables
        self.Id = id1          # Instance variables

    def disp(self):            # Instance method
        self.pin = 500080
        self.admin = "Kishore"
        print("Name is ", self.name)
        print("ID is ", self.Id)

s = student("SLC", 100)
s.Course = "Python"
s.Location = "Hyd"
s.disp()
print(s.__dict__)
