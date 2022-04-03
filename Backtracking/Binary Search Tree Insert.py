"""
https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem
"""


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


def preOrder(root):
    if root == None:
        return
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Node is defined as
    # self.left (the left child of the node)
    # self.right (the right child of the node)
    # self.info (the value of the node)

    def insert(self, val):

        # edge case
        if self.root is None:  # empty tree, so insert
            self.root = Node(val)

        else:  # tree is not empty
            current = self.root  # current node

            while True:
                if val < current.info:  # search left subtree
                    if current.left is None:  # left subtree is empty, so insert
                        current.left = Node(val)
                        return

                    else:  # search left subtree
                        current = current.left

                else:  # search right subtree
                    if current.right is None:  # right subtree is empty, so insert
                        current.right = Node(val)
                        return

                    else:  # search right subtree
                        current = current.right


tree = BinarySearchTree()