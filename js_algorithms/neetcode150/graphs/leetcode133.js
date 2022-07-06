function Node(val, neighbors) {
  this.val = val ?? 0;
  this.neighbors = neighbors ?? [];
}

/**
 * @param {Node} node
 * @return {Node}
 */
const cloneGraph = function (node) {
  if (!node) {
    return null;
  }

  // go through each node in the graph and
  // create copies as we iterate through the graph
  // we should keep track of nodes we've visited via a set
  const copies = new Map();
  const result = new Node(node.val);
  const queue = [];

  queue.push([result, node]);
  copies.set(node.val, result);

  while (queue.length) {
    const [copy, orig] = queue.shift();

    for (const neighbor of orig.neighbors) {
      if (copies.has(neighbor.val)) {
        copy.neighbors.push(copies.get(neighbor.val));
      } else {
        const neighborCopy = new Node(neighbor.val);
        copy.neighbors.push(neighborCopy);
        copies.set(neighbor.val, neighborCopy);
        queue.push([neighborCopy, neighbor]);
      }
    }
  }

  return result;
};

const n1 = new Node(1);
const n2 = new Node(2);
const n3 = new Node(3);
const n4 = new Node(4);

n1.neighbors.push(n2);
n1.neighbors.push(n4);
n2.neighbors.push(n3);
n2.neighbors.push(n1);
n3.neighbors.push(n2);
n3.neighbors.push(n4);
n4.neighbors.push(n3);
n4.neighbors.push(n1);

console.log(cloneGraph(n1));
