class Node:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None

def topView(root):
    if root is None:
        return
    
    topView(root.left)
    print(root.data,end=" ")
    topView(root.right)

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(60)

topView(root)
