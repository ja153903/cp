/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
const maxSlidingWindow = function (nums, k) {
  // keep track of indices of certain numbers
  const deque = [];
  const result = [];

  for (let i = 0; i < nums.length; i++) {
    // if i - last > k, then its out of the window
    while (deque.length && i - deque[0] >= k) {
      deque.shift();
    }

    while (deque.length && nums[deque[deque.length - 1]] < nums[i]) {
      deque.pop();
    }

    deque.push(i);

    if (i >= k - 1) {
      result.push(nums[deque[0]]);
    }
  }

  return result;
};

module.exports = maxSlidingWindow;
