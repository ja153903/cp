#![allow(dead_code)]
struct Solution;

use crate::utility::char::char_at;
use std::collections::HashMap;

impl Solution {
    pub fn min_window(s: String, t: String) -> String {
        if s.len() < t.len() {
            return String::from("");
        }

        let mut freq: HashMap<char, i32> = HashMap::new();

        for ch in t.chars() {
            *freq.entry(ch).or_insert(0) += 1;
        }

        let mut start: usize = 0;

        let mut min_start: usize = 0;
        let mut min_length: usize = usize::MAX;

        let mut target = t.len();

        // go through each character
        for (end, ch) in s.chars().enumerate() {
            *freq.entry(ch).or_insert(0) -= 1;
            if let Some(&count) = freq.get(&ch) {
                if count >= 0 {
                    target -= 1;
                }
            }

            while target == 0 {
                let window_size = end - start + 1;
                if window_size < min_length {
                    min_length = window_size;
                    min_start = start;
                }

                let ch_at_start = char_at(s.as_str(), start);
                *freq.entry(ch_at_start).or_insert(0) += 1;
                if let Some(&count) = freq.get(&ch_at_start) {
                    if count > 0 {
                        target += 1;
                    }
                }

                start += 1;
            }
        }

        if min_length == usize::MAX {
            String::from("")
        } else {
            String::from(&s[min_start..min_start + min_length])
        }
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    pub fn min_window_should_return_min_window() {
        let s = String::from("ADOBECODEBANC");
        let t = String::from("ABC");
        let expected = String::from("BANC");

        assert_eq!(Solution::min_window(s, t), expected);
    }
}
