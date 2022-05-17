class UnionFind:
    def __init__(self, num_nodes: int):
        self.num_nodes = num_nodes
        self.parent = [i for i in range(num_nodes)]
        self.rank = [0] * num_nodes

    def find(self, u: int) -> int:
        # This is the path compression version
        while self.parent[u] != u:
            self.parent[u] = self.parent[self.parent[u]]
            u = self.parent[u]

        return u

    def union(self, u: int, v: int) -> None:
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return

        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
            self.rank[pv] += 1
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1
