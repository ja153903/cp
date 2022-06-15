#![allow(dead_code)]
struct Solution;

impl Solution {
    pub fn eval_rpn(tokens: Vec<String>) -> i32 {
        let mut stack: Vec<String> = Vec::new();

        for ch in tokens.iter() {
            if Solution::is_operation(ch.as_str()) {
                let b = stack.pop().unwrap();
                let a = stack.pop().unwrap();

                let b_as_i32 = b.parse::<i32>().unwrap();
                let a_as_i32 = a.parse::<i32>().unwrap();

                let result = match ch.as_str() {
                    "+" => a_as_i32 + b_as_i32,
                    "-" => a_as_i32 - b_as_i32,
                    "*" => a_as_i32 * b_as_i32,
                    _ => a_as_i32 / b_as_i32,
                };

                stack.push(result.to_string());
            } else {
                stack.push(ch.clone());
            }
        }

        stack.last().unwrap().parse::<i32>().unwrap()
    }

    fn is_operation(s: &str) -> bool {
        s == "+" || s == "-" || s == "*" || s == "/"
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    pub fn test_eval_rpn() {
        let tokens = vec!["2", "1", "+", "3", "*"]
            .iter()
            .map(|str| str.to_string())
            .collect::<Vec<String>>();
        let expected = 9;

        assert_eq!(Solution::eval_rpn(tokens), expected);
    }

    #[test]
    pub fn test_eval_rpn2() {
        let tokens = vec!["4", "13", "5", "/", "+"]
            .iter()
            .map(|str| str.to_string())
            .collect::<Vec<String>>();
        let expected = 6;

        assert_eq!(Solution::eval_rpn(tokens), expected);
    }

    #[test]
    pub fn test_eval_rpn3() {
        let tokens = vec![
            "10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+",
        ]
        .iter()
        .map(|str| str.to_string())
        .collect::<Vec<String>>();
        let expected = 22;

        assert_eq!(Solution::eval_rpn(tokens), expected);
    }
}
