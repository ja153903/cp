#![allow(dead_code)]
struct Solution;

impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {
        let mut left: usize = 0;
        let mut right: usize = height.len() - 1;

        let mut max_left: i32 = height[left];
        let mut max_right: i32 = height[right];

        let mut result: i32 = 0;

        while left < right {
            if height[left] < height[right] {
                if height[left] > max_left {
                    max_left = height[left];
                } else {
                    result += max_left - height[left];
                }

                left += 1;
            } else {
                if height[right] > max_right {
                    max_right = height[right];
                } else {
                    result += max_right - height[right];
                }

                right -= 1;
            }
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    pub fn trap_should_return_valid_solution() {
        let height = vec![0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1];
        let expected = 6;

        assert_eq!(Solution::trap(height), expected);
    }
}
