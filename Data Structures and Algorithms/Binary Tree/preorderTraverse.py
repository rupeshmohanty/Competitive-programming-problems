class Node:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None

def preorder(root):
    if root is None:
        return
    
    print(root.data,end=" ")

    preorder(root.left)
    preorder(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)

preorder(root)
