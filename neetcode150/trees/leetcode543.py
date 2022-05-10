from typing import Optional

from data_structures.tree import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_depth = 0

        def depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left = depth(node.left)
            right = depth(node.right)

            nonlocal max_depth
            max_depth = max(max_depth, left + right)

            return max(left, right) + 1

        depth(root)

        return max_depth
