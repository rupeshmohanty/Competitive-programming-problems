class Node:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None

def bottomView(root):
    if root is None:
        return
    
    bottomView(root.left)
    bottomView(root.right)

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(60)

bottomView(root)
