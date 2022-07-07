/**
 * sortString sorts a string in alphabetic order
 *
 * @param {string} s
 * @return {string}
 */
function sortString(s) {
  if (s.length <= 1) {
    return s;
  }

  return s
    .split('')
    .sort((a, b) => a.localeCompare(b))
    .join('');
}

module.exports = { sortString };
