class stack:
    def __init__(self):
        self.stack = []
    
    # adding elements to the stack!
    def add(self,dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
        
    # to peek the last element or top of the stack!
    def peek(self):
        return self.stack[-1]

if __name__ == "__main__":    
    Astack = stack()
    Astack.add("Mon")
    Astack.add("Tue")
    print(Astack.peek())

    Astack.add("Wed")
    Astack.add("Thu")
    print(Astack.peek())
