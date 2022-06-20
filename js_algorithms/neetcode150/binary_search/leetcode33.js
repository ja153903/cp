/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
const search = function (nums, target) {
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

  const pivot = left;

  left = 0;
  right = n - 1;

  while (left <= right) {
    const mid = left + Math.floor((right - left) / 2);
    const realMid = (mid + pivot) % n;

    if (nums[realMid] === target) {
      return realMid;
    } else if (nums[realMid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return -1;
};

module.exports = { search };
