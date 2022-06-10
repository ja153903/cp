/**
 * 3. Longest Substring Without Repeating Characters
 *
 * Given a string s, find the length of the longest substring without repeating characters.
 *
 * @param {string} s
 * @return {number}
 */
const lengthOfLongestSubstring = function (s) {
  // keep track of items in map
  const seen = new Map();
  let max = 0,
    start = 0;

  for (let i = 0; i < s.length; i++) {
    // if we've seen the character before, we need to update the start of the window
    if (seen.has(s[i])) {
      start = Math.max(start, seen.get(s[i]) + 1);
    }

    seen.set(s[i], i);
    max = Math.max(max, i - start + 1);
  }

  return max;
};

module.exports = { lengthOfLongestSubstring };
