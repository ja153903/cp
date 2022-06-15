/**
 * 76. Minimum Window Substring
 *
 * Given two strings s and t of lengths m and n respectively, return the minimum window substring of s
 * such that every character in t (including duplicates) is included in the window. If there is no such substring,
 * return the empty string "".
 *
 * The testcases will be generated such that the answer is unique.
 *
 * A substring is a contiguous sequence of characters within the string.
 *
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
const minWindow = function (s, t) {
  if (s.length < t.length) {
    return "";
  }

  const frequency = new Map();
  for (const ch of t) {
    frequency.set(ch, (frequency.get(ch) ?? 0) + 1);
  }

  let target = t.length;
  let start = 0;
  let minStart = 0,
    minLength = Number.MAX_VALUE;

  for (let end = 0; end < s.length; end++) {
    const currentCount = frequency.get(s[end]) ?? 0;
    if (currentCount > 0) {
      target--;
    }
    frequency.set(s[end], currentCount - 1);

    while (target === 0) {
      const windowSize = end - start + 1;
      if (windowSize < minLength) {
        minStart = start;
        minLength = windowSize;
      }

      const startCount = frequency.get(s[start]);
      frequency.set(s[start], startCount + 1);
      if (frequency.get(s[start]) > 0) {
        target++;
      }
      start++;
    }
  }

  if (minLength === Number.MAX_VALUE) {
    return "";
  }

  return s.substring(minStart, minStart + minLength);
};

module.exports = { minWindow };
