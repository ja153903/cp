/**
 * @param {number} num
 * @param {number} k
 * @return {number}
 */
const minimumNumbers = function (num, k) {
  if (num === 0) {
    return 0;
  }

  // dp[i] ~ minimum number of items to achieve sum i
  let dp = new Array(num + 1).fill(num + 1);
  dp[0] = 0;

  for (let i = 1; i <= num; i++) {
    for (let j = k; j <= num; j += 10) {
      if (i - j >= 0) {
        dp[i] = Math.min(dp[i], dp[i - j] + 1);
      }
    }
  }

  return dp[num] !== num + 1 ? dp[num] : -1;
};

module.exports = { minimumNumbers };
