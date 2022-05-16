from collections import deque
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        You are given an m x n grid rooms initialized with these three possible values.

        * -1 A wall or an obstacle.
        * 0 A gate.
        * INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to
          represent INF as you may assume that the distance to a gate is less than 2147483647.

        Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

        Do not return anything, modify rooms in-place instead.
        """
        queue = deque()

        INF = 2147483647

        for i, row in enumerate(rooms):
            for j, col in enumerate(row):
                if col == 0:
                    queue.append((i, j))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            x, y = queue.popleft()

            for dx, dy in directions:
                cx, cy = x + dx, y + dy

                if (
                    cx < 0
                    or cy < 0
                    or cx >= len(rooms)
                    or cy >= len(rooms[0])
                    or rooms[cx][cy] != INF
                ):
                    continue

                rooms[cx][cy] = rooms[x][y] + 1

                queue.append((cx, cy))
