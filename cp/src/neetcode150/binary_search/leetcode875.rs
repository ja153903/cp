#![allow(dead_code)]
struct Solution;

impl Solution {
    pub fn min_eating_speed(piles: Vec<i32>, h: i32) -> i32 {
        let max_bananas = *piles.iter().max().unwrap();

        let mut left = 1;
        let mut right = max_bananas;

        while left < right {
            let mid = left + (right - left) / 2;
            let can_finish = Solution::can_finish(&piles, mid, h);

            if can_finish {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        right
    }

    fn can_finish(piles: &Vec<i32>, k: i32, h: i32) -> bool {
        let mut result = 0;

        for pile in piles {
            result += pile / k;
            if pile % k > 0 {
                result += 1;
            }
        }

        result <= h
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    pub fn test_min_eating_speed1() {
        let piles = vec![3, 6, 7, 11];
        let h = 8;

        assert_eq!(Solution::min_eating_speed(piles, h), 4);
    }

    #[test]
    pub fn test_min_eating_speed2() {
        let piles = vec![30, 11, 23, 4, 20];
        let h = 5;

        assert_eq!(Solution::min_eating_speed(piles, h), 30);
    }
}
