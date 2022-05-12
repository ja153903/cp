from typing import Optional

from data_structures.tree import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # given a node, we want to make sure that the relationship follows
        # throughout the entire tree
        if not root:
            return True

        left = self._is_greater_than(root.val, root.left)
        if not left:
            return False

        right = self._is_less_than(root.val, root.right)
        if not right:
            return False

        return self.isValidBST(root.left) and self.isValidBST(root.right)

    def _is_less_than(self, val: int, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return (
            root.val > val
            and self._is_less_than(val, root.left)
            and self._is_less_than(val, root.right)
        )

    def _is_greater_than(self, val: int, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return (
            root.val < val
            and self._is_greater_than(val, root.left)
            and self._is_greater_than(val, root.right)
        )

    def iterative(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = []
        prev = None

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if prev and root.val <= prev.val:
                return False
            prev = root
            root = root.right

        return True
