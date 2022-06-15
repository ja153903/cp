#![allow(dead_code)]
struct Solution;

impl Solution {
    pub fn daily_temperatures(temperatures: Vec<i32>) -> Vec<i32> {
        let mut stack: Vec<usize> = Vec::new();
        let mut result: Vec<i32> = vec![0; temperatures.len()];

        for (i, &temp) in temperatures.iter().enumerate() {
            while !stack.is_empty() && temperatures[*stack.last().unwrap()] < temp {
                let last = stack.pop().unwrap();
                result[last] = (i - last) as i32;
            }

            stack.push(i);
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    pub fn test_daily_temperatures() {
        let temps = vec![73, 74, 75, 71, 69, 72, 76, 73];
        let expected = vec![1, 1, 4, 2, 1, 1, 0, 0];

        assert_eq!(Solution::daily_temperatures(temps), expected);
    }

    #[test]
    pub fn test_daily_temperatures2() {
        let temps = vec![30, 40, 50, 60];
        let expected = vec![1, 1, 1, 0];

        assert_eq!(Solution::daily_temperatures(temps), expected);
    }

    #[test]
    pub fn test_daily_temperatures3() {
        let temps = vec![30, 60, 90];
        let expected = vec![1, 1, 0];

        assert_eq!(Solution::daily_temperatures(temps), expected);
    }
}
