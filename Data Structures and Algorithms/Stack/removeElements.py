class stack:
    def __init__(self):
        self.stack = []
    
    # to add elements to the stack!
    def add(self,dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
    
    # to peek the top of the stack!
    def peek(self):
        return self.stack[-1]
    
    # remove latest element
    def removeElement(self):
        if len(self.stack) <= 0:
            return ("No element in the stack!")
        else:
            return self.stack.pop()

if __name__ == "__main__":
    Astack = stack()
    Astack.add("Mon")
    Astack.add("Tue")
    Astack.add("Wed")
    Astack.add("Thu")
    print(Astack.removeElement())
    print(Astack.removeElement())
    print(Astack.peek())


    