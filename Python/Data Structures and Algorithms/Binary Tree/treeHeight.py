class Node:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None

def height(root):
    if root is None:
        return 0
    else:
        lheight = height(root.left)
        rheight = height(root.right)

        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)

res = height(root)
print(res)