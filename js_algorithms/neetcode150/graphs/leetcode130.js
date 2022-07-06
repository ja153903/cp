/**
 * @param {string[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
const solve = function (board) {
  // we should find a value 1 that is not
  // on the border and then do a DFS
  // as long as that value is not on the border
  const rows = board.length;
  if (rows === 0) {
    return;
  }

  const cols = board[0].length;

  // if there exists any Os on the boundary
  // we want to do a DFS and mark any connected Os with a 3rd character

  // go down first and last columns
  for (let i = 0; i < rows; i++) {
    if (board[i][0] === "O") {
      dfs(board, i, 0);
    }

    if (board[i][cols - 1] === "O") {
      dfs(board, i, cols - 1);
    }
  }

  // go over first and last rows
  for (let i = 0; i < cols; i++) {
    if (board[0][i] === "O") {
      dfs(board, 0, i);
    }

    if (board[rows - 1][i] === "O") {
      dfs(board, rows - 1, i);
    }
  }

  // after we've marked those, we should flip those with the 3rd character
  // back to the O and the ones that are still Os into Xs since those are
  // going to be legal flips
  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      if (board[i][j] === "#") {
        board[i][j] = "O";
      } else if (board[i][j] === "O") {
        board[i][j] = "X";
      }
    }
  }
};

/**
 * @param {string[][]} board
 * @param {number} i
 * @param {number} j
 */
function dfs(board, i, j) {
  if (
    i < 0 ||
    j < 0 ||
    i >= board.length ||
    j >= board[0].length ||
    board[i][j] !== "O"
  ) {
    return;
  }

  board[i][j] = "#";

  dfs(board, i + 1, j);
  dfs(board, i - 1, j);
  dfs(board, i, j + 1);
  dfs(board, i, j - 1);
}
