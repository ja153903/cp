/**
 * 36. Valid Sudoku
 *
 * Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
 *  1. Each row must contain the digits 1-9 without repetition.
 *  2. Each column must contain the digits 1-9 without repetition.
 *  3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
 *
 * Note:
 * - A Sudoku board (partially filled) could be valid but is not necessarily solvable.
 * - Only the filled cells need to be validated according to the mentioned rules.
 *
 * @param {character[][]} board
 * @return {boolean}
 */
const isValidSudoku = function (board) {
  const seen = new Set();

  for (let row = 0; row < 9; row++) {
    for (let col = 0; col < 9; col++) {
      if (board[row][col] !== '.') {
        const rowHash = `Row ${row} has value ${board[row][col]}`;
        const colHash = `Col ${col} has value ${board[row][col]}`;
        const subBoxHash = `SubBoxHash (${Math.floor(row / 3)}, ${
          Math.floor(
            col / 3,
          )
        }) has value ${board[row][col]}`;

        if (seen.has(rowHash) || seen.has(colHash) || seen.has(subBoxHash)) {
          return false;
        }

        for (const hash of [rowHash, colHash, subBoxHash]) {
          seen.add(hash);
        }
      }
    }
  }

  return true;
};

module.exports = { isValidSudoku };
