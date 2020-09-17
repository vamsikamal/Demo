class student:
    instituition = "SLC"                  # Static variable 
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def disp(self):
        print("Name ", self.name)
        print("Id ", self.id)
        print("Instituition ", student.instituition)


s1 = student('Ramesh',10)
s2 = student('Rajesh',11)
s3 = student('Ramu',12)

s1.disp()
s2.disp()
s3.disp()