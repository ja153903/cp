const { groupAnagrams } = require('../leetcode49');

test.each([
  {
    strs: ['eat', 'tea', 'tan', 'ate', 'nat', 'bat'],
    expected: [['bat'], ['nat', 'tan'], ['ate', 'eat', 'tea']],
  },
])('groupAnagrams($strs)', ({ strs, expected }) => {
  const result = groupAnagrams(strs);
  const sortedResult = [];
  for (const arr of result) {
    sortedResult.push(arr.sort((a, b) => a.localeCompare(b)));
  }
  sortedResult.sort((a, b) => a.length - b.length);

  expect(sortedResult).toEqual(expected);
});
