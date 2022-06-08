const { isalnum } = require("../../utils/characters");

/**
 * 125. Valid Palindrome
 *
 * A phrase is a palindrome if, after converting all uppercase letters into lowercase
 * letters and removing all non-alphanumeric characters, it reads the same forward and backward.
 * Alphanumeric characters include letters and numbers.
 *
 * Given a string s, return true if it is a palindrome, or false otherwise.
 *
 * @param {string} s
 * @return {boolean}
 */
const isPalindrome = function (s) {
  const filtered = s
    .split("")
    .filter((ch) => isalnum(ch))
    .map((ch) => ch.toLowerCase());

  let i = 0,
    j = filtered.length - 1;

  while (i < j) {
    if (filtered[i] !== filtered[j]) {
      return false;
    }

    i++;
    j--;
  }

  return true;
};

module.exports = { isPalindrome };
