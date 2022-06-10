struct Codec;

impl Codec {
    fn new() -> Self {
        Codec {}
    }

    fn encode(&self, strs: Vec<String>) -> String {
        strs.iter()
            .map(|str| format!("{}/{}", str.len(), str))
            .collect::<Vec<String>>()
            .join("")
    }

    fn decode(&self, s: String) -> Vec<String> {
        let mut result: Vec<String> = Vec::new();
        let mut start: usize = 0;

        while start < s.len() {
            let slash_idx = *&s[start..].find('/').unwrap() + start;
            let length = *&s[start..slash_idx].parse::<usize>().unwrap_or(0);
            let decoded_word = String::from(&s[(slash_idx + 1)..(slash_idx + 1 + length)]);

            result.push(decoded_word);
            start = slash_idx + 1 + length;
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::Codec;

    #[test]
    pub fn encode_should_encode_properly() {
        let codec = Codec::new();
        let input = vec![String::from("hello"), String::from("world")];
        let output = String::from("5/hello5/world");

        assert_eq!(codec.encode(input), output);
    }

    #[test]
    pub fn decode_should_decode_properly() {
        let codec = Codec::new();
        let input = String::from("5/hello5/world");
        let output = vec![String::from("hello"), String::from("world")];

        assert_eq!(codec.decode(input), output);
    }
}
