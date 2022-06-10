struct Solution;

use crate::utility::counter::create_char_counter;

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let mut s_counter = create_char_counter(s.chars());

        for ch in t.chars() {
            if !s_counter.contains_key(&ch) || *s_counter.get(&ch).unwrap() == 0 {
                return false;
            }

            *s_counter.entry(ch).or_insert(1) -= 1;
        }

        s_counter.values().sum::<i32>() == 0
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    pub fn is_anagram_should_return_true() {
        let s = String::from("anagram");
        let t = String::from("nagaram");

        assert_eq!(Solution::is_anagram(s, t), true);
    }

    #[test]
    pub fn is_anagram_should_return_false() {
        let s = String::from("rat");
        let t = String::from("car");

        assert_eq!(Solution::is_anagram(s, t), false);
    }
}
