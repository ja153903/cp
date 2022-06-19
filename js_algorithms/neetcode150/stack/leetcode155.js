const MinStack = function () {
  this.stack = [];
};

/**
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function (val) {
  if (this.stack.length) {
    const min = this.getMin();
    this.stack.push([val, Math.min(min, val)]);
  } else {
    this.stack.push([val, val]);
  }
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function () {
  this.stack.pop();
};

/**
 * @return {number}
 */
MinStack.prototype.top = function () {
  const last = this.stack[this.stack.length - 1];
  return last[0];
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function () {
  const last = this.stack[this.stack.length - 1];
  return last[1];
};
