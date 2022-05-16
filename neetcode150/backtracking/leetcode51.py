from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        The n-queens puzzle is the problem of placing n queens on an n x n chessboard
        such that no two queens attack each other.

        Given an integer n, return all distinct solutions to the n-queens puzzle.
        You may return the answer in any order.

        Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.'
        both indicate a queen and an empty space, respectively.

        Approach:

        For this problem, we should probably enumerate all possible positions we can try to get a queen in
        Any time we fail to put a queen, we can stop that path and start again.

        :param n:
        :return:
        """
        result = []

        grid = [["." for _ in range(n)] for _ in range(n)]

        self._backtrack(grid, result, n, 0)

        return result

    def _backtrack(
        self, grid: List[List[str]], result: List[List[str]], n: int, row: int
    ) -> None:
        if row == n:
            result.append(list(["".join(row) for row in grid]))
            return

        for i in range(n):
            if self._is_valid(grid, i, row, n):
                grid[row][i] = "Q"
                self._backtrack(grid, result, n, row + 1)
                grid[row][i] = "."

    @staticmethod
    def _is_valid(grid: List[List[str]], col: int, row: int, n: int) -> bool:
        # check above
        for i in range(row):
            if grid[i][col] == "Q":
                return False

        # check diagonal above
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if grid[i][j] == "Q":
                return False

        # check other diagonal above
        for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
            if grid[i][j] == "Q":
                return False

        return True
