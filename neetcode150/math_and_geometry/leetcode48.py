from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        When we're doing clockwise rotation, we reverse rows and then transpose.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        i, j = 0, rows - 1

        while i < j:
            matrix[i], matrix[j] = matrix[j], matrix[i]
            i += 1
            j -= 1

        for i in range(rows):
            for j in range(i + 1, cols):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
