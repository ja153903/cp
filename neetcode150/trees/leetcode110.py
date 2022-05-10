from typing import Optional

from data_structures.tree import TreeNode
from utilities.tree import height


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Given a binary tree, determine if it is height-balanced.

        For this problem, a height-balanced binary tree is defined as:
            a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

        :param root:
        :return:
        """
        if not root:
            return True

        left = height(root.left)
        right = height(root.right)

        if abs(left - right) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)
