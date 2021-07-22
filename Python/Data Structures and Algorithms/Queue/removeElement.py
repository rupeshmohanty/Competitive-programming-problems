class queue:
    def __init__(self):
        self.queue = list()
    
    def addtoq(self,dataval):
        if dataval not in self.queue:
            self.queue.insert(0, dataval)
            return True
        return False
    
    def removefromq(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return("No elements in queue!")
    
    def peek(self):
        return self.queue[-1]

if __name__ == "__main__":
    Tqueue = queue()
    Tqueue.addtoq("Mon")
    Tqueue.addtoq("Tue")
    Tqueue.addtoq("Wed")
    print(Tqueue.removefromq()) # Mon removed!
    print(Tqueue.removefromq()) # Tue removed!
    print(Tqueue.peek())