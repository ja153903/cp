/**
 * 567. Permutation in String
 *
 * Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
 *
 * In other words, return true if one of s1's permutations is the substring of s2.
 *
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
const checkInclusion = function (s1, s2) {
  const freq = new Map();

  for (const ch of s1) {
    freq.set(ch, (freq.get(ch) ?? 0) + 1);
  }

  const target = s1.length;

  for (let i = 0; i < s2.length; i++) {
    const ch = s2[i];
    if (freq.has(ch)) {
      freq.set(ch, (freq.get(ch) ?? 0) - 1);
    }

    const start = s2[i - target];
    if (i - target >= 0 && freq.has(start)) {
      freq.set(start, (freq.get(start) ?? 0) + 1);
    }

    if (_allZero(freq)) {
      return true;
    }
  }

  return false;
};

function _allZero(map) {
  for (const value of map.values()) {
    if (value !== 0) {
      return false;
    }
  }

  return true;
}

module.exports = { checkInclusion };
