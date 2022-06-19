use std::collections::HashMap;

struct TimeMapNode {
    value: String,
    timestamp: i32,
}

struct TimeMap {
    store: HashMap<String, Vec<TimeMapNode>>,
}

impl TimeMap {
    fn new() -> Self {
        TimeMap {
            store: HashMap::new(),
        }
    }

    fn set(&mut self, key: String, value: String, timestamp: i32) {
        self.store
            .entry(key)
            .or_insert_with(Vec::new)
            .push(TimeMapNode { value, timestamp });
    }

    fn get(&self, key: String, timestamp: i32) -> String {
        if let Some(nodes) = self.store.get(&key) {
            let mut left = 0;
            let mut right = nodes.len() as i32 - 1;

            while left < right {
                let mid = left + (right - left) / 2;

                // if the timestamp in the middle is greater than the current timestamp
                // then we should reduce the size of right
                if nodes[mid as usize].timestamp > timestamp {
                    right = mid;
                } else {
                    left = mid + 1;
                }
            }

            if nodes[left as usize].timestamp <= timestamp {
                nodes[left as usize].value.clone()
            } else {
                String::from("")
            }
        } else {
            String::from("")
        }
    }
}

#[cfg(test)]
mod tests {
    use super::TimeMap;

    #[test]
    pub fn test_timemap() {
        let mut timemap = TimeMap::new();
        timemap.set(String::from("foo"), String::from("bar"), 1);

        assert_eq!(timemap.get(String::from("foo"), 1), "bar");
        assert_eq!(timemap.get(String::from("foo"), 3), "bar");

        timemap.set("foo".to_string(), "bar2".to_string(), 4);

        assert_eq!(timemap.get(String::from("foo"), 4), "bar2");
        assert_eq!(timemap.get(String::from("foo"), 5), "bar2");
    }
}
