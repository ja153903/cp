#![allow(dead_code)]
struct Solution;

impl Solution {
    pub fn calculate_tax(brackets: Vec<Vec<i32>>, mut income: i32) -> f64 {
        if income == 0 {
            return 0 as f64;
        }

        let mut result: f64 = 0 as f64;

        for i in 0..brackets.len() {
            let percentile = brackets[i][1] as f64 / 100.0;

            // if the current i is 0, then we should just subtract the percentile
            let amount_to_tax = if i == 0 {
                income.min(brackets[i][0])
            } else {
                // if the current i is non-zero, then how much we take away
                // is the minimum between the remaining income and the difference between two uppers
                income.min(brackets[i][0] - brackets[i - 1][0])
            };
            income -= amount_to_tax;
            result += amount_to_tax as f64 * percentile;
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    pub fn test_calculate_tax() {
        let brackets = vec![vec![3, 50], vec![7, 10], vec![12, 25]];
        let income = 10;

        assert_eq!(Solution::calculate_tax(brackets, income), 2.65000);
    }

    #[test]
    pub fn test_calculate_tax2() {
        let brackets = vec![vec![1, 0], vec![4, 25], vec![5, 50]];
        let income = 2;

        assert_eq!(Solution::calculate_tax(brackets, income), 0.25000);
    }
}
