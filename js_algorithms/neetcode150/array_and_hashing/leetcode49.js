const { sortString } = require("../../utils/sort");

/**
 * 49. Group Anagrams
 *
 * Given an array of strings strs, group the anagrams together. You can return the answer in any order.
 *
 * An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
 * typically using all the original letters exactly once.
 *
 * @param {string[]} strs
 * @return {string[][]}
 */
const groupAnagrams = function (strs) {
  const groups = new Map();

  for (const str of strs) {
    const key = sortString(str);
    if (groups.has(key)) {
      groups.get(key).push(str);
    } else {
      groups.set(key, [str]);
    }
  }

  return [...groups.values()];
};

module.exports = { groupAnagrams };
