#![allow(dead_code)]

use std::collections::HashMap;

#[derive(Default)]
pub struct Trie {
    pub is_word: bool,
    pub nodes: HashMap<char, Trie>,
}

impl Trie {
    fn new() -> Self {
        Default::default()
    }

    fn insert(&mut self, word: String) {
        let mut current = self;

        for ch in word.chars() {
            current = current.nodes.entry(ch).or_insert_with(|| Trie::new());
        }
        current.is_word = true;
    }

    fn search(&self, word: String) -> bool {
        let mut current = self;
        for ch in word.chars() {
            if let Some(node) = current.nodes.get(&ch) {
                current = node;
            } else {
                return false;
            }
        }

        current.is_word
    }

    fn starts_with(&self, prefix: String) -> bool {
        let mut current = self;
        for ch in prefix.chars() {
            if let Some(node) = current.nodes.get(&ch) {
                current = node;
            } else {
                return false;
            }
        }

        true
    }
}

#[cfg(test)]
mod tests {
    use super::Trie;

    #[test]
    pub fn test_trie() {
        let mut trie = Trie::new();
        trie.insert(String::from("apple"));

        assert_eq!(trie.starts_with(String::from("app")), true);
    }
}
