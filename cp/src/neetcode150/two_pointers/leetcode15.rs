#![allow(dead_code)]
struct Solution;

impl Solution {
    pub fn three_sum(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
        if nums.len() < 3 {
            return vec![];
        }

        let mut result = Vec::new();
        nums.sort();

        for i in 0..(nums.len() - 2) {
            if i == 0 || (i > 0 && nums[i] != nums[i - 1]) {
                let mut j = i + 1;
                let mut k = nums.len() - 1;

                while j < k {
                    let current = nums[i] + nums[j] + nums[k];
                    if current == 0 {
                        result.push(vec![nums[i], nums[j], nums[k]]);

                        while j < k && nums[j] == nums[j + 1] {
                            j += 1;
                        }

                        while j < k && nums[k] == nums[k - 1] {
                            k -= 1;
                        }

                        j += 1;
                        k -= 1;
                    } else if current < 0 {
                        j += 1;
                    } else {
                        k -= 1;
                    }
                }
            }
        }

        result
    }
}
