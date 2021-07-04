class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self,data):
        if self.data: # check if any data is passed!
            if data < self.data: # comparing with the root node!
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data
        
    def search(self,key):
        if self.data is None or self.data == key:
            return self.data

        if self.data < key:
            return search(self.right,key)
        
        return search(self.left,key)