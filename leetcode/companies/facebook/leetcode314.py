from collections import deque, defaultdict
from typing import List, Optional

from data_structures.tree import TreeNode


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        We want to use a level order approach here, but we want to keep track
        of the current vertical level it should be on.

        :param root:
        :return:
        """
        if not root:
            return []

        graph = defaultdict(list)
        queue = deque()

        queue.append((root, 0))

        while queue:
            front, level = queue.popleft()

            graph[level].append(front.val)

            if front.left:
                queue.append((front.left, level - 1))

            if front.right:
                queue.append((front.right, level + 1))

        result = sorted(
            [(key, value) for key, value in graph.items()], key=lambda t: t[0]
        )

        return [value for _, value in result]
