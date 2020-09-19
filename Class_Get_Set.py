class Bank:
    def setInterest(self, interest):
        self.intrst = interest + 4    # Some extra logic

    def getInterest(self):
        return self.intrst - 4


b = Bank()
b.setInterest(10)
print(b.getInterest())