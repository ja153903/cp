const { twoSum } = require('../leetcode1');

test.each([
  { nums: [2, 7, 11, 15], target: 9, expected: [0, 1] },
  { nums: [3, 2, 4], target: 6, expected: [1, 2] },
])('twoSum($nums, $target)', ({ nums, target, expected }) => {
  expect(twoSum(nums, target).sort()).toEqual(expected);
});
