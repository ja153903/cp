from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    row_hash = f"Row {i} has value {board[i][j]}"
                    col_hash = f"Col {j} has value {board[i][j]}"
                    box_hash = f"Box ({i // 3}, {j // 3}) has value {board[i][j]}"

                    hashes = [row_hash, col_hash, box_hash]

                    if any(hash in seen for hash in hashes):
                        return False

                    for hash in hashes:
                        seen.add(hash)

        return True
