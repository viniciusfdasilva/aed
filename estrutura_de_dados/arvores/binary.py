
import treelib

class Node():

    def __init__(self, val):
        self.val   = val
        self.right = None
        self.left  = None

class BinaryTree():

    def __init__(self, root):
        self.root = root
    
    def insert_callable(self, val):
        self.root = self.__insert(val, self.root)

    def __insert(self, val, node):
        if not node:
            node = Node(val)
            return node
        elif val < node.val:
            node.left = self.__insert(val, node.left)
            return node
        elif val > node.val:
            node.right = self.__insert(val, node.right)
            return node
        else:
            raise Exception('This element already exist!')

    def search_callable(self, val):
        return self.__search(val, self.root)

    def set_less(self, node_left, node_right):

        if not node_right:
            return node_left
        else:
            node_right.left = self.set_less(node_left, node_right.left)
            return node_right

    def __search(self, val, node):
        
        if not node:
            return False
        elif node.val == val:
            return True
        elif val < node.val:
            return self.__search(val, node.left)
        else:
            return self.__search(val, node.right)
    
    def remove_callable(self, val):
        self.root = self.__remove(val, self.root)

    def __remove(self, val, node):

        if not node:
            raise Exception('Value not found!')
        elif node.val == val:
            return self.set_less(node.left, node.right)
        elif val < node.val:
            node.left = self.__remove(val, node.left)
            return node
        else:
            node.right = self.__remove(val, node.right)
            return node

    def show_callable(self):
        tree = treelib.Tree()
        tree = self.__show(tree, self.root)
        tree.show()

    def __show(self, tree, node):

        if not node:
            return tree
        else:
            if node.left:
                tree = self.__show(tree, node.left)
                tree.create_node(node.left.val, node.left.val, parent=node.val)
            
            if node.right:
                tree = self.__show(tree, node.right)
                tree.create_node(node.right.val, node.right.val, parent=node.val)
            
            return tree

if __name__ == '__main__':

    tree = BinaryTree(Node(10))
    tree.insert_callable(1)
    tree.insert_callable(4)
    tree.insert_callable(0)
    tree.insert_callable(14)
    tree.insert_callable(22)

    tree.remove_callable(14)

    print(tree.search_callable(1))
    print(tree.search_callable(13))
    print(tree.search_callable(4))
    print(tree.search_callable(0))
    print(tree.search_callable(14))
    #print(tree.search_callable(22))
    #print(tree.search_callable(12))
    #print(tree.search_callable(15))
    #print(tree.search_callable(16))
    #print(tree.search_callable(-1))
#
    
    #tree.show_callable()
