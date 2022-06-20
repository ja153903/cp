/**
 * @param {number[]} nums
 * @return {number}
 */
const findMin = function (nums) {
  const n = nums.length;
  let left = 0;
  let right = n - 1;

  while (left < right) {
    const mid = left + Math.floor((right - left) / 2);
    if (nums[mid] > nums[right]) {
      left = mid + 1;
    } else {
      right = mid;
    }
  }

  return nums[left];
};

module.exports = { findMin };
