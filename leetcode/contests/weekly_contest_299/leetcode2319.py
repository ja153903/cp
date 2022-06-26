from typing import List


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)

        diagonals = set([(i, i) for i in range(n)])

        for i, j in zip(range(n - 1, -1, -1), range(n)):
            diagonals.add((i, j))

        for row in range(n):
            for col in range(n):
                if (row, col) in diagonals:
                    if grid[row][col] == 0:
                        return False
                else:
                    if grid[row][col] != 0:
                        return False

        return True
