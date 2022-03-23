from collections import deque

class Queue:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.appendleft(val)
    
    def pop(self):
        return self.container.pop()
    
    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)

if __name__ == "__main__":
    q = Queue()

    q.push(5)
    q.push(8)
    q.push(27)

    print(q.pop())
    print(q.is_empty())
    print(q.size())