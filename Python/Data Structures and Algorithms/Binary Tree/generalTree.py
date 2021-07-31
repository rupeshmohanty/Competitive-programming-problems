class TreeNode:
    # Constructor!
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None
    
    # Adding child to a root node!
    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    # getting the level of the element!
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    # print the tree!
    def print_tree(self):
        # adding some space based on the level of the element!
        spaces = ' '*self.get_level()*3
        
        if self.parent:
            prefix = spaces + '|__'
        else:
            prefix = ""

        print(prefix + self.data)
        if self.children:
            for child in self.children:
                # printing the subcategories for the specific branch or node!
                child.print_tree()

def build_product_tree():
    # Setting the root!
    root = TreeNode("Electronics")

    # adding first branch!
    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    # adding second branch!
    cellphone = TreeNode("Cellphone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    # adding third branch!
    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root

if __name__ == "__main__":
    root = build_product_tree()
    root.print_tree()