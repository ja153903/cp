const { containsDuplicate } = require('../leetcode217');

test.each([
  { nums: [1, 2, 3, 1], expected: true },
  { nums: [], expected: false },
  { nums: [1, 2, 3, 4], expected: false },
])('containsDuplicate($nums)', ({ nums, expected }) => {
  expect(containsDuplicate(nums)).toBe(expected);
});
