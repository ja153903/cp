from typing import Optional

from data_structures.tree import TreeNode


class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def count(root: Optional[TreeNode], val: int) -> int:
            if not root:
                return 0

            max_value = max(root.val, val)

            # if the root value is currently greater than the value
            # then this means that we have an increasing path
            if root.val >= val:
                return 1 + count(root.left, max_value) + count(root.right, max_value)
            else:
                return count(root.left, max_value) + count(root.right, max_value)

        return count(root, root.val)
