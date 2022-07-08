function canFinish(numCourses: number, prerequisites: Array<Array<number>>) {
  const graph: Map<number, Array<number>> = new Map();
  const inorder: Array<number> = new Array(numCourses).fill(0);
  const visited: Set<number> = new Set();
  let count = 0;

  for (const [a, b] of prerequisites) {
    if (graph.has(b)) {
      graph.get(b)?.push(a);
    } else {
      graph.set(b, [a]);
    }

    inorder[a]++;
  }

  const queue: Array<number> = [];

  for (let i = 0; i < numCourses; i++) {
    if (inorder[i] === 0) {
      queue.push(i);
    }
  }

  while (queue.length) {
    const front = queue.shift() ?? -1;
    count++;

    visited.add(front);

    // go through each child
    for (const nextCourse of graph.get(front) ?? []) {
      inorder[nextCourse]--;

      if (inorder[nextCourse] === 0) {
        queue.push(nextCourse);
      }
    }
  }

  return count === numCourses;
}

export default canFinish;
