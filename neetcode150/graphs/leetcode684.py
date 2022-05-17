from typing import List

from utilities.union_find import UnionFind


class SolutionUnionFind(UnionFind):
    # Extended UnionFind class to allow for overrided union function
    # This union function will return False if there already exists
    # some path between two nodes
    def union(self, u: int, v: int) -> bool:
        pu = self.find(u)
        pv = self.find(v)

        # we return false here if we already
        # have connection between the two nodes
        if pu == pv:
            return False

        if self.rank[pu] < self.rank[pv]:
            self.rank[pv] += 1
            self.parent[pu] = pv
        else:
            self.rank[pu] += 1
            self.parent[pv] = pu

        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = SolutionUnionFind(len(edges))

        for u, v in edges:
            # if there already exists a connection between u and v
            # then this is a redundant edge.
            if not uf.union(u - 1, v - 1):
                return [u, v]

        return []

    def brute_force(self, edges: List[List[int]]) -> List[int]:
        """
        In this problem, a tree is an undirected graph that is connected and has no cycles.

        You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added.
        The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.
        The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge
        between nodes ai and bi in the graph.

        Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple
        answers, return the answer that occurs last in the input.

        :param edges:
        :return:
        """

        results = []

        for i, edge in enumerate(edges):
            to_skip = i

            uf = self._build_uf(edges, to_skip)

            if self.has_one_connected_component(uf):
                results.append(edge)

        return results[-1]

    @staticmethod
    def _build_uf(edges: List[List[int]], to_skip: int) -> UnionFind:
        uf = UnionFind(len(edges))

        for i, (u, v) in enumerate(edges):
            if to_skip == i:
                continue

            uf.union(u - 1, v - 1)

        return uf

    @staticmethod
    def has_one_connected_component(uf: UnionFind) -> bool:
        parents = set()
        n = uf.num_nodes

        for i in range(n):
            parents.add(uf.find(i))

        return len(parents) == 1
