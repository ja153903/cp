from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if col != ".":
                    row_msg = f"row {i} has value {col}"
                    col_msg = f"col {j} has value {col}"
                    grid_msg = f"grid {i // 3},{j // 3} has value {col}"

                    if row_msg in seen or col_msg in seen or grid_msg in seen:
                        return False

                    seen.add(row_msg)
                    seen.add(col_msg)
                    seen.add(grid_msg)

        return True
