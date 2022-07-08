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

  union(u: number, v: number) {
    const pu = this.find(u);
    const pv = this.find(v);

    if (pu === pv) {
      return;
    }

    if (this.ranks[pu] < this.ranks[pv]) {
      this.parents[pu] = pv;
      this.ranks[pv]++;
    } else {
      this.parents[pv] = pu;
      this.ranks[pu]++;
    }
  }
}

function countComponents(n: number, edges: number[][]): number {
  const uf = new UnionFind(n);
  for (const [u, v] of edges) {
    uf.union(u, v);
  }

  const result: Set<number> = new Set();

  for (let i = 0; i < n; i++) {
    result.add(uf.find(i));
  }

  return result.size;
}

export default countComponents;
