from typing import List, Optional

from data_structures.tree import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder will tell us what the root will be
        # inorder will tell us how to filter left and right subtrees
        if not inorder:
            return None

        index = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[index])

        left = inorder[:index]
        right = inorder[index + 1 :]

        root.left = self.buildTree(preorder, left)
        root.right = self.buildTree(preorder, right)

        return root
