/**
 * @param {string} s
 * @return {string}
 */
const greatestLetter = function (s) {
  let upper = new Array(26).fill(0);
  let lower = new Array(26).fill(0);

  for (const ch of s) {
    const code = ch.charCodeAt(0);
    if (code - 97 < 0) {
      upper[code - 65]++;
    } else {
      lower[code - 97]++;
    }
  }

  for (let i = 25; i >= 0; i--) {
    if (upper[i] > 0 && lower[i] > 0) {
      return String.fromCharCode(i + 65);
    }
  }

  return '';
};

module.exports = { greatestLetter };
