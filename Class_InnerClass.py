class Outer:
    def __init__(self):
        print("Outer class constructor")

    def dispOuter(self):
        print("Hello from outer class")

    class inner:
        def __init__(self):
            print("Inner class constructor")

        def dispInner(self):
            print("Hello from inner class")

o = Outer()
i = o.inner()

o.dispOuter()
i.dispInner()

