#![allow(dead_code)]
struct Solution;

use std::collections::VecDeque;

impl Solution {
    pub fn max_sliding_window(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut result: Vec<i32> = Vec::new();
        let mut queue: VecDeque<usize> = VecDeque::new();
        let k: usize = k as usize;

        for (end, &num) in nums.iter().enumerate() {
            // if the index is outside of the window, then we should get rid of the value in the front of the queue
            while !queue.is_empty() && end >= k && *queue.front().unwrap() < (end - k + 1) {
                queue.pop_front();
            }

            // if the value in the back of the queue is less than the current item, we should remove it
            while !queue.is_empty() && nums[*queue.back().unwrap()] < num {
                queue.pop_back();
            }

            queue.push_back(end);

            if end >= k - 1 {
                result.push(nums[*queue.front().unwrap()]);
            }
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    pub fn max_sliding_window_test_case1() {
        let nums = vec![1, 3, -1, -3, 5, 3, 6, 7];
        let k = 3;

        let expected = vec![3, 3, 5, 5, 6, 7];

        assert_eq!(Solution::max_sliding_window(nums, k), expected);
    }
}
