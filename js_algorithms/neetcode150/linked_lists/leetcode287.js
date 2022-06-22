/**
 * @param {number[]} nums
 * @return {number}
 */
const findDuplicate = function (nums) {
  if (nums.length <= 1) {
    return -1;
  }

  let slow = nums[0];
  let fast = nums[nums[0]];

  // run the slow-fast pointer until we hit the same element
  while (slow !== fast) {
    slow = nums[slow];
    fast = nums[nums[fast]];
  }

  // once we do that, we should find the duplicate
  // which is the entry point for this cycle
  fast = 0;

  while (slow !== fast) {
    slow = nums[slow];
    fast = nums[fast];
  }

  return slow;
};

module.exports = { findDuplicate };
