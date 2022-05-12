from typing import Optional

from data_structures.tree import TreeNode


class Solution:
    """
    Reference: https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/603423/Python-Recursion-stack-thinking-process-diagram

    If in doubt, always go back to that link.
    """

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = float("-inf")

        def get_max_gain(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            # we only care for achieving the max gains on the left and right paths
            left_gain = max(get_max_gain(node.left), 0)
            right_gain = max(get_max_gain(node.right), 0)

            current_max_path = node.val + left_gain + right_gain

            nonlocal result
            result = max(result, current_max_path)

            return node.val + max(left_gain, right_gain)

        get_max_gain(root)

        return result
