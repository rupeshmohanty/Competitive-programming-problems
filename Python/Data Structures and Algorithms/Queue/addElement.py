class queue:
    def __init__(self):
        self.queue = list()
    
    def addtoq(self,dataval):
        if dataval not in self.queue:
            self.queue.insert(0, dataval)
            return True
        return False
    
    def size(self):
        return len(self.queue)
    
    def peek(self):
        return self.queue[-1]

if __name__ == "__main__":
    Tqueue = queue()
    Tqueue.addtoq("Mon")
    Tqueue.addtoq("Tue")
    Tqueue.addtoq("Wed")
    print(Tqueue.size())
    print(Tqueue.peek())