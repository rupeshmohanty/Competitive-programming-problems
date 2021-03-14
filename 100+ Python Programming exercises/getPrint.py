class InputOutString:
    def __init__(self,s):
        self.s = s
    
    def getString(self):
        print(self.s)
    
    def printString(self):
        print(self.s.upper())

strObj = InputOutString("Rupesh")
strObj.getString()
strObj.printString()