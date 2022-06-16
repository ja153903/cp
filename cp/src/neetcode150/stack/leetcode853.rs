#![allow(dead_code)]
struct Solution;

#[derive(Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Data {
    pub position: i32,
    pub speed: i32,
}

impl Solution {
    pub fn car_fleet(target: i32, position: Vec<i32>, speed: Vec<i32>) -> i32 {
        let mut items: Vec<Data> = Vec::new();

        for (pos, spd) in position.iter().zip(speed.iter()) {
            items.push(Data {
                position: *pos,
                speed: *spd,
            });
        }

        items.sort_by(|a, b| a.position.cmp(&b.position));

        let mut cur: f32 = 0 as f32;
        let mut result: i32 = 0;

        for data in items.iter().rev() {
            let x = (target - data.position) as f32 / data.speed as f32;
            if x > cur {
                result += 1;
                cur = x;
            }
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    pub fn test_car_fleet() {
        let target = 12;
        let position = vec![10, 8, 0, 5, 3];
        let speed = vec![2, 4, 1, 1, 3];
        let expected = 3;

        assert_eq!(Solution::car_fleet(target, position, speed), expected);
    }
}
