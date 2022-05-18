import heapq
from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def manhattan(p1: List[int], p2: List[int]) -> int:
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    # NOTE: This is a typical MST question (https://en.wikipedia.org/wiki/Minimum_spanning_tree)
    # Here is the Prim's algorithm solution (https://en.wikipedia.org/wiki/Prim%27s_algorithm)
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)
        nodes = len(points)

        # Create graph with weight via manhattan distance
        for i in range(nodes):
            for j in range(i + 1, nodes):
                dist = self.manhattan(points[i], points[j])
                graph[i].append((dist, j))
                graph[j].append((dist, i))

        count, ans = 1, 0
        visited, heap = [0] * nodes, graph[0]

        visited[0] = 1

        heapq.heapify(heap)

        while heap:
            dist, j = heapq.heappop(heap)
            if not visited[j]:
                visited[j] = 1
                count += 1
                ans += dist

                for record in graph[j]:
                    heapq.heappush(heap, record)

            if count >= nodes:
                break

        return ans
