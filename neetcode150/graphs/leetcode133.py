from collections import defaultdict, deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        """
        Clone Graph

        Approach:
            * We should keep copies of the node within the hashmap probably?

        :param node:
        :return:
        """
        if not node:
            return node

        graph = defaultdict()

        visited = set()

        queue = deque()
        queue.append(node)

        while queue:
            front = queue.popleft()

            if front.val in visited:
                continue

            visited.add(front.val)

            if front.val not in graph:
                graph[front.val] = Node(front.val)

            for neighbor in front.neighbors:
                if neighbor.val not in graph:
                    graph[neighbor.val] = Node(neighbor.val)

                graph[front.val].neighbors.append(graph[neighbor.val])

                if neighbor.val not in visited:
                    queue.append(neighbor)

        return graph[node.val]
