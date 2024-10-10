# Sources used: https://lut-dsa.cc.lut.fi/Books/LUTDSA/html/BST.html#bst-remove



# bintree.py


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
    
    def preorder(self): # I'm assuming we are supposed to actually give parameters to this.
        if self.root != None:
            self._preorderhelper(self.root)
        print() # Newline
        
    def _preorderhelper(self, node):
        print(node.key, end=" ")
        if node.left: # First right side
            self._preorderhelper(node.left)
        if node.right: # Then left side
            self._preorderhelper(node.right)


    def insert(self, key: int):
        if self.root == None: # If there is no root, create one.
            self.root = Node(key)
        self._inserthelper(self.root, key)


    def _inserthelper(self, node, key):
        if node == None:
            node == Node(key)
        if key < node.key:
            if node.left == None: # If there is no left node, insert left.
                node.left = Node(key)
            self._inserthelper(node.left, key)
        elif key > node.key:
            if node.right == None:
                node.right = Node(key)
            self._inserthelper(node.right, key)

    def search(self, key: int):
        def _search(node, key):
            if node == None:
                return False
            if key == node.key:
                return True
            if key < node.key:
                return _search(node.left, key)
            return _search(node.right, key)

        return _search(self.root, key)

    def remove(self, key: int):
        def _removemax(node): # Helper function got from the source we were told to use. Source: https://lut-dsa.cc.lut.fi/Books/LUTDSA/html/BST.html#bst-remove
            if node.right == None:
                return node.left
            node.right = _removemax(node.right)
            return node

        def _getmax(node): # Helper function got from the same source as above.
            if node.right == None:
                return node.key
            else:
                return _getmax(node.right)

        def _removehelper(node, key):
            if node == None:
                return node

            if key < node.key:
                node.left = _removehelper(node.left, key)
            elif key > node.key:
                node.right = _removehelper(node.right, key)
            else:
                if node.left == None:
                    return node.right
                elif node.right == None:
                    return node.left
                node.key = _getmax(node.left)
                node.left = _removemax(node.left)
            
            return node
            
        self.root = _removehelper(self.root, key)


    def postorder(self): 
        self._postorderhelper(self.root) # We don't need to use helper functions here but I wanted to be consistent.
        print() # Newline
    
    def _postorderhelper(self, node):
        if node.left: # First traverse left tree.
            self._postorderhelper(node.left)
        if node.right: # Then right tree.
            self._postorderhelper(node.right)
        print(node.key, end=" ") # Then visit the root.




    def inorder(self):
        self._inorderhelper(self.root)
        print() # Newline
    
    def _inorderhelper(self, node):
        if node.left: # First traverse left tree.
            self._inorderhelper(node.left)
        
        print(node.key, end=" ") # Then visit the root.
        
        if node.right: # Then traverse the right tree.
            self._inorderhelper(node.right)


        


if __name__ == "__main__":
    Tree = BST()
    keys = [5, 9, 1, 3, 7, 7, 4, 6, 2]

    for key in keys:
        Tree.insert(key)
   
    Tree.postorder()
    Tree.inorder()