#![allow(dead_code)]
struct MinStack {
    items: Vec<(i32, i32)>,
}

impl MinStack {
    fn new() -> Self {
        MinStack { items: vec![] }
    }

    fn push(&mut self, val: i32) {
        if self.items.is_empty() {
            self.items.push((val, val));
        } else {
            let min = self.get_min();
            self.items.push((val, min.min(val)));
        }
    }

    fn pop(&mut self) {
        self.items.pop();
    }

    fn top(&self) -> i32 {
        if let Some(&item) = self.items.last() {
            item.0
        } else {
            -1
        }
    }

    fn get_min(&self) -> i32 {
        if let Some(&item) = self.items.last() {
            item.1
        } else {
            0
        }
    }
}
