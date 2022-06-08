/**
 * sum computes the sum of a collections of numbers
 *
 * @param {number[]} items
 * @return {number}
 */
function sum(items) {
  const length = items.length;

  if (length === 0) {
    return 0;
  }

  if (length === 1) {
    return items[0];
  }

  return items.reduce((a, b) => a + b);
}

module.exports = sum;
