const { minWindow } = require('../leetcode76');

test.each([
  { s: 'ADOBECODEBANC', t: 'ABC', expected: 'BANC' },
  { s: 'a', t: 'a', expected: 'a' },
  { s: 'a', t: 'b', expected: '' },
])('minWindow($s, $t)', ({ s, t, expected }) => {
  expect(minWindow(s, t)).toBe(expected);
});
