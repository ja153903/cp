#![allow(dead_code)]
struct Solution;

use std::collections::HashSet;

//A password is said to be strong if it satisfies all the following criteria:
//
// It has at least 8 characters.
// It contains at least one lowercase letter.
// It contains at least one uppercase letter.
// It contains at least one digit.
// It contains at least one special character. The special characters are the characters in the following string: "!@#$%^&*()-+".
// It does not contain 2 of the same character in adjacent positions (i.e., "aab" violates this condition, but "aba" does not).
impl Solution {
    pub fn strong_password_checker_ii(password: String) -> bool {
        if password.len() < 8 {
            false
        } else {
            let mut lower_cnt: i32 = 0;
            let mut upper_cnt: i32 = 0;
            let mut digit_cnt: i32 = 0;
            let mut special_cnt: i32 = 0;
            let mut prev: char = ' ';

            let special = String::from("!@#$%^&*()-+");
            let mut special_chars = HashSet::new();

            for ch in special.chars() {
                special_chars.insert(ch);
            }

            for ch in password.chars() {
                if prev == ch {
                    return false;
                } else if ch.is_alphabetic() && ch.is_lowercase() {
                    lower_cnt += 1;
                } else if ch.is_alphabetic() && ch.is_uppercase() {
                    upper_cnt += 1;
                } else if ch.is_digit(10) {
                    digit_cnt += 1;
                } else if special_chars.contains(&ch) {
                    special_cnt += 1;
                }

                prev = ch;
            }

            lower_cnt > 0 && upper_cnt > 0 && digit_cnt > 0 && special_cnt > 0
        }
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    pub fn test_strong_password_checker_ii() {
        assert_eq!(
            Solution::strong_password_checker_ii(String::from("IloveLe3tcode!")),
            true
        );
    }

    #[test]
    pub fn test_strong_password_checker_ii2() {
        assert_eq!(
            Solution::strong_password_checker_ii(String::from("Me+You--IsMyDream")),
            false
        );
    }

    #[test]
    pub fn test_strong_password_checker_ii3() {
        assert_eq!(
            Solution::strong_password_checker_ii(String::from("a1A!A!A!")),
            true
        );
    }
}
