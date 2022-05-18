from typing import List

from utilities.union_find import UnionFind


class ValidTreeUnionFind(UnionFind):
    def introduces_cycle(self, u: int, v: int) -> bool:
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return True

        if self.rank[pu] < self.rank[pv]:
            self.rank[pv] += 1
            self.parent[pu] = pv
        else:
            self.rank[pu] += 1
            self.parent[pv] = pu

        return False


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        You have a graph of n nodes labeled from 0 to n - 1.
        You are given an integer n and a list of edges where edges[i] = [ai, bi]
        indicates that there is an undirected edge between nodes ai and bi in the graph.

        Return true if the edges of the given graph make up a valid tree, and false otherwise.

        Approach:

        We know if it's a valid tree if there is no cycle.

        using union find, we know that an edge uv introduces a cycle, if u and v already share
        the same parent node

        :param n:
        :param edges:
        :return:
        """
        uf = ValidTreeUnionFind(n)

        for u, v in edges:
            # if the edge introduces a cycle, we know it's not a valid tree
            if uf.introduces_cycle(u, v):
                return False

        # the last check we need to do is make sure that we only have 1
        # connected component
        return uf.num_connected_components == 1
