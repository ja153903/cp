#![allow(dead_code)]
struct Solution;

impl Solution {
    pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
        let mut left: i32 = 0;
        let mut right: i32 = matrix.len() as i32 - 1;

        while left <= right {
            let mid = left + (right - left) / 2;

            let row = &matrix[mid as usize];

            let first = row.first().unwrap();
            let last = row.last().unwrap();

            if target >= *first && target <= *last {
                // search within here
                let mut row_left: i32 = 0;
                let mut row_right: i32 = row.len() as i32 - 1;

                while row_left <= row_right {
                    let row_mid = row_left + (row_right - row_left) / 2;
                    let value = row[row_mid as usize];

                    if value == target {
                        return true;
                    } else if value < target {
                        row_left = row_mid + 1;
                    } else {
                        row_right = row_mid - 1;
                    }
                }

                return false;
            } else if *first > target {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        false
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    pub fn test_search_matrix() {
        let matrix = vec![vec![1, 3, 5, 7], vec![10, 11, 16, 20], vec![23, 30, 34, 60]];
        let target = 3;

        assert_eq!(Solution::search_matrix(matrix, target), true);
    }

    #[test]
    pub fn test_search_matrix2() {
        let matrix = vec![vec![1, 3, 5, 7], vec![10, 11, 16, 20], vec![23, 30, 34, 60]];
        let target = 13;

        assert_eq!(Solution::search_matrix(matrix, target), false);
    }

    #[test]
    pub fn test_search_matrix3() {
        let matrix = vec![vec![1]];
        let target = 1;

        assert_eq!(Solution::search_matrix(matrix, target), true);
    }
}
