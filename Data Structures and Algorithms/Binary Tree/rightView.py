class Node:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None

def rightView(root):
    if root is None:
        return
    
    print(root.data,end=" ")
    rightView(root.right)

root = Node(1)
root.left = Node(3)
root.right = Node(2)

rightView(root)
