const { productExceptSelf } = require("../leetcode238");

test.each([
  { nums: [1, 2, 3, 4], expected: [24, 12, 8, 6] },
  { nums: [-1, 1, 0, -3, 3], expected: [0, 0, 9, 0, 0] },
])("productExceptSelf($nums)", ({ nums, expected }) => {
  // NOTE: For some reason 0s are signed and give a problem here
  expect(productExceptSelf(nums).map((num) => num >> 0)).toEqual(expected);
});
