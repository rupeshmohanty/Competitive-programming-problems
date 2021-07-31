class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self, data):
        if data == self.data:
            return 
        
        # add in left subtree!
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        # add in right subtree!
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    
    # Inorder traversal --> Left, Parent, Right!
    def inorder_traversal(self):
        elements = []

        # adding the left node!
        if self.left:
            elements += self.left.inorder_traversal()
        
        # adding the base node!
        elements.append(self.data)

        # adding the right node!
        if self.right:
            elements += self.right.inorder_traversal()

        return elements

    def search(self, val):
        if self.data == val:
            return True
        
        if val < self.data:
            # val might be in left subtree!
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            # val might be in right subtree!
            if self.right:
                return self.right.search(val)
            else:
                return False

def buildTree(elements):
    # setting the first element as the parent node!
    root = BinarySearchTreeNode(elements[0])

    # adding the other elements to the list!
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    
    return root

if __name__ == "__main__":
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = buildTree(numbers)
    print(numbers_tree.search(21))