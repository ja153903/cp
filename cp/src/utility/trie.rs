use std::borrow::Borrow;
use std::cell::Cell;
use std::collections::HashMap;

pub struct TrieNode {
    is_word: bool,
    children: Cell<HashMap<char, TrieNode>>,
}

pub struct Trie {
    root: TrieNode,
}

impl Trie {
    fn new() -> Self {
        Trie {
            root: TrieNode {
                is_word: false,
                children: Cell::new(HashMap::new()),
            },
        }
    }

    fn insert(&mut self, word: String) {
        let mut current = &self.root;
        let word_len = word.len();
        for (i, ch) in word.chars().enumerate() {
            let mut map = current.children.borrow().get_mut();
            if Some(node) = map.get(&ch) {
                current = node;
            } else {
                let node = TrieNode {
                    is_word: false,
                    children: Cell::new(HashMap::new()),
                };
                map.insert(ch, node);
                current = &node;
            }
        }

        current.is_word = true;
    }

    fn search(&self, word: String) -> bool {}

    fn starts_with(&self, prefix: String) -> bool {}
}
