const { threeSum } = require('../leetcode13');

test.each([
  {
    nums: [-1, 0, 1, 2, -1, -4],
    expected: [
      [-1, -1, 2],
      [-1, 0, 1],
    ],
  },
])('threeSum($nums)', ({ nums, expected }) => {
  expect(threeSum(nums)).toEqual(expected);
});
