/**
 * @param {character[][]} grid
 * @return {number}
 */
const numIslands = function (grid) {
  let result = 0;

  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      if (grid[i][j] === "1") {
        dfs(grid, i, j);
        result++;
      }
    }
  }

  return result;
};

function dfs(grid, i, j) {
  if (
    i < 0 ||
    j < 0 ||
    i >= grid.length ||
    j >= grid[0].length ||
    grid[i][j] !== "1"
  ) {
    return;
  }

  grid[i][j] = "#";

  dfs(grid, i + 1, j);
  dfs(grid, i - 1, j);
  dfs(grid, i, j + 1);
  dfs(grid, i, j - 1);
}

module.exports = { numIslands };
