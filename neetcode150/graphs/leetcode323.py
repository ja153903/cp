from typing import List

from utilities.union_find import UnionFind


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        for u, v in edges:
            uf.union(u, v)

        return uf.num_connected_components
