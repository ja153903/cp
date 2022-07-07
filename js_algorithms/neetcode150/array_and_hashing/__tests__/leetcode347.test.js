const { topKFrequent } = require('../leetcode347');

test.each([
  { nums: [1, 1, 1, 2, 2, 3], k: 2, expected: [1, 2] },
  { nums: [1], k: 1, expected: [1] },
])('topKFrequent($nums, $k)', ({ nums, k, expected }) => {
  expect(topKFrequent(nums, k).sort()).toEqual(expected);
});
