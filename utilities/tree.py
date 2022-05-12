from collections import deque
from typing import Optional, List

from data_structures.tree import TreeNode


def height(node: Optional[TreeNode]) -> int:
    if not node:
        return 0

    left, right = height(node.left), height(node.right)

    return max(left, right) + 1


def is_same_tree(s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
    if not s and not t:
        return True

    if not s or not t:
        return False

    return (
        s.val == t.val
        and is_same_tree(s.left, t.left)
        and is_same_tree(s.right, t.right)
    )


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    result = []
    queue = deque()
    queue.append(root)

    while queue:
        size = len(queue)
        sub_result = []
        for _ in range(size):
            front = queue.popleft()
            sub_result.append(front.val)

            if front.left:
                queue.append(front.left)

            if front.right:
                queue.append(front.right)

        result.append(sub_result)

    return result
