#![allow(dead_code)]
struct Solution;

use std::collections::HashSet;
use std::iter::FromIterator;

impl Solution {
    pub fn longest_consecutive(nums: Vec<i32>) -> i32 {
        let unique: HashSet<i32> = HashSet::from_iter(nums.iter().cloned());
        let mut result = 0;

        for num in nums {
            if !unique.contains(&(num - 1)) {
                let mut current = num;
                let mut current_count = 0;
                while unique.contains(&current) {
                    current_count += 1;
                    current += 1;
                }

                if current_count > result {
                    result = current_count;
                }
            }
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    pub fn longest_consecutive_should_return_correct_count() {
        let nums = vec![100, 4, 200, 1, 3, 2];
        assert_eq!(Solution::longest_consecutive(nums), 4);
    }
}
