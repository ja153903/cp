const { maxArea } = require("../leetcode11");

test.each([{ height: [1, 8, 6, 2, 5, 4, 8, 3, 7], expected: 49 }])(
  "maxArea($height)",
  ({ height, expected }) => {
    expect(maxArea(height)).toBe(expected);
  }
);
