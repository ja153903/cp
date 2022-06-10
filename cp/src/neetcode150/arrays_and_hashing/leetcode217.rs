struct Solution;

use std::collections::HashSet;

impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut unique = HashSet::new();

        for num in nums {
            if unique.contains(&num) {
                return true;
            }

            unique.insert(num);
        }

        false
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    pub fn contains_duplicate_should_return_false() {
        assert_eq!(Solution::contains_duplicate(vec![1, 2, 3, 4]), false);
    }
}
