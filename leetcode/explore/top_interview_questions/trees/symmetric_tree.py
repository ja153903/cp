from typing import Optional
from data_structures.tree import TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.helper(root.left, root.right)

    def helper(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right:
            return True

        if not left or not right:
            return False

        return (
            left.val == right.val
            and self.helper(left.left, right.right)
            and self.helper(left.right, right.left)
        )
