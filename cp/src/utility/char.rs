pub fn to_usize_as_lower(c: char) -> usize {
    (c as u32 - 'a' as u32) as usize
}

pub fn to_usize_as_upper(c: char) -> usize {
    (c as u32 - 'A' as u32) as usize
}

pub fn char_at(s: &str, i: usize) -> char {
    s[i..i + 1].parse::<char>().unwrap()
}
