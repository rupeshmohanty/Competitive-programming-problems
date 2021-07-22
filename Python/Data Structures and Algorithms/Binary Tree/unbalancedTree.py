class Node:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None

def height(root):
    if root is None:
        return 0
    
    return max(height(root.left),height(root.right)) + 1

def isBalanced(root):
    if root is None:
        return 1
    
    lh = height(root.left)
    rh = height(root.right)

    if abs(lh - rh) <= 1 and isBalanced(root.left) is True and isBalanced(root.right) is True:
        return 1
    else:
        return 0

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(60)

res = isBalanced(root)
print(res)
