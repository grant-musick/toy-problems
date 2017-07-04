from __future__ import division, absolute_import, print_function, unicode_literals

import unittest


# Tree of trees approach
class BinarySearchTree(object):

    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


    def is_leaf(self):
        return self.left == self.right == None

    def insert(self, value):
        if self.value == None:
            self.value = value
        elif value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value=value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = BinarySearchTree(value=value)
            else:
                self.right.insert(value)


    def remove(self, value):
        pass



def in_order(root, accum=[]):
    if root is None:
        return
    in_order(root.left, accum)
    accum.append(root.value)
    in_order(root.right, accum)

def pre_order(root, accum=[]):
    if root is None:
        return
    accum.append(root.value)
    pre_order(root.left, accum)
    pre_order(root.right, accum)

def post_order(root, accum=[]):
    if root is None:
        return
    post_order(root.left, accum)
    post_order(root.right, accum)
    accum.append(root.value)




class BinarySearchTreeTest(unittest.TestCase):

    def setUp(self):
        self.tree = BinarySearchTree()
        self.tree.insert(4)        
        self.tree.insert(2)        
        self.tree.insert(3)        
        self.tree.insert(1)
        self.tree.insert(6)
        self.tree.insert(5)

    def test_insert(self):
        tree = self.tree
        self.assertEqual(4, tree.value)
        self.assertEqual(2, tree.left.value)
        self.assertEqual(6, tree.right.value)
        self.assertEqual(1, tree.left.left.value)
        self.assertEqual(3, tree.left.right.value)
        self.assertEqual(5, tree.right.left.value)

    def test_in_order(self):
        tree = self.tree
        expected = [1,2,3,4,5,6]
        accum = []
        in_order(tree, accum)
        self.assertListEqual(expected, accum)

    def test_pre_order(self):
        tree = self.tree
        expected = [4,2,1,3,6,5]
        accum = []
        pre_order(tree, accum)
        self.assertListEqual(expected, accum)

    def test_post_order(self):
        tree = self.tree
        expected = [1,3,2,5,6,4]
        accum = []
        post_order(tree, accum)
        self.assertListEqual(expected, accum)





if __name__ == "__main__":
    unittest.main()