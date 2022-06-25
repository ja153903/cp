from typing import Optional
from data_structures.tree import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # we can do an inorder traversal without recursion to solve this problem
        prev = None
        stack = []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if prev and root and prev.val >= root.val:
                return False
            else:
                prev = root

            if root:
                root = root.right

        return True
