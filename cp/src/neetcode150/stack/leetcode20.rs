#![allow(dead_code)]
struct Solution;

impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut stack: Vec<char> = Vec::new();
        for ch in s.chars() {
            match ch {
                '(' => stack.push(')'),
                '{' => stack.push('}'),
                '[' => stack.push(']'),
                n => {
                    if stack.is_empty() {
                        return false;
                    }

                    if let Some(&top) = stack.last() {
                        if top != n {
                            return false;
                        }
                    }
                    stack.pop();
                }
            }
        }

        stack.is_empty()
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    pub fn is_valid_test_case1() {
        let s = String::from("()[]{}");
        assert_eq!(Solution::is_valid(s), true);

        let s = String::from("(]");
        assert_eq!(Solution::is_valid(s), false);
    }
}
