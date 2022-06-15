#![allow(dead_code)]
struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn character_replacement(s: String, k: i32) -> i32 {
        let mut start: usize = 0;
        let mut max_freq: i32 = 0;
        let mut max_length: i32 = 0;
        let mut freq: HashMap<char, i32> = HashMap::new();

        for (i, c) in s.chars().enumerate() {
            *freq.entry(c).or_insert(0) += 1;
            max_freq = max_freq.max(*freq.get(&c).unwrap());

            while (i - start + 1) as i32 - max_freq > k {
                *freq
                    .entry((&s[start..start + 1]).parse().unwrap())
                    .or_insert(0) -= 1;
                start += 1;
            }

            max_length = max_length.max((i - start + 1) as i32);
        }

        max_length
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    pub fn character_replacement_should_return_valid_solution() {
        let s = "ABAB".to_string();
        assert_eq!(Solution::character_replacement(s, 2), 4);
    }
}
