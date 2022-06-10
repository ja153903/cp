struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut seen = HashMap::new();

        for (i, val) in nums.iter().enumerate() {
            let complement = target - *val;
            if seen.contains_key(&complement) {
                let value = *seen.get(&complement).unwrap();
                return vec![value as i32, i as i32];
            }

            seen.insert(*val, i);
        }

        vec![]
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    pub fn two_sum_should_return_some_valid_solution() {
        let nums = vec![2, 7, 11, 15];
        let target = 9;
        let expected = vec![0, 1];

        assert_eq!(Solution::two_sum(nums, target), expected);
    }
}
