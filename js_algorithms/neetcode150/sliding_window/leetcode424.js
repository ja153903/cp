/**
 * 424. Longest Repeating Character Replacement
 *
 * You are given a string s and an integer k. You can choose any character of the string
 * and change it to any other uppercase English character. You can perform this operation at most k times.
 *
 * Return the length of the longest substring containing the same letter you can get after
 * performing the above operations.
 *
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
const characterReplacement = function (s, k) {
  const frequency = new Map();
  let maxFrequency = 0,
    maxLength = 0,
    start = 0;

  for (let end = 0; end < s.length; end++) {
    frequency.set(s[end], (frequency.get(s[end]) ?? 0) + 1);
    maxFrequency = Math.max(maxFrequency, frequency.get(s[end]));

    // Window Size - Max Frequency => Number of characters we can replace
    while (end - start + 1 - maxFrequency > k) {
      frequency.set(s[start], frequency.get(s[start]) - 1);
      start++;
    }

    maxLength = Math.max(maxLength, end - start + 1);
  }

  return maxLength;
};

module.exports = { characterReplacement };
