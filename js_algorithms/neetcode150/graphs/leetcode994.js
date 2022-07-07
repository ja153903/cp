/**
 * @param {number[][]} grid
 * @return {number}
 */
const orangesRotting = function (grid) {
  // count the number of fresh oranges
  // we can start making things rotten by doing a BFS around each rotten tomato
  const rows = grid.length;
  const cols = grid[0].length;
  let minutes = 0;
  let fresh = 0;
  let queue = [];

  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      if (grid[i][j] === 1) {
        fresh++;
      }

      if (grid[i][j] === 2) {
        queue.push([i, j]);
      }
    }
  }

  if (fresh === 0) {
    return 0;
  }

  while (queue.length) {
    const size = queue.length;
    minutes++;

    for (let i = 0; i < size; i++) {
      const [cx, cy] = queue.shift();

      for (
        const [dx, dy] of [
          [1, 0],
          [-1, 0],
          [0, 1],
          [0, -1],
        ]
      ) {
        const [nx, ny] = [cx + dx, cy + dy];

        if (
          nx < 0 ||
          ny < 0 ||
          nx >= rows ||
          ny >= cols ||
          grid[nx][ny] !== 1
        ) {
          continue;
        }

        grid[nx][ny] = 2;
        fresh--;

        queue.push([nx, ny]);
      }
    }
  }

  return fresh === 0 ? minutes - 1 : -1;
};
