/**
 * @param {string} key
 * @param {string} message
 * @return {string}
 */
const decodeMessage = function (key, message) {
  const map = new Map();
  let idx = 0;
  for (let i = 0; i < key.length; i++) {
    if (key[i] === ' ') {
      continue;
    }

    if (!map.has(key[i])) {
      map.set(key[i], idx);
      idx++;
    }
  }

  return message
    .split('')
    .map((ch) => {
      if (ch === ' ') {
        return ' ';
      }

      const charCode = map.get(ch) + 97;

      return String.fromCharCode(charCode);
    })
    .join('');
};

module.exports = { decodeMessage };
