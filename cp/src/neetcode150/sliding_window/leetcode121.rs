#![allow(dead_code)]
struct Solution;

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut profit = 0;
        let mut min_buy = prices[0];

        for i in 1..prices.len() {
            min_buy = min_buy.min(prices[i]);
            profit = profit.max(prices[i] - min_buy);
        }

        profit
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    pub fn max_profit_should_return_valid_solution() {
        let prices = vec![7, 1, 5, 3, 6, 4];
        assert_eq!(Solution::max_profit(prices), 5);
    }
}
