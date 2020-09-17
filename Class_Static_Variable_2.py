class student:
    instituition = "SLC"                  # Static variable
    strength = 0                          # Static variable
    def __init__(self, name, id):
        self.name = name
        self.id = id
        student.strength = student.strength + 1

    def disp(self):
        print("Name ", self.name)
        print("Id ", self.id)
        print("Instituition ", student.instituition)
        print("Strength", student.strength)


student.strength = 200                # Changing static variable out side of the class
s1 = student('Ramesh',10)
s1.strength = 300                     # This is not static variable, It is instance specific variable
s1.disp()
s2 = student('Rajesh',11)
s2.disp()
s3 = student('Ramu',12)
s3.disp()