function ListNode(val, next) {
  this.val = val ?? 0;
  this.next = next ?? null;
}

/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
const removeNthFromEnd = function (head, n) {
  let start = new ListNode(0);
  let slow = start;
  let fast = start;

  // this connects both slow and fast to head
  slow.next = head;

  // go through the first n elements
  for (let i = 0; i <= n; i++) {
    fast = fast.next;
  }

  while (fast) {
    slow = slow.next;
    fast = fast.next;
  }

  slow.next = slow.next.next;

  return start.next;
};

module.exports = { removeNthFromEnd };
