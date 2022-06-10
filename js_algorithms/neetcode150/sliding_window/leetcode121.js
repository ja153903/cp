/**
 * 121. Best Time to Buy and Sell Stock
 *
 * You are given an array prices where prices[i] is the price of a given stock on the ith day.
 *
 * You want to maximize your profit by choosing a single day to buy one stock and choosing a
 * different day in the future to sell that stock.
 *
 * Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
 *
 * @param {number[]} prices
 * @return {number}
 */
const maxProfit = function (prices) {
  let minimumPriceToBuy = prices[0];
  let maximumProfit = 0;

  for (let i = 1; i < prices.length; i++) {
    minimumPriceToBuy = Math.min(minimumPriceToBuy, prices[i]);
    maximumProfit = Math.max(maximumProfit, prices[i] - minimumPriceToBuy);
  }

  return maximumProfit;
};

module.exports = { maxProfit };
