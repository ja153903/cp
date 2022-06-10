const { checkInclusion } = require("../leetcode567");

test.each([
  { s1: "ab", s2: "eidbaooo", expected: true },
  { s1: "ab", s2: "eidboaoo", expected: false },
])("checkInclusion($s1, $s2)", ({ s1, s2, expected }) => {
  expect(checkInclusion(s1, s2)).toBe(expected);
});
