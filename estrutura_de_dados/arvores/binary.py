
class Node():

    def __init__(self, val):
        self.val   = val
        self.right = None
        self.left  = None

class BinaryTree():

    def __init__(self, root):
        self.root = root
    
    def insert(self, val):

        node = self.root
        