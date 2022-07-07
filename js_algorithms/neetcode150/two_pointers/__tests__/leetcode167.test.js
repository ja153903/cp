const { twoSum } = require('../leetcode167');

test.each([{ numbers: [2, 7, 11, 15], target: 9, expected: [1, 2] }])(
  '',
  ({ numbers, target, expected }) => {
    expect(twoSum(numbers, target)).toEqual(expected);
  },
);
