const { isAnagram } = require('../leetcode242');

test.each([
  { s: 'anagram', t: 'nagaram', expected: true },
  { s: 'rat', t: 'car', expected: false },
])('isAnagram($s, $t)', ({ s, t, expected }) => {
  expect(isAnagram(s, t)).toBe(expected);
});
