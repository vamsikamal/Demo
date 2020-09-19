class student:
    universirty = "Python"
    def __init__(self):
        self.college = "SLC"

    def display(self):
        print("From instance method", self.college)

    @classmethod
    def disp(cls):
        print(cls.universirty)

    @staticmethod
    def wish():
        print("Good morning all students ")
        print(student.universirty)


s = student()         # Constructor
s.display()           # instance method
student.disp()        # class method
student.wish()        # static method

