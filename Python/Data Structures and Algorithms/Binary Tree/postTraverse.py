class Node:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None

def postorder(root):
    if root is None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.data,end=" ")

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)

postorder(root)
