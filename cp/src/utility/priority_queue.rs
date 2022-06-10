use std::cmp::Ordering;

#[derive(Copy, Clone)]
pub struct PrioritizedItem<T: PartialEq> {
    pub priority: i32,
    pub item: T,
}

impl<T: PartialEq> PartialEq<Self> for PrioritizedItem<T> {
    fn eq(&self, other: &Self) -> bool {
        self.item == other.item
    }
}

impl<T: PartialEq> Eq for PrioritizedItem<T> {}

impl<T: PartialEq> PartialOrd<Self> for PrioritizedItem<T> {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl<T: PartialEq> Ord for PrioritizedItem<T> {
    fn cmp(&self, other: &Self) -> Ordering {
        self.priority.cmp(&other.priority)
    }
}
