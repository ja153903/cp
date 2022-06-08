/**
 * 128. Longest Consecutive Sequence
 *
 * Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
 *
 * You must write an algorithm that runs in O(n) time.
 *
 * @param {number[]} nums
 * @return {number}
 */
const longestConsecutive = function (nums) {
  const uniqueNums = new Set(nums);
  let longestSeq = 0;

  for (const num of nums) {
    if (!uniqueNums.has(num - 1)) {
      let current = num;
      let currentSeq = 0;

      while (uniqueNums.has(current)) {
        currentSeq++;
        current++;
      }

      longestSeq = Math.max(longestSeq, currentSeq);
    }
  }

  return longestSeq;
};

module.exports = { longestConsecutive };
