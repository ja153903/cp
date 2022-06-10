struct Solution;

impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let mut result = vec![1; nums.len()];

        for i in 1..nums.len() {
            result[i] = result[i - 1] * nums[i - 1];
        }

        let mut right = 1;
        let mut i = nums.len() - 1;

        for i in (0..nums.len()).rev() {
            result[i] *= right;
            right *= nums[i];
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    pub fn product_except_self_should_return_correct_value() {
        let nums = vec![1, 2, 3, 4];
        let expected = vec![24, 12, 8, 6];

        assert_eq!(Solution::product_except_self(nums), expected);
    }
}
