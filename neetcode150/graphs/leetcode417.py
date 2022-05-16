from collections import deque
from typing import List, Deque, Tuple, Set


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean.
        The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the
        island's right and bottom edges.

        The island is partitioned into a grid of square cells. You are given an m x n integer matrix
        heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

        The island receives a lot of rain, and the rain water can flow to neighboring cells directly north,
        south, east, and west if the neighboring cell's height is less than or equal to the current cell's height.
         Water can flow from any cell adjacent to an ocean into the ocean.

        Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow
        from cell (ri, ci) to both the Pacific and Atlantic oceans.

        Approach:

        This problem looks like we need to return the intersection from both flows starting from the top left
        and from the bottom right.

        We stop the search once we hit a point that is greater than the previous node. If this node is in bounds,
        then we keep it and store it as a potential answer.

        :param heights:
        :return:
        """
        rows, cols = len(heights), len(heights[0])

        pacific, atlantic = deque(), deque()
        pacific_visited, atlantic_visited = set(), set()
        pacific_result, atlantic_result = set(), set()

        for i in range(rows):
            pacific.append((i, 0))
            atlantic.append((i, cols - 1))
            pacific_result.add((i, 0))
            atlantic_result.add((i, cols - 1))

        for i in range(cols):
            pacific.append((0, i))
            atlantic.append((rows - 1, i))
            pacific_result.add((0, i))
            atlantic_result.add((rows - 1, i))

        self._bfs(pacific, pacific_visited, pacific_result, heights)
        self._bfs(atlantic, atlantic_visited, atlantic_result, heights)

        intersection = pacific_result & atlantic_result

        return [[x, y] for x, y in intersection]

    @staticmethod
    def _bfs(
        queue: Deque[Tuple[int, int]],
        visited: Set[Tuple[int, int]],
        result: Set[Tuple[int, int]],
        heights: List[List[int]],
    ):
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        rows, cols = len(heights), len(heights[0])

        while queue:
            x, y = queue.popleft()

            visited.add((x, y))

            for dx, dy in directions:
                cx, cy = x + dx, y + dy
                if (
                    cx < 0
                    or cx >= rows
                    or cy < 0
                    or cy >= cols
                    or (cx, cy) in visited
                    # we check here if the current item is greater than
                    # the next one we might go to and skip it if its less
                    or heights[cx][cy] < heights[x][y]
                ):
                    continue

                result.add((cx, cy))

                queue.append((cx, cy))
