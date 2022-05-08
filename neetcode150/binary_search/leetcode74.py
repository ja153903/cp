from typing import List

from utilities.binary_search import binary_search


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rleft, rright = 0, len(matrix) - 1

        while rleft <= rright:
            rmid = rleft + (rright - rleft) // 2

            if matrix[rmid][0] <= target <= matrix[rmid][-1]:
                result = binary_search(matrix[rmid], target)
                return result != -1
            elif matrix[rmid][0] > target:
                rright = rmid - 1
            else:
                rleft = rmid + 1

        return False
