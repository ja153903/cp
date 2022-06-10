#![allow(dead_code)]
struct Solution;

impl Solution {
    pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
        let mut left: usize = 0;
        let mut right = numbers.len() - 1;

        while left < right {
            let current = numbers[left] + numbers[right];
            if current == target {
                return vec![(left + 1) as i32, (right + 1) as i32];
            } else if current < target {
                left += 1;
            } else {
                right -= 1;
            }
        }

        vec![]
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    pub fn two_sum_should_return_valid_solution() {
        let numbers = vec![2, 7, 11, 15];
        let target = 9;

        assert_eq!(Solution::two_sum(numbers, target), vec![1, 2]);
    }
}
