from typing import List
from collections import deque


class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        """
        We can try to do a BFS for this problem

        TODO: Figure out how to optimize this problem

        :param grid:
        :return:
        """
        if grid[0][0] == ")":
            return False

        queue = deque()
        queue.append((0, 0, grid[0][0]))

        candidates = []

        while queue:
            i, j, path = queue.popleft()

            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                candidates.append(path)

            # can we optimize our path here by only going into the direction
            # if we need to add a particular character?
            # that probably seems like the right way to go with this question

            # go down
            if i + 1 < len(grid):
                queue.append((i + 1, j, f"{path}{grid[i + 1][j]}"))

            # go right
            if j + 1 < len(grid[0]):
                queue.append((i, j + 1, f"{path}{grid[i][j + 1]}"))

        for candidate in candidates:
            stack = []
            is_invalid = False

            for ch in candidate:
                if ch == "(":
                    stack.append(")")
                elif not stack or stack.pop() != ch:
                    is_invalid = True
                    break

            if not stack and not is_invalid:
                return True

        return False
