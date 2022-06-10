/**
 * 42. Trapping Rain Water
 *
 * Given n non-negative integers representing an elevation map where the width of each bar is 1,
 * compute how much water it can trap after raining.
 *
 * TODO: Figure out how to explain this problem. I may know the answer, but I don't know how to explain the solution.
 *
 * @param {number[]} height
 * @return {number}
 */
const trap = function (height) {
  let left = 0,
    right = height.length - 1;
  let maxLeft = height[left],
    maxRight = height[right];
  let result = 0;

  while (left < right) {
    if (height[left] < height[right]) {
      if (height[left] > maxLeft) {
        maxLeft = height[left];
      } else {
        result += maxLeft - height[left];
      }
      left++;
    } else {
      if (height[right] > maxRight) {
        maxRight = height[right];
      } else {
        result += maxRight - height[right];
      }
      right--;
    }
  }

  return result;
};

module.exports = { trap };
