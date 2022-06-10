struct Solution;

use std::collections::HashSet;

impl Solution {
    pub fn is_valid_sudoku(board: Vec<Vec<char>>) -> bool {
        let mut hashes: HashSet<String> = HashSet::new();

        for i in 0..board.len() {
            for j in 0..board[i].len() {
                if board[i][j] != '.' {
                    let row_hash = format!("Row {} has value {}", i, board[i][j]);
                    let col_hash = format!("Col {} has value {}", j, board[i][j]);
                    let sub_box_hash =
                        format!("SubBox {} {} has value {}", i / 3, j / 3, board[i][j]);

                    if hashes.contains(&row_hash)
                        || hashes.contains(&col_hash)
                        || hashes.contains(&sub_box_hash)
                    {
                        return false;
                    }

                    hashes.insert(row_hash);
                    hashes.insert(col_hash);
                    hashes.insert(sub_box_hash);
                }
            }
        }

        true
    }
}
