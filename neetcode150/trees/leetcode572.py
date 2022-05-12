from typing import Optional

from data_structures.tree import TreeNode
from utilities.tree import is_same_tree


class Solution:
    def isSubtree(self, root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
        if not root and not sub_root:
            return True

        if not root or not sub_root:
            return False

        result = False

        if root.val == sub_root.val:
            result = is_same_tree(root, sub_root)

        return (
            result
            or self.isSubtree(root.left, sub_root)
            or self.isSubtree(root.right, sub_root)
        )
