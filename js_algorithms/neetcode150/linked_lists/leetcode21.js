function ListNode(val, next) {
  this.val = val ?? 0;
  this.next = next ?? null;
}

/**
 * @param {ListNode} a
 * @param {ListNode} b
 * @return {ListNode}
 */
const mergeTwoLists = function (a, b) {
  if (!a && !b) {
    return null;
  }

  if (!a) {
    return b;
  }

  if (!b) {
    return a;
  }

  if (a.val < b.val) {
    a.next = mergeTwoLists(a.next, b);
    return a;
  }

  b.next = mergeTwoLists(a, b.next);
  return b;
};

module.exports = { mergeTwoLists };
