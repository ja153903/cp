class UnionFind {
  parents: Array<number>;
  ranks: Array<number>;

  constructor(n: number) {
    this.parents = new Array(n).fill(0).map((_, index) => index);
    this.ranks = new Array(n).fill(0);
  }

  find(u: number): number {
    // implement with path compression
    while (u !== this.parents[u]) {
      this.parents[u] = this.parents[this.parents[u]];
      u = this.parents[u];
    }

    return u;
  }

  union(u: number, v: number): boolean {
    const pu = this.find(u);
    const pv = this.find(v);

    if (pu === pv) {
      return true;
    }

    if (this.ranks[pu] < this.ranks[pv]) {
      this.parents[pu] = pv;
      this.ranks[pv]++;
    } else {
      this.parents[pv] = pu;
      this.ranks[pu]++;
    }

    return false;
  }
}

function findRedundantConnection(edges: number[][]): number[] {
  const uf = new UnionFind(edges.length);

  for (const [u, v] of edges) {
    if (uf.union(u - 1, v - 1)) {
      return [u, v];
    }
  }

  return [];
}

export default findRedundantConnection;
