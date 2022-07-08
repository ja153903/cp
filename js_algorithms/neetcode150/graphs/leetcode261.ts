class UnionFind {
  parents: Array<number>;
  ranks: Array<number>;

  constructor(n: number) {
    this.parents = new Array(n).fill(0).map((_, index) => index);
    this.ranks = new Array(n).fill(0);
  }

  find(u: number): number {
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

function validTree(n: number, edges: number[][]): boolean {
  // if the nodes of an incoming edge have the same parent
  // this means that we can form a cycle

  const uf = new UnionFind(n);

  for (const [u, v] of edges) {
    const pu = uf.find(u);
    const pv = uf.find(v);

    if (pu === pv) {
      return false;
    }

    uf.union(u, v);
  }

  // we also have to check how many connected components there are
  const connectedComponents: Set<number> = new Set();
  for (let i = 0; i < n; i++) {
    connectedComponents.add(uf.find(i));
  }

  return connectedComponents.size === 1;
}

export default validTree;
