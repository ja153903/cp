from typing import List

from data_structures.trie import Trie, TrieNode


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Given an m x n board of characters and a list of strings words, return all words on the board.

        Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally
        or vertically neighboring. The same letter cell may not be used more than once in a word.

        NOTE: Although this solution is correct, it is now TLE for Python 3 on LeetCode.

        :param board:
        :param words:
        :return:
        """
        result = []
        trie = Trie()

        for word in words:
            trie.insert(word)

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, trie.root, i, j, "", result)

        return result

    def dfs(
        self,
        board: List[List[str]],
        root: TrieNode,
        i: int,
        j: int,
        path: str,
        result: List[str],
    ) -> None:
        if root.has_word:
            result.append(path)
            root.has_word = False

        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            return

        tmp = board[i][j]
        root = root.children.get(tmp)
        if not root:
            return

        board[i][j] = "#"
        ext = f"{path}{tmp}"
        self.dfs(board, root, i + 1, j, ext, result)
        self.dfs(board, root, i - 1, j, ext, result)
        self.dfs(board, root, i, j + 1, ext, result)
        self.dfs(board, root, i, j - 1, ext, result)
        board[i][j] = tmp
