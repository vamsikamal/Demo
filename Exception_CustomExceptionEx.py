class TooYoungException(Exception):
    def __init__(self,arg):
        self.msg = arg

class TooOldException(Exception):
    def __init__(self,arg):
        self.msg = arg

age = int(input("Enter age: "))
if age>60:
    raise TooOldException("You are too old for this job ")
elif age<14:
    raise TooYoungException("You are too young for this job ")
else:
    print("You are eligible")