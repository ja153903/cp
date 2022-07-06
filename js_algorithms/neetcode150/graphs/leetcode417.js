/**
 * @param {number[][]} heights
 * @return {number[][]}
 */
const pacificAtlantic = function (heights) {
  // how to solve this problem?
  // we can have two queues stemming from pacific and atlantic
  // from those starting points, we then continually add items to
  // the queue if the value is greater than or equal to the previous one
  // we processed from the queue

  // we put items here that end up reaching specific oceans
  const atlantic = [];
  const pacific = [];

  const atlanticQueue = [];
  const pacificQueue = [];

  const atlanticVisited = new Set();
  const pacificVisited = new Set();

  // how do we initialize these values?

  const rows = heights.length;
  const cols = heights[0].length;

  for (let i = 0; i < rows; i++) {
    pacificQueue.push([i, 0]);
    atlanticQueue.push([i, cols - 1]);

    pacific.push([i, 0]);
    atlantic.push([i, cols - 1]);
  }

  for (let i = 0; i < cols; i++) {
    pacificQueue.push([0, i]);
    atlanticQueue.push([rows - 1, i]);

    pacific.push([0, i]);
    atlantic.push([rows - 1, i]);
  }

  // for each value in each queue, we should do a bfs
  bfs(heights, pacific, pacificQueue, pacificVisited);
  bfs(heights, atlantic, atlanticQueue, atlanticVisited);

  // find the intersection between pacific and atlantic
  const pacificHashes = new Set(pacific.map((key) => `${key[0]},${key[1]}`));
  const atlanticHashes = new Set(atlantic.map((key) => `${key[0]},${key[1]}`));

  return Array.from(
    new Set([...pacificHashes].filter((key) => atlanticHashes.has(key)))
  ).map((key) => key.split(",").map((item) => parseInt(item)));
};

/**
 * @param {number[][]} heights
 * @param {number[][]} result
 * @param {number[][]} queue
 * @param {Set<string>} visited
 */
function bfs(heights, result, queue, visited) {
  while (queue.length) {
    const front = queue.shift();

    visited.add(`${front[0]},${front[1]}`);

    for (const [dx, dy] of [
      [1, 0],
      [-1, 0],
      [0, 1],
      [0, -1],
    ]) {
      const [cx, cy] = [front[0] + dx, front[1] + dy];
      const hash = `${cx},${cy}`;

      if (
        cx < 0 ||
        cy < 0 ||
        cx >= heights.length ||
        cy >= heights[0].length ||
        heights[cx][cy] < heights[front[0]][front[1]] ||
        visited.has(hash)
      ) {
        continue;
      }

      result.push([cx, cy]);
      queue.push([cx, cy]);
    }
  }
}
