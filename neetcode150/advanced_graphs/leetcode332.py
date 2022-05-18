from collections import defaultdict
from typing import List, DefaultDict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        You are given a list of airline tickets where tickets[i] = [from_i, to_i] represent the departure and
        the arrival airports of one flight. Reconstruct the itinerary in order and return it.

        All the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK".
        If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order
        when read as a single string.

        For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
        You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

        Approach: This question involves finding an Euler path.

        An Euler path is a path in a graph that passes every edge exactly once

        Reference:
        https://leetcode.com/problems/reconstruct-itinerary/discuss/709590/Python-Short-Euler-Path-Finding-O(E-log-E)-explained.

        :param tickets:
        :return:
        """
        routes = []
        graph = defaultdict(list)

        for src, dst in tickets:
            graph[src].append(dst)

        for key, value in graph.items():
            graph[key] = sorted(value, reverse=True)

        self.dfs("JFK", graph, routes)

        return routes[::-1]

    def dfs(
        self, airport: str, graph: DefaultDict[str, List[str]], routes: List[str]
    ) -> None:
        while graph[airport]:
            candidate = graph[airport].pop()
            self.dfs(candidate, graph, routes)
        routes.append(airport)
