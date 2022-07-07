/**
 * @param {string[]} tokens
 * @return {number}
 */
const evalRPN = function (tokens) {
  const stack = [];
  const ops = ['+', '-', '*', '/'];

  for (const token of tokens) {
    if (ops.includes(token)) {
      const second = parseInt(stack.pop());
      const first = parseInt(stack.pop());

      switch (token) {
        case '+':
          stack.push((first + second).toString());
          break;
        case '-':
          stack.push((first - second).toString());
          break;
        case '*':
          stack.push((first * second).toString());
          break;
        case '/':
          stack.push(Math.trunc(first / second).toString());
          break;
      }
    } else {
      stack.push(token);
    }
  }

  return stack.pop();
};

module.exports = evalRPN;
