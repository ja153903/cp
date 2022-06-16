#![allow(dead_code)]
struct Solution;

use std::collections::VecDeque;

impl Solution {
    pub fn min_path_cost(grid: Vec<Vec<i32>>, move_cost: Vec<Vec<i32>>) -> i32 {
        let rows = grid.len();
        let cols = grid[0].len();

        let mut queue: VecDeque<(i32, i32, i32, usize)> = VecDeque::new();
        let mut result = i32::MAX;

        for col in 0..cols {
            queue.push_back((grid[0][col], 0, 0, 0 as usize));
        }

        while !queue.is_empty() {
            let (grid_value, p_cost, m_cost, curr_idx) = queue.pop_front().unwrap();

            if curr_idx == rows - 1 {
                result = result.min(grid_value + p_cost + m_cost);
            } else {
                let mvs = &move_cost[grid_value as usize];
                for (i, mv) in mvs.iter().enumerate() {
                    queue.push_back((
                        grid[curr_idx + 1][i],
                        p_cost + grid_value,
                        m_cost + mv,
                        curr_idx + 1,
                    ));
                }
            }
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    pub fn test_min_path_cost() {
        let grid = vec![vec![5, 3], vec![4, 0], vec![2, 1]];
        let move_cost = vec![
            vec![9, 8],
            vec![1, 5],
            vec![10, 12],
            vec![18, 6],
            vec![2, 4],
            vec![14, 3],
        ];

        assert_eq!(Solution::min_path_cost(grid, move_cost), 17);
    }

    #[test]
    pub fn test_min_path_cost2() {
        let grid = vec![vec![5, 1, 2], vec![4, 0, 3]];
        let move_cost = vec![
            vec![12, 10, 15],
            vec![20, 23, 8],
            vec![21, 7, 1],
            vec![8, 1, 13],
            vec![9, 10, 25],
            vec![5, 3, 2],
        ];

        assert_eq!(Solution::min_path_cost(grid, move_cost), 6);
    }
}
