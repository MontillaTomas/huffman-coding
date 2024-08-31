"""
This module contains the NodeTree class.
"""


class NodeTree(object):
    """
    A class that represents a node in a binary tree.
    """

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        """
        Returns the children of the node.

        Returns:
            tuple: A tuple containing the left and right children of the node.
        """
        return (self.left, self.right)
