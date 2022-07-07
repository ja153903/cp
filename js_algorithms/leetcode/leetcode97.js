/**
 * @param {string} s1
 * @param {string} s2
 * @param {string} s3
 * @return {boolean}
 */
function isInterleave(s1, s2, s3) {
  /**
   * Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
   * Output: true
   */

  if (s1.length + s2.length !== s3.length) {
    return false;
  }

  // Create queue for BFS
  const queue = [];
  const visited = new Set();
  visited.add('0,0');
  queue.push({ s1Ptr: 0, s2Ptr: 0 });

  while (queue.length) {
    const { s1Ptr, s2Ptr } = queue.shift();

    if (s1Ptr + s2Ptr === s3.length) {
      return true;
    }
    if (
      s1Ptr + 1 <= s1.length && s1[s1Ptr] === s3[s1Ptr + s2Ptr] &&
      !visited.has(`${s1Ptr + 1},${s2Ptr}`)
    ) {
      queue.push({ s1Ptr: s1Ptr + 1, s2Ptr });
      visited.add(`${s1Ptr + 1},${s2Ptr}`);
    }

    if (
      s2Ptr + 1 <= s2.length && s2[s2Ptr] === s3[s1Ptr + s2Ptr] &&
      !visited.has(`${s1Ptr},${s2Ptr + 1}`)
    ) {
      queue.push({ s1Ptr, s2Ptr: s2Ptr + 1 });
      visited.add(`${s1Ptr},${s2Ptr + 1}`);
    }
  }

  return false;
}

export default isInterleave;
