class Node:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None
    
def zigzagTraversal(root):
    if root is None:
        return 
    
    currentLevel = []
    nextLevel = []

    ltr = True

    currentLevel.append(root)

    while(len(currentLevel) > 0):
        temp = currentLevel.pop(-1)

        print(temp.data,end=" ")

        if ltr:
            if temp.left:
                nextLevel.append(root.left)
            if temp.right:
                nextLevel.append(root.right)
        else:
            if temp.right:
                nextLevel.append(temp.right)
            if temp.left:
                nextLevel.append(temp.left)
        
        if len(currentLevel) == 0:
            ltr = not ltr
            currentLevel,nextLevel = nextLevel,currentLevel
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(4)

zigzagTraversal(root)