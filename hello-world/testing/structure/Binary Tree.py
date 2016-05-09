class BinaryTree(object):
    class TreeNode(object):
        def __init__(self, value=None, left=None, right=None):
            self.val = value
            self.left = left
            self.right = right

        def __eq__(self, other):
            return self.val == other

        def __ne__(self, other):
            return self.val != other

    def __init__(self):
        self.root = self.TreeNode()
        self._len = 0

    def get_root(self):
        return self.root.val

    def get_left(self, node):
        if node != None:
            return node.left
        else:
            return

    def get_right(self, node):
        if node != None:
            return node.right
        else:
            return

    def add_root(self, value=0):
        new_node = self.TreeNode(value)
        self.root = new_node
        return self.root

    def add_left(self,parent,value):
        if parent.left != None:
            raise ValueError('parent already had a left child')
        new_node = self.TreeNode(value)
        parent.left = new_node
        return parent.left

    def add_right(self,parent,value):
        if parent.right != None:
            raise ValueError('parent already had a right child')
        new_node = self.TreeNode(value)
        parent.right = new_node
        return parent.right

    def replace(self, old, value):
        old.val = value
        return old

    def pre_order(self,node):
        if node == None:
            return
        else:
            print node.val
            self.pre_order(node.left)
            self.pre_order(node.right)
            return node

    def depth_of(self, node):
        '''
        :param node: tree node
        :return: depth of that node, depth of root is 1
        '''
        if node == None:
            return 0
        else :
            return 1 + max(self.depth_of(node.left), self.depth_of(node.right))

    def max_depth(self):
        '''
        :return: max depth of the tree
        '''
        return self.depth_of(self.root)

    def invert_tree(self):
        """
            :type root: TreeNode
            :rtype: TreeNode
        """
        def inver(root):
             if root != None:
                inver(root.left)
                inver(root.right)
                root.left, root.right = root.right, root.left
        return inver(self.root)

tree = BinaryTree()
root = tree.add_root(0)
root_left = tree.add_left(root,10)
root_right = tree.add_right(root,20)
tree.add_left(root_left,12)

print root.val, root.left.val, root.right.val
print tree.maxDepth()
print tree.depth_of(root_left)
print 'travesing' , tree.pre_order(root)
tree.invert_tree()
print 'invert-traversing', tree.pre_order(root)
print tree.get_left(root).val
