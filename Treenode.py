class TreeNode:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value

    def insert(self,key_value):
        if key_value<self.value:

            if self.left is None:
                self.left= TreeNode(key_value)
            else:
                self.left.insert(key_value)

        else:
            if self.right is None:
                self.right = TreeNode(key_value)
            else:
                self.right.insert(key_value)

    def preorder_traversal(self):
        print(self.value)

        if self.left:
            self.left.preorder_traversal()

        if self.right:
            self.right.preorder_traversal()


    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()

        print(self.value)

        if self.right:
            self.right.inorder_traversal()



    def post_order_traversal(self):
        if self.left:
            self.left.post_order_traversal()

        if self.right:
            self.right.post_order_traversal()

        print(self.value)




if __name__=='__main__':
    tree_obj= TreeNode(17)

    tree_obj.insert(5)
    tree_obj.insert(4)
    tree_obj.insert(3)

    tree_obj.insert(23)
    tree_obj.insert(20)
    tree_obj.insert(18)

    print("\n Preorder Traversal: ")
    tree_obj.preorder_traversal()