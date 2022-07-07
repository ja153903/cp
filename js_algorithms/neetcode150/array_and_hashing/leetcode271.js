/**
 * Encodes a list of strings to a single string.
 *
 * @param {string[]} strs
 * @return {string}
 */
const encode = function (strs) {
  return strs.map((str) => `${str.length}/${str}`).join('');
};

/**
 * Decodes a single string to a list of strings.
 *
 * @param {string} s
 * @return {string[]}
 */
const decode = function (s) {
  const result = [];
  let start = 0;

  while (start < s.length) {
    const slash = s.indexOf('/', start);
    const length = parseInt(s.substring(start, slash));
    const subResult = s.substring(slash + 1, slash + length + 1);

    result.push(subResult);
    start = slash + length + 1;
  }

  return result;
};

module.exports = { encode, decode };
