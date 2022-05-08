from typing import Optional, Tuple

from data_structures.tree import TreeNode


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def _compute(node: Optional[TreeNode]) -> Tuple[int, int]:
            nonlocal result

            if node is None:
                return 0, 0
            elif node.left is None and node.right is None:
                result += 1

                return node.val, 1
            else:
                left_sum, left_count = _compute(node.left)
                right_sum, right_count = _compute(node.right)

                _sum, _count = (
                    left_sum + right_sum + node.val,
                    left_count + right_count + 1,
                )

                if _sum // _count == node.val:
                    result += 1

                return _sum, _count

        _compute(root)

        return result
