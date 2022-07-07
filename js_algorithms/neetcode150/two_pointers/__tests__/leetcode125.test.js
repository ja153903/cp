const { isPalindrome } = require('../leetcode125');

test.each([
  { s: 'A man, a plan, a canal: Panama', expected: true },
  { s: 'race a car', expected: false },
])('isPalindrome($s)', ({ s, expected }) => {
  expect(isPalindrome(s)).toBe(expected);
});
