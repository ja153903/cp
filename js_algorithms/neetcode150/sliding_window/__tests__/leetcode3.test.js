const { lengthOfLongestSubstring } = require("../leetcode3");

test.each([
  { s: "abcabcbb", expected: 3 },
  { s: "bbbbb", expected: 1 },
  { s: "pwwkew", expected: 3 },
])("lengthOfLongestSubstring($s)", ({ s, expected }) => {
  expect(lengthOfLongestSubstring(s)).toBe(expected);
});
