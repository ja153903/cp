#![allow(dead_code)]
struct Solution;

use std::collections::VecDeque;

impl Solution {
    pub fn generate_parenthesis(n: i32) -> Vec<String> {
        let mut result: Vec<String> = Vec::new();
        let mut queue: VecDeque<(i32, i32, String)> = VecDeque::new();

        queue.push_back((1, 0, String::from("(")));

        while !queue.is_empty() {
            let (open, close, s) = queue.pop_front().unwrap();

            if s.len() as i32 == 2 * n {
                result.push(s);
            } else {
                if open < n {
                    queue.push_back((open + 1, close, format!("{}(", s)));
                }

                if close < open {
                    queue.push_back((open, close + 1, format!("{})", s)));
                }
            }
        }

        result
    }
}
