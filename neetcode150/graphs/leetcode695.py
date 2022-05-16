from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    islands = max(islands, self._dfs(grid, i, j))

        return islands

    def _dfs(self, grid: List[List[int]], i: int, j: int) -> int:
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
            return 0

        grid[i][j] = 0

        return (
            1
            + self._dfs(grid, i + 1, j)
            + self._dfs(grid, i - 1, j)
            + self._dfs(grid, i, j + 1)
            + self._dfs(grid, i, j - 1)
        )
