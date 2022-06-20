function ListNode(val, next) {
  this.val = val ?? 0;
  this.next = next ?? null;
}

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
const reverseList = function (head) {
  let prev = null;
  let curr = head;

  while (curr) {
    const next = curr.next;
    curr.next = prev;
    prev = curr;
    curr = next;
  }

  return prev;
};

module.exports = { reverseList };
