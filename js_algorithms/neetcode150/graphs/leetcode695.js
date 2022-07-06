/**
 * @param {number[][]} grid
 * @return {number}
 */
const maxAreaOfIsland = function (grid) {
  // if we find a 1, we DFS, returning the number of 1s that exist on the island
  // we keep track of max area this way
  let result = 0;

  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      if (grid[i][j] === 1) {
        result = Math.max(result, dfs(grid, i, j));
      }
    }
  }

  return result;
};

/**
 * @param {number[][]} grid
 * @param {number} i
 * @param {number} j
 * @return {number}
 */
const dfs = function (grid, i, j) {
  if (
    i < 0 ||
    i >= grid.length ||
    j < 0 ||
    j >= grid[0].length ||
    grid[i][j] !== 1
  ) {
    return 0;
  }

  grid[i][j] = -1;

  return (
    1 +
    dfs(grid, i + 1, j) +
    dfs(grid, i - 1, j) +
    dfs(grid, i, j + 1) +
    dfs(grid, i, j - 1)
  );
};
