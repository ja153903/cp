from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        You are given an m x n grid where each cell can have one of three values:
            * 0 representing an empty cell,
            * 1 representing a fresh orange, or
            * 2 representing a rotten orange.

        Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

        Return the minimum number of minutes that must elapse until no cell has a fresh orange.
        If this is impossible, return -1.

        :param grid:
        :return:
        """
        fresh = 0
        minutes = 0
        queue = deque()
        rows, cols = len(grid), len(grid[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1

                if grid[i][j] == 2:
                    queue.append((i, j))

        if fresh == 0:
            return 0

        while queue and fresh > 0:
            minutes += 1
            size = len(queue)

            for _ in range(size):
                i, j = queue.popleft()

                for di, dj in directions:
                    ci, cj = i + di, j + dj
                    if (
                        ci < 0
                        or cj < 0
                        or ci >= rows
                        or cj >= cols
                        or grid[ci][cj] != 1
                    ):
                        continue

                    fresh -= 1

                    grid[ci][cj] = 2

                    queue.append((ci, cj))

        return minutes if fresh == 0 else -1
