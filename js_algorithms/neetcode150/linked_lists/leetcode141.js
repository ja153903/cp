function ListNode(val, next) {
  this.val = val ?? 0;
  this.next = next ?? null;
}

/**
 * @param {ListNode} head
 * @return {boolean}
 */
const hasCycle = function (head) {
  let slow = head;
  let fast = head;

  while (fast?.next) {
    slow = slow.next;
    fast = fast.next.next;

    if (slow === fast) {
      return true;
    }
  }

  return false;
};

module.exports = { hasCycle };
