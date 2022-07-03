function ListNode(val, next) {
  this.val = val ?? 0;
  this.next = next ?? null;
}

/**
 * @param {number} m
 * @param {number} n
 * @param {ListNode} head
 * @return {number[][]}
 */
const spiralMatrix = function (m, n, head) {
  // we're given the spiral matrix in the form of a linked list
  // our job is to de-spiral it into the actual matrix form
  // the remaining items will be filled with -1
  const result = new Array(m).fill().map(() => new Array(n).fill(-1));

  if (!head) {
    return result;
  }

  let rowStart = 0;
  let colStart = 0;
  let rowEnd = m - 1;
  let colEnd = n - 1;

  while (head) {
    // go across
    for (let i = colStart; i <= colEnd; i++) {
      result[rowStart][i] = head?.val ?? -1;
      head = head?.next;
    }

    rowStart++;

    // go down
    for (let i = rowStart; i <= rowEnd; i++) {
      result[i][colEnd] = head?.val ?? -1;
      head = head?.next;
    }

    colEnd--;

    if (rowStart <= rowEnd) {
      // go back to colStart
      for (let i = colEnd; i >= colStart; i--) {
        result[rowEnd][i] = head?.val ?? -1;
        head = head?.next;
      }

      rowEnd--;
    }

    if (colStart <= colEnd) {
      // go back to colStart
      for (let i = rowEnd; i >= rowStart; i--) {
        result[i][colStart] = head?.val ?? -1;
        head = head?.next;
      }

      colStart++;
    }
  }

  return result;
};

export default spiralMatrix;
