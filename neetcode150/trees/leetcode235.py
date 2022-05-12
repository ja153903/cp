from typing import Optional

from data_structures.tree import TreeNode


class Solution:
    def lowestCommonAncestor(
        self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        """
        Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

        According to the definition of LCA on Wikipedia:
        “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has
        both p and q as descendants (where we allow a node to be a descendant of itself).”

        :param root:
        :param p:
        :param q:
        :return:
        """
        if not root:
            return None

        if root == p:
            return p

        if root == q:
            return q

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left if left else right
