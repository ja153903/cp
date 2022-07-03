/**
 * This solution is TLE
 *
 * @param {number} n
 * @param {number} delay
 * @param {number} forget
 * @return {number}
 */
const peopleAwareOfSecret = function (n, delay, forget) {
  // since result can be extremely large let's avoid O(n) space
  // when trying to find the total value
  const MOD = Math.pow(10, 9) + 7;
  const deque = [];

  deque.push({ forgetAt: forget + 1, canShareAt: delay + 1 });

  for (let i = 1; i <= n; i++) {
    // remove any values that should be forgotten
    while (deque.length && deque[0].forgetAt === i) {
      deque.shift();
    }

    const size = deque.length;
    for (let j = 0; j < size; j++) {
      if (i >= deque[j].canShareAt) {
        deque.push({
          canShareAt: i + delay,
          forgetAt: i + forget,
        });
      }
    }
  }

  return deque.length % MOD;
};

export default peopleAwareOfSecret;
