class Demo:
    def __init__(self):
        print("Constructor")
    def __del__(self):
        print("Destructor")

d = Demo()
del d
