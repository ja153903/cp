from typing import Optional

from data_structures.tree import TreeNode


def height(node: Optional[TreeNode]) -> int:
    if not node:
        return 0

    left, right = height(node.left), height(node.right)

    return max(left, right) + 1
