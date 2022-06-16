#![allow(dead_code)]
struct Solution;

impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let mut left: i32 = 0;
        let mut right: i32 = nums.len() as i32 - 1;

        while left < right {
            let mid = left + (right - left) / 2;

            if nums[mid as usize] == target {
                return mid;
            } else if nums[mid as usize] < target {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        if nums[left as usize] == target {
            left
        } else {
            -1
        }
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    pub fn test_search1() {
        let nums = vec![-1, 0, 3, 5, 9, 12];
        let target = 9;

        assert_eq!(Solution::search(nums, target), 4);
    }

    #[test]
    pub fn test_search2() {
        let nums = vec![-1, 0, 3, 5, 9, 12];
        let target = 2;

        assert_eq!(Solution::search(nums, target), -1);
    }

    #[test]
    pub fn test_search3() {
        let nums = vec![5];
        let target = -5;

        assert_eq!(Solution::search(nums, target), -1);
    }

    #[test]
    pub fn test_search4() {
        let nums = vec![5];
        let target = 5;

        assert_eq!(Solution::search(nums, target), 0);
    }
}
