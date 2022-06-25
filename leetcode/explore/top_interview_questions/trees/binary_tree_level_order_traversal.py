from collections import deque
from typing import Optional, List
from data_structures.tree import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque()
        queue.append(root)

        while queue:
            size = len(queue)
            current = []
            for _ in range(size):
                front = queue.popleft()
                current.append(front.val)

                if front.left:
                    queue.append(front.left)

                if front.right:
                    queue.append(front.right)

            result.append(current)

        return result
