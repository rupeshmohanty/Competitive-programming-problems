class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key
    
# function to print level traversal!
def printLevelTraverse(root):
    h = height(root)
    for i in range(1,h+1):
        printGivenLevel(root,i)

# print nodes at a given level!
def printGivenLevel(root,level):
    if root is None:
        return

    if level == 1:
        print(root.data,end = " ")
    elif level > 1:
        printGivenLevel(root.left,level-1)
        printGivenLevel(root.right,level-1)

# computing the height of the tree!
def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)

        # use the larger height!
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

printLevelTraverse(root)
