const generateCounter = require("../../utils/generateCounter");
const sum = require("../../utils/sum");

/**
 * 242. Valid Anagram
 *
 * Given two strings s and t, return true if t is an anagram of s, and false otherwise.
 *
 * An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
 * typically using all the original letters exactly once.
 *
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
const isAnagram = function (s, t) {
  const sCounter = generateCounter(s.split(""));

  for (const ch of t) {
    const currentCount = sCounter.get(ch) ?? 0;
    if (currentCount === 0) {
      return false;
    }

    sCounter.set(ch, currentCount - 1);
  }

  return sum([...sCounter.values()]) === 0;
};

module.exports = { isAnagram };
