struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut groups: HashMap<String, Vec<String>> = HashMap::new();

        for str in strs {
            // sort the string alphabetically
            let mut chars: Vec<char> = str.chars().collect();
            chars.sort_by(|a, b| a.cmp(b));
            let sorted_str = chars.into_iter().collect::<String>();

            groups.entry(sorted_str).or_insert(vec![]).push(str);
        }

        let mut result: Vec<Vec<String>> = Vec::new();

        for value in groups.values() {
            result.push(value.clone());
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    pub fn group_anagrams_should_return_valid_solution() {
        let strs = vec![
            String::from("eat"),
            String::from("tea"),
            String::from("tan"),
            String::from("ate"),
            String::from("nat"),
            String::from("bat"),
        ];
        let mut solution = Solution::group_anagrams(strs);
        let expected = vec![
            vec![String::from("bat")],
            vec![String::from("tan"), String::from("nat")],
            vec![
                String::from("eat"),
                String::from("tea"),
                String::from("ate"),
            ],
        ];

        solution.sort_by(|a, b| a.len().cmp(&b.len()));

        assert_eq!(solution, expected);
    }
}
