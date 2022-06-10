#![allow(dead_code)]
struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut encounter: HashMap<char, i32> = HashMap::new();
        let mut start: i32 = 0;
        let mut max_len: i32 = 0;

        for (i, c) in s.chars().enumerate() {
            if let Some(prev) = encounter.get(&c) {
                start = start.max(*prev + 1);
            }

            encounter.insert(c, i as i32);
            max_len = max_len.max(i as i32 - start + 1);
        }

        max_len
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    pub fn length_of_longest_substring_should_return_valid_solution() {
        let s = "abcabcbb".to_string();
        assert_eq!(Solution::length_of_longest_substring(s), 3);
    }
}
