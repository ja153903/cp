/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
const searchMatrix = function (matrix, target) {
  // instead of treating this as a matrix, we can treat this as a sorted list
  // This list has length row * cols
  const rows = matrix.length;
  const cols = matrix[0].length;

  let left = 0;
  let right = rows * cols - 1;

  while (left <= right) {
    const mid = left + Math.floor((right - left) / 2);
    // mid / cols gives us which group
    // mid % cols gives us the position within the group
    const value = matrix[Math.floor(mid / cols)][mid % cols];

    if (value === target) {
      return true;
    } else if (value < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return false;
};

module.exports = { searchMatrix };
