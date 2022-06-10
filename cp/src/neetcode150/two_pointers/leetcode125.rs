#![allow(dead_code)]
struct Solution;

impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let cleaned = s
            .chars()
            .filter(|ch| ch.is_alphanumeric())
            .map(|ch| ch.to_lowercase().to_string())
            .collect::<String>();

        if cleaned.is_empty() {
            return true;
        }

        let mut i: usize = 0;
        let mut j: usize = cleaned.len() - 1;

        while i < j {
            if &cleaned[i..(i + 1)] != &cleaned[j..(j + 1)] {
                return false;
            }
            i += 1;
            j -= 1;
        }

        true
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    pub fn is_palindrome_should_return_true() {
        assert_eq!(
            Solution::is_palindrome(String::from("A man, a plan, a canal: Panama")),
            true
        );
        assert_eq!(Solution::is_palindrome(String::from(" ")), true);
    }
}
