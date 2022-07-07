/**
 * @param {string} s
 * @return {boolean}
 */
const isValid = function (s) {
  const stack = [];

  for (const ch of s) {
    if (ch === '(') {
      stack.push(')');
    } else if (ch === '[') {
      stack.push(']');
    } else if (ch === '{') {
      stack.push('}');
    } else if (!stack.length || stack.pop() !== ch) {
      return false;
    }
  }

  return !stack.length;
};

module.exports = isValid;
