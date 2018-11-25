class TreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


"""
QUESTION 1
============================================================
Write a function "build_tree" that takes a list and other arguments
to construct a full binary tree that consists of nodes.
The TreeNode class is defined above.


Example 1:
===============================
The list [1, 3, None] should return a tree like:

   1
  / \
 3  None

Example 2:
===============================
The list [9, 7, 12, None, None, 3, None] should return a tree like:

           9
        /     
       7      12
     /  \    /  
 None  None 3  None
"""


def build_tree(root, my_list, i):
    if i < len(my_list):
        if my_list[i] is None:
            return None
        else:
            root = TreeNode(my_list[i])
            root.left = build_tree(root.left, my_list, 2*i+1)
            root.right = build_tree(root.right, my_list, 2*i+2)
            return root
    return root


"""
QUESTION 2
============================================================
Write tests for "build_tree" function in test_build_tree.py in directory tests.
"""

"""
QUESTION 3
============================================================
Write a binary class tree with name "BinaryClass" that 

- initializes the tree for a given "node" as an argument and assigns it
to an attribute of the class which is also called "node"; also creates new
attributes "left" and "right" which are "None" by default.

- has a method called "add_left" that takes a new node as an argument
and assigns it to the left node of the tree.

- has a method called "add_right" that takes a new node as an argument
and assigns it to the right node of the tree.

- has a method is_leaf that returns True if the tree does not have any
children.
"""

"""
QUESTION 4
============================================================
Write tests for "BinaryTree" class in test_binary_tree.py in directory tests.
"""


class BinaryTree(object):
    def __init__(self, node, left=None, right=None):
        self.node = node
        self.left = left
        self.right = right

    def add_left(self, left_node):
        self.left = BinaryTree(left_node)

    def add_right(self, right_node):
        self.right = BinaryTree(right_node)

    def is_leaf(self):
        if self.left is None and self.right is None:
            return True
        return False
