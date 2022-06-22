function ListNode(val, next) {
  this.val = val ?? 0;
  this.next = next ?? null;
}

/**
 *
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
const addTwoNumbers = function (l1, l2) {
  let result = new ListNode(0);
  let carry = 0;

  let runner = result;

  while (l1 || l2) {
    let current = carry;

    if (l1) {
      current += l1.val;
      l1 = l1.next;
    }

    if (l2) {
      current += l2.val;
      l2 = l2.next;
    }

    carry = Math.floor(current / 10);
    runner.next = new ListNode(current % 10);

    runner = runner.next;
  }

  if (carry > 0) {
    runner.next = new ListNode(carry);
  }

  return result.next;
};

module.exports = { addTwoNumbers };
