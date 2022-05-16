from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        Two cells are connected if they are adjacent cells connected horizontally or vertically.

        Surrounded regions should not be on the border, which means that any 'O' on the border of the board
        are not flipped to 'X'. Any 'O' that is not on the border, and it is not connected to an 'O' on the
        border will be flipped to 'X'.

        What we're doing here is we're masking
        """
        rows, cols = len(board), len(board[0])

        if rows == 0:
            return

        for i in range(rows):
            if board[i][0] == "O":
                self.dfs(board, i, 0)

            if board[i][cols - 1] == "O":
                self.dfs(board, i, cols - 1)

        for i in range(cols):
            if board[0][i] == "O":
                self.dfs(board, 0, i)

            if board[rows - 1][i] == "O":
                self.dfs(board, rows - 1, i)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"

    def dfs(self, board: List[List[str]], i: int, j: int) -> None:
        rows, cols = len(board), len(board[0])

        if i < 0 or j < 0 or i >= rows or j >= cols or board[i][j] != "O":
            return

        board[i][j] = "#"

        self.dfs(board, i + 1, j)
        self.dfs(board, i - 1, j)
        self.dfs(board, i, j + 1)
        self.dfs(board, i, j - 1)
