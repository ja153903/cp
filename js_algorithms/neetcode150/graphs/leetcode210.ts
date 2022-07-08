function findOrder(numCourses: number, prerequisites: number[][]): number[] {
  const result: number[] = [];

  const graph: Map<number | null, number[]> = new Map();
  const inorder: number[] = new Array(numCourses).fill(0);
  const queue: number[] = [];

  for (const [a, b] of prerequisites) {
    if (graph.has(b)) {
      graph.get(b)?.push(a);
    } else {
      graph.set(b, [a]);
    }
    inorder[a]++;
  }

  inorder.forEach((value, index) => {
    if (value === 0) {
      queue.push(index);
    }
  });

  while (queue.length) {
    const front = queue.shift() ?? null;

    if (front !== null) {
      result.push(front);
    }

    for (const next of graph.get(front) ?? []) {
      inorder[next]--;

      if (inorder[next] === 0) {
        queue.push(next);
      }
    }
  }

  return result.length === numCourses ? result : [];
}

export default findOrder;
