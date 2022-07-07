/**
 * @param {number} n
 * @return {string[]}
 */
const generateParenthesis = function (n) {
  const result = [];
  const stack = [];
  stack.push({ path: '', open: 0, close: 0 });

  while (stack.length) {
    const { path, open, close } = stack.pop();

    if (path.length === 2 * n) {
      result.push(path);
    } else {
      if (open < n) {
        stack.push({ path: `${path}(`, open: open + 1, close });
      }

      if (close < open) {
        stack.push({ path: `${path})`, open, close: close + 1 });
      }
    }
  }

  return result;
};

module.exports = generateParenthesis;
