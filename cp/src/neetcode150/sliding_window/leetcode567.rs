#![allow(dead_code)]
struct Solution;

use crate::utility::char::{char_at, to_usize_as_lower};

impl Solution {
    pub fn check_inclusion(s1: String, s2: String) -> bool {
        let mut freq = [0; 26];

        for ch in s1.chars() {
            freq[to_usize_as_lower(ch)] += 1;
        }

        let mut start: usize = 0;
        let mut end: usize = 0;
        let mut target: usize = s1.len();

        while end < s2.len() {
            let current = char_at(s2.as_str(), end);
            let current_as_usize = to_usize_as_lower(current);

            if freq[current_as_usize] > 0 {
                target -= 1;
            }

            freq[current_as_usize] -= 1;
            end += 1;

            if target == 0 {
                return true;
            }

            if end - start == s1.len() {
                let start_char = char_at(s2.as_str(), start);
                let start_char_as_usize = to_usize_as_lower(start_char);

                if freq[start_char_as_usize] >= 0 {
                    target += 1;
                }
                freq[start_char_as_usize] += 1;
                start += 1;
            }
        }

        false
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    pub fn check_inclusion_should_return_valid_solution() {
        let s1 = String::from("ab");
        let s2 = String::from("eidbaooo");

        assert_eq!(Solution::check_inclusion(s1, s2), true);

        let s1 = String::from("ab");
        let s2 = String::from("eidboaoo");

        assert_eq!(Solution::check_inclusion(s1, s2), false);
    }
}
