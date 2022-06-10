/**
 * 13. 3Sum
 * Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
 * such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
 *
 * Notice that the solution set must not contain duplicate triplets.
 *
 * @param {number[]} nums
 * @return {number[][]}
 */
const threeSum = function (nums) {
  const result = [];

  nums.sort((a, b) => a - b);

  for (let i = 0; i < nums.length - 2; i++) {
    if (i === 0 || (i > 0 && nums[i] !== nums[i - 1])) {
      let j = i + 1,
        k = nums.length - 1;

      while (j < k) {
        const current = nums[i] + nums[j] + nums[k];

        if (current === 0) {
          result.push([nums[i], nums[j], nums[k]]);

          while (j < k && nums[j] === nums[j + 1]) {
            j++;
          }

          while (j < k && nums[k] === nums[k - 1]) {
            k--;
          }

          j++;
          k--;
        } else if (current < 0) {
          j++;
        } else {
          k--;
        }
      }
    }
  }

  return result;
};

module.exports = { threeSum };
