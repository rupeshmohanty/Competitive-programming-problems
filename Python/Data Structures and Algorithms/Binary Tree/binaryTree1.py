class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    # Adding elements into the list!
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

    # searching an element in the binary tree!
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

    # finding maximum element!
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    # finding minimum element!
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    # Delete an element from the binary tree!
    def deleteNode(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.deleteNode(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.deleteNode(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.deleteNode(min_val)

        return self

if __name__ == "__main__":
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    root = BinarySearchTreeNode(numbers[0])

    # adding the other elements to the list!
    for i in range(1,len(numbers)):
        root.add_child(numbers[i])
    
    root.deleteNode(20)
    print(root.inorder_traversal())