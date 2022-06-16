#![allow(dead_code)]
struct Solution;

impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let n = nums.len() as i32;
        let mut left: i32 = 0;
        let mut right: i32 = n - 1;

        while left < right {
            let mid = left + (right - left) / 2;
            if nums[mid as usize] > nums[right as usize] {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        let pivot = left;

        left = 0;
        right = n - 1;

        while left <= right {
            let mid = left + (right - left) / 2;
            let real_mid = (mid + pivot) % n;

            if nums[real_mid as usize] == target {
                return real_mid;
            } else if nums[real_mid as usize] < target {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        -1
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    pub fn test_search1() {
        let nums = vec![4, 5, 6, 7, 0, 1, 2];
        let target = 0;

        assert_eq!(Solution::search(nums, target), 4);
    }
}
