from typing import List, Set


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited = set()
                    if self._dfs(board, i, j, visited, word, 0):
                        return True

        return False

    def _dfs(
        self,
        board: List[List[str]],
        i: int,
        j: int,
        visited: Set[str],
        word: str,
        start: int,
    ) -> bool:
        if start == len(word):
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False

        if word[start] != board[i][j]:
            return False

        hash = f"{i},{j}"

        if hash in visited:
            return False

        visited.add(hash)

        result = (
            self._dfs(board, i + 1, j, visited, word, start + 1)
            or self._dfs(board, i - 1, j, visited, word, start + 1)
            or self._dfs(board, i, j + 1, visited, word, start + 1)
            or self._dfs(board, i, j - 1, visited, word, start + 1)
        )

        visited.remove(hash)

        return result
