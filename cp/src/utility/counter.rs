use std::collections::HashMap;
use std::str::Chars;

pub fn create_counter(nums: Vec<i32>) -> HashMap<i32, i32> {
    let mut counter = HashMap::new();
    for num in nums {
        *counter.entry(num).or_insert(0) += 1;
    }
    counter
}

pub fn create_char_counter(chars: Chars<'_>) -> HashMap<char, i32> {
    let mut counter = HashMap::new();
    for ch in chars {
        *counter.entry(ch).or_insert(0) += 1;
    }
    counter
}


#[cfg(test)]
mod tests {
    use super::{create_counter, create_char_counter};

    #[test]
    pub fn create_counter_should_test_with_vector() {
        let vector: Vec<i32> = vec![1, 1, 1, 1, 1, 2];
        let counter = create_counter(vector);

        assert_eq!(*counter.get(&1).unwrap(), 5);
        assert_eq!(*counter.get(&2).unwrap(), 1);
    }

    #[test]
    pub fn create_char_counter_should_test_with_string() {
        let test_string = String::from("hello, world");
        let counter = create_char_counter(test_string.chars());

        assert_eq!(*counter.get(&'l').unwrap(), 3);
    }
}
