#![allow(dead_code)]
struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn successful_pairs(spells: Vec<i32>, potions: Vec<i32>, success: i64) -> Vec<i32> {
        let mut result: Vec<i32> = vec![0; spells.len()];
        let mut computed: HashMap<i32, i32> = HashMap::new();

        for (i, &spell) in spells.iter().enumerate() {
            if let Some(count) = computed.get(&spell) {
                result[i] = *count;
            } else {
                let mut count = 0;
                for &potion in potions.iter() {
                    if potion as i64 * spell as i64 >= success {
                        count += 1;
                    }
                }
                result[i] = count;
                computed.insert(spell, count);
            }
        }

        result
    }
}
