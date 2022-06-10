struct Solution;

use crate::utility::priority_queue::PrioritizedItem;
use std::collections::{BinaryHeap, HashMap};

impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut frequency: HashMap<i32, i32> = HashMap::new();
        let mut heap = BinaryHeap::new();

        for num in nums {
            *frequency.entry(num).or_insert(0) += 1;
        }

        for (&key, &count) in frequency.iter() {
            // we use negative priority here because by default
            // binary heap is a max heap
            heap.push(PrioritizedItem {
                priority: -count,
                item: key,
            });

            if heap.len() > (k as usize) {
                heap.pop();
            }
        }

        heap.into_vec()
            .iter()
            .map(|item| item.item)
            .collect::<Vec<i32>>()
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    pub fn top_k_frequent_should_return_correct_value() {
        let nums = vec![1, 1, 1, 2, 2, 3];
        let k: i32 = 2;
        let expected = vec![1, 2];
        let mut solution = Solution::top_k_frequent(nums, k);
        solution.sort_by(|a, b| a.cmp(b));

        assert_eq!(solution, expected);
    }
}
