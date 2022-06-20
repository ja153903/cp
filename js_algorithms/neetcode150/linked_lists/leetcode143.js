function ListNode(val, next) {
  this.val = val ?? 0;
  this.next = next ?? null;
}

/**
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */
const reorderList = function (head) {
  // go through half of the list
  // reverse the second half of the list
  // once we do this, we would have two pointers
  // one from the beginning and another one from the end of the list
  let slow = head;
  let fast = head;

  // 1 -> 2 -> 3 -> 4
  // 1 -> 2 -> 3 -> 4 -> 5
  while (fast?.next) {
    slow = slow.next;
    fast = fast.next.next;
  }

  let otherHalf = null;

  if (slow?.next) {
    let temp = slow.next;
    slow.next = null;
    otherHalf = reverse(temp);
  }

  let result = head;

  while (result && otherHalf) {
    // store the next node
    let temp = result.next;
    // the next node should really be otherHalf
    result.next = otherHalf;
    otherHalf = temp;
    result = result.next;
  }
};

function reverse(head) {
  let prev = null;
  let curr = head;

  while (curr) {
    const next = curr.next;
    curr.next = prev;
    prev = curr;
    curr = next;
  }

  return prev;
}

module.exports = { reorderList };
